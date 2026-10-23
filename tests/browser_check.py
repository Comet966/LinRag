"""Browser acceptance check. Run: uv run python tests/browser_check.py."""

import socket
import tempfile
import threading
import time
from pathlib import Path

import uvicorn
from playwright.sync_api import expect, sync_playwright

from linrag.app import create_app
from linrag.config import Settings
from linrag.corpus import Chunk
from linrag.index import Index, build_index


def main():
    artifacts = Path("artifacts")
    artifacts.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as directory:
        settings = Settings(data_dir=Path(directory))
        chunks = [
            Chunk(
                "grep",
                "grep",
                "递归搜索",
                "# 递归搜索\n\n- 搜索文件内容\n\n```sh\ngrep -r test .\n```\n\n| 参数 | 含义 |\n| --- | --- |\n| -r | 递归 |\n\n<script>window.untrusted = true</script>",
                "test-fixture",
                "https://github.com/tldr-pages/tldr",
                "test-only",
                "zh",
                "linux",
                "CC-BY-4.0",
                "Test fixture",
            )
        ]
        build_index(settings, chunks, {}, lexical_only=True)

        app = create_app(settings, Index(settings))
        sock = socket.socket()
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
        server = uvicorn.Server(uvicorn.Config(app, log_level="error"))
        thread = threading.Thread(target=server.run, kwargs={"sockets": [sock]}, daemon=True)
        thread.start()
        for _ in range(100):
            if server.started:
                break
            time.sleep(0.05)
        if not server.started:
            raise RuntimeError("Test server did not start")
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                context = browser.new_context(
                    viewport={"width": 1440, "height": 1100},
                    permissions=["clipboard-read", "clipboard-write"],
                )
                page = context.new_page()
                errors = []
                page.on("pageerror", lambda error: errors.append(str(error)))
                page.goto(f"http://127.0.0.1:{port}")
                expect(page.locator("#health")).to_contain_text("1 个")
                page.screenshot(path=str(artifacts / "desktop-home.png"), full_page=True)
                expect(page.locator("#query")).to_be_focused()
                page.locator("#query").fill("grep -r")
                page.locator("#query").press("Enter")
                page.locator("#response").wait_for(state="visible")
                assert page.locator("#answer").count() == 0
                expect(page.locator(".document h1")).to_have_text("递归搜索")
                assert page.locator(".document table").is_visible()
                assert page.locator(".document ul").is_visible()
                assert page.evaluate("window.untrusted === undefined")
                page.locator("details summary").click()
                assert not page.locator(".evidence-body").is_visible()
                page.locator("details summary").click()
                assert (
                    page.locator(".source-link").get_attribute("href") == "https://github.com/tldr-pages/tldr"
                )
                assert page.locator(".evidence-body").is_visible()
                page.locator(".copy").click()
                page.get_by_role("button", name="已复制", exact=True).wait_for()
                assert "grep -r test ." in page.evaluate("navigator.clipboard.readText()")
                page.screenshot(path=str(artifacts / "desktop-search.png"), full_page=True)
                page.set_viewport_size({"width": 390, "height": 844})
                assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
                page.screenshot(path=str(artifacts / "mobile-search.png"), full_page=True)
                page.locator("details summary").focus()
                page.keyboard.press("/")
                expect(page.locator("#query")).to_be_focused()
                page.locator("#query").fill("zzzznonexistent")
                page.locator("#query").press("Enter")
                expect(page.locator("#empty-results")).to_be_visible()
                assert page.locator("details").count() == 0
                page.route("**/api/search", lambda route: route.fulfill(status=503, body="unavailable"))
                page.locator("#submit").click()
                expect(page.locator("#notice")).to_contain_text("HTTP 503")
                assert not page.locator("#submit").is_disabled()
                assert not errors, errors
                browser.close()
                print(
                    "Browser checks passed: desktop/mobile, autofocus, Enter search, keyboard shortcut, Markdown, source links, empty results, copy, API error, no JS errors."
                )
        finally:
            server.should_exit = True
            thread.join(timeout=5)
            sock.close()


if __name__ == "__main__":
    main()
