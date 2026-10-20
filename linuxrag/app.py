import sqlite3
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, field_validator

from .config import Settings
from .index import Index
from .rendering import render_markdown


class SearchRequest(BaseModel):
    top_k: int = Field(default=6, ge=1, le=20)
    query: str = Field(min_length=1, max_length=2000)

    @field_validator("query")
    @classmethod
    def nonblank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("请输入问题")
        return value.strip()


def create_app(settings: Settings | None = None, index: Index | None = None) -> FastAPI:
    settings = settings or Settings.load()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        try:
            app.state.index = index or Index(settings)
            app.state.index_error = None
        except (OSError, ValueError, KeyError, sqlite3.Error):
            app.state.index = None
            app.state.index_error = "索引无法读取，请重新建立索引并重启服务。"
        yield

    app = FastAPI(title="LinuxRag", version="0.1.0", lifespan=lifespan)
    static = Path(__file__).parent / "static"
    app.mount("/static", StaticFiles(directory=static), name="static")

    @app.middleware("http")
    async def security_headers(request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; "
            "connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'"
        )
        return response

    @app.get("/")
    def home():
        return FileResponse(static / "index.html")

    @app.get("/api/health")
    def health():
        current = app.state.index
        return {
            "status": "ok" if current and current.rows else "needs_index",
            "index_ready": bool(current and current.rows),
            "chunks": len(current.rows) if current else 0,
            "commands": len(current.cards) if current else 0,
            "vector_ready": bool(current and current.vector_ready),
            "error": app.state.index_error,
        }

    @app.post("/api/search")
    def search(request: SearchRequest):
        if app.state.index is None:
            return {"results": [], "mode": "unavailable", "warnings": [app.state.index_error]}
        result = app.state.index.search(request.query, request.top_k)
        result["results"] = [{**row, "html": render_markdown(row["text"])} for row in result["results"]]
        return result

    return app


app = create_app()
