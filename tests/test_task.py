import pytest
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

from src.main import app


@pytest.mark.asyncio
async def test_health():
    async with LifespanManager(app):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            r = await ac.get("/health")
            assert r.status_code == 200
            assert r.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_crud_tasks_flow():
    async with LifespanManager(app):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            # Create
            payload = {
                "title": "Write tests",
                "description": "Add pytest suite",
                "completed": False,
            }
            r = await ac.post("/tasks/", json=payload)
            assert r.status_code == 201
            tid = r.json()["id"]

            # Read one
            r = await ac.get(f"/tasks/{tid}")
            assert r.status_code == 200
            assert r.json()["id"] == tid

            # List
            r = await ac.get("/tasks/")
            assert r.status_code == 200
            assert any(t["id"] == tid for t in r.json())

            # Filter
            r = await ac.get("/tasks/?completed=false")
            assert r.status_code == 200
            assert all(not t["completed"] for t in r.json())

            # Update
            r = await ac.patch(f"/tasks/{tid}", json={"completed": True})
            assert r.status_code == 200
            assert r.json()["completed"] is True

            # Delete
            r = await ac.delete(f"/tasks/{tid}")
            assert r.status_code == 204

            # Not found
            r = await ac.get(f"/tasks/{tid}")
            assert r.status_code == 404
