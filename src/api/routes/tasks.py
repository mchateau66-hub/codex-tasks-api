from __future__ import annotations

from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.deps import get_db
from src.models.task import Task
from src.schemas.task import TaskCreate, TaskOut, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])
DbDep = Annotated[AsyncSession, Depends(get_db)]


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
async def create_task(payload: TaskCreate, db: DbDep):
    task = Task(
        title=payload.title,
        description=payload.description,
        completed=payload.completed,
    )
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


@router.get("/", response_model=list[TaskOut])
async def list_tasks(
    db: DbDep,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    completed: Optional[bool] = Query(default=None),
):
    stmt = select(Task)
    if completed is not None:
        stmt = stmt.where(Task.completed.is_(completed))
    stmt = stmt.offset(skip).limit(limit)
    res = await db.execute(stmt)
    return list(res.scalars())


@router.get("/{task_id}", response_model=TaskOut)
async def get_task(task_id: Annotated[int, Path(ge=1)], db: DbDep):
    task = await db.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return task


@router.patch("/{task_id}", response_model=TaskOut)
async def update_task(
    task_id: Annotated[int, Path(ge=1)], payload: TaskUpdate, db: DbDep
):
    task = await db.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )

    if payload.title is not None:
        task.title = payload.title
    if payload.description is not None:
        task.description = payload.description
    if payload.completed is not None:
        task.completed = payload.completed

    await db.commit()
    await db.refresh(task)
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: Annotated[int, Path(ge=1)], db: DbDep):
    task = await db.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    await db.delete(task)
    await db.commit()
    return None
