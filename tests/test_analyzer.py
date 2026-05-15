from datetime import datetime, timezone
from github_analyzer.models import GithubRepo
from github_analyzer.analyzer import RepoAnalyzer


def test_get_stats():
    #Arrange
    repo_finto1 = GithubRepo(
        full_name="raffytorres96/github",
        owner="Raffaele Gatta",
        html_url="https://github.com/utente/progetto1",
        fork=False,
        forks=0,
        size=150,
        visibility="public",
        created_at=datetime(2020, 1, 24, tzinfo=timezone.utc),
        updated_at=datetime(2024, 6, 1, tzinfo=timezone.utc),
        stargazers_count=5,
        language="Python"
    )
    repo_finto2 = GithubRepo(
        full_name="vibedrop/vibedropit",
        owner="VibeDrop",
        html_url="https://github.com/utente/progetto2",
        fork=False,
        forks=0,
        size=100,
        visibility="public",
        created_at=datetime(2024, 1, 1, tzinfo=timezone.utc),
        updated_at=datetime(2025, 6, 1, tzinfo=timezone.utc),
        stargazers_count=12,
        language="C++"
    )
    repo_finto3 = GithubRepo(
        full_name="bellini_4/codacons",
        owner="Marco Bellini",
        html_url="https://github.com/utente/progetto3",
        fork=True,
        forks=0,
        size=300,
        visibility="private",
        created_at=datetime(2018, 1, 1, tzinfo=timezone.utc),
        updated_at=datetime(2022, 6, 1, tzinfo=timezone.utc),
        stargazers_count=8,
        language="Java"
    )
    repo_finto4 = GithubRepo(
        full_name="sando89/the_jungle",
        owner="Sandokan",
        html_url="https://github.com/utente/progetto4",
        fork=False,
        forks=0,
        size=100,
        visibility="private",
        created_at=datetime(2003, 1, 1, tzinfo=timezone.utc),
        updated_at=datetime(2023, 6, 1, tzinfo=timezone.utc),
        stargazers_count=5,
        language="Python"
    )

    #Act
    lista = []
    lista.append(repo_finto1)
    lista.append(repo_finto2)
    lista.append(repo_finto3)
    lista.append(repo_finto4)
    risultato = RepoAnalyzer.get_stats(lista)

    #Assert
    assert risultato["Numero stelle"] == 30
    assert risultato["Numero repos originali"] == 3
    assert risultato["Numero repos forks"] == 1
    assert risultato["Repo più recente"] == repo_finto2