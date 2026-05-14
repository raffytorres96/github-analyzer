import requests
from github_analyzer.config import Config
from github_analyzer.models import GithubUser
from datetime import datetime

class GithubClient:

    @classmethod
    def get_user(cls, username: str):
        
        url = f"{Config.URL_BASE}/users/{username}"

        try:
            response = requests.get(url, headers=Config.get_headers(), timeout=Config.TIMEOUT)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Timeout raggiunto per l'utente {username}")
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Impossibile connettersi a GitHub")
        except requests.exceptions.HTTPError:
            raise Exception(f"Errore HTTP: {response.status_code}")
        

        data = response.json()
        utente = GithubUser(
            login=data["login"],
            public_repos=data["public_repos"],
            followers=data["followers"],
            html_url=str(data["html_url"]),
            created_at=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")),
            location=data["location"],
            name=data["name"],
            bio=data["bio"]
        )

        return utente