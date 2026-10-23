from markdown_it import MarkdownIt

# Treat source HTML as text; never execute markup supplied by documents.
markdown = MarkdownIt("commonmark", {"html": False, "linkify": False}).enable(["table", "strikethrough"])


def render_markdown(text: str) -> str:
    return markdown.render(text)
