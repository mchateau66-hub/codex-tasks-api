# src/main.py — Application principale FastAPI

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.api.routes.tasks import router as tasks_router
from src.db.session import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestionnaire de cycle de vie (remplace on_event)."""
    # --- Startup ---
    await init_db()
    yield
    # --- Shutdown ---
    # (si besoin: fermeture de connexions, nettoyage, etc.)


app = FastAPI(
    title="Codex Tasks API",
    version="1.0.0",
    default_response_class=ORJSONResponse,
    contact={"name": "Team Codex"},
    license_info={"name": "MIT"},
    lifespan=lifespan,
)


@app.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    """Vérifie l'état de santé de l'API."""
    return {"status": "ok"}


@app.get("/", tags=["root"])
async def root() -> dict[str, str]:
    """Route racine simple."""
    return {"message": "🚀 Codex Tasks API is running perfectly!"}


# Inclusion du router des tâches
app.include_router(tasks_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
