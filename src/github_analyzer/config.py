from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    URL_BASE = "https://api.github.com"
    TIMEOUT = int(os.getenv("TIMEOUT", 10))

    @classmethod
    def get_headers(cls):
        a = {}

        a["X-GitHub-Api-Version"] = "2022-11-28"
        a["Accept"] = "application/vnd.github+json"

        if cls.GITHUB_TOKEN is not None:
            a["Authorization"] = f"Bearer {cls.GITHUB_TOKEN}"
        
        return a