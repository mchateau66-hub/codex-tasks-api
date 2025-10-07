from __future__ import annotations

from typing import Optional  # 👈 ajouté

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), index=True)
    description: Mapped[Optional[str]] = mapped_column(String(2000), default=None)  # 👈
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
