"""Application settings (simple). Extendable for env-based config."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Settings(BaseModel):
    app_name: str = Field(default="Codex Tasks API")
    debug: bool = Field(default=True)
    # SQLite for dev/tests; override to PostgreSQL in prod via DATABASE_URL env if needed
    database_url: str = Field(default="sqlite+aiosqlite:///./tasks.db")


settings = Settings()
