from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, Boolean
from typing import Optional
from datetime import datetime

class Base(DeclarativeBase):
    pass

class UserRecord(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(100), unique=True)
    public_repos: Mapped[int] = mapped_column(Integer)
    followers: Mapped[int] = mapped_column(Integer)
    html_url: Mapped[str] = mapped_column(String(200))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    location: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    bio: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    hireable: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)


class RepoRecord(Base):
    __tablename__ = "repos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(100))
    owner: Mapped[str] = mapped_column(String(100))
    html_url: Mapped[str] = mapped_column(String(300))
    fork: Mapped[bool] = mapped_column(Boolean)
    forks: Mapped[int] = mapped_column(Integer)
    size: Mapped[int] = mapped_column(Integer)
    visibility: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    stargazers_count: Mapped[int] = mapped_column(Integer)
    language: Mapped[Optional[str]] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(500))