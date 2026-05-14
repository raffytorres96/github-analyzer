from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class GithubUser:
    login: str
    public_repos: int
    followers: int
    html_url: str
    created_at: datetime
    name: Optional[str] = None
    location: Optional[str] = None
    bio: Optional[str] = None
    hireable: Optional[bool] = None
    email: Optional[str] = None

@dataclass
class GithubRepo:
    full_name: str
    owner: str
    html_url: str
    fork: bool
    forks: int
    size: int
    visibility: str
    created_at: datetime
    updated_at: datetime
    stargazers_count: int
    language: Optional[str] = None
    description: Optional[str] = None