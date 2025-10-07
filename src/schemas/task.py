from __future__ import annotations

from typing import Optional  # 👈 ajouté

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=2000)  # 👈


class TaskCreate(TaskBase):
    completed: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)  # 👈
    description: Optional[str] = Field(default=None, max_length=2000)  # 👈
    completed: Optional[bool] = None  # 👈


class TaskOut(TaskBase):
    id: int
    completed: bool
    model_config = {"from_attributes": True}
