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