import requests
from github_analyzer.config import Config
from github_analyzer.models import GithubUser
from github_analyzer.models import GithubRepo
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
    
    @classmethod
    def get_repos(cls, username: str):

        url = f"{Config.URL_BASE}/users/{username}/repos"

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
        repos = []
        for repo in data:
            repo = GithubRepo(
                full_name= repo["full_name"],
                owner= repo["owner"]["login"],
                html_url= repo["html_url"],
                fork= repo["fork"],
                forks= repo["forks"],
                size= repo["size"],
                visibility= repo["visibility"],
                created_at=datetime.fromisoformat(repo["created_at"].replace("Z", "+00:00")),
                updated_at=datetime.fromisoformat(repo["updated_at"].replace("Z", "+00:00")),
                stargazers_count= repo["stargazers_count"]
            )
            repos.append(repo)

        return repos