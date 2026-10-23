import argparse
import json
import subprocess
from pathlib import Path

from .config import Settings
from .corpus import read_corpus
from .evaluate import evaluate
from .index import Index, build_index
from .provider import ProviderError


def main():
    parser = argparse.ArgumentParser(description="Linux command RAG")
    sub = parser.add_subparsers(dest="action", required=True)
    validate = sub.add_parser("validate", help="Validate curated Markdown without calling a model")
    validate.add_argument("--knowledge", type=Path, default=Path("knowledge"))
    build = sub.add_parser("build", help="Build an atomic index from reviewed knowledge")
    build.add_argument("--knowledge", type=Path, default=Path("knowledge"))
    build.add_argument("--lexical-only", action="store_true")
    serve = sub.add_parser("serve")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", default=8000, type=int)
    evaluation = sub.add_parser("evaluate")
    evaluation.add_argument("--cases", type=Path, default=Path("eval/cases.json"))
    evaluation.add_argument("--output", type=Path, default=Path("data/evaluation.json"))
    args = parser.parse_args()
    settings = Settings.load()
    try:
        if args.action in {"validate", "build"}:
            chunks, sources = read_corpus(args.knowledge)
            if args.action == "validate":
                result = {
                    "commands": len({c.command for c in chunks}),
                    "chunks": len(chunks),
                    "embedding_called": False,
                    "review": "knowledge/REVIEW.md",
                }
            else:
                result = build_index(
                    settings, chunks, sources, lexical_only=args.lexical_only, knowledge_dir=args.knowledge
                )
            print(json.dumps(result, ensure_ascii=False, indent=2))
        elif args.action == "serve":
            import uvicorn

            uvicorn.run("linrag.app:app", host=args.host, port=args.port)
        else:
            index = Index(settings)
            if not index.rows:
                raise ValueError("请先建立索引再运行评测。")
            report = evaluate(index, args.cases)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
            print(
                json.dumps(
                    {
                        mode: {k: v for k, v in result.items() if k != "details"}
                        for mode, result in report["modes"].items()
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
    except (OSError, ValueError, ProviderError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"操作失败：{exc}\n")


if __name__ == "__main__":
    main()
