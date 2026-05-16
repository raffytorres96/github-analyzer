from github_analyzer.client import GithubClient
from github_analyzer.analyzer import RepoAnalyzer
from github_analyzer.database.database import get_engine, init_db, get_session
from github_analyzer.database.repository import save_user, save_repos

if __name__ == "__main__":

    motore = get_engine()
    init_db(motore)
    sessione = get_session(motore)

    utente = GithubClient.get_user("raffytorres96")
    print(utente)
    save_user(sessione, utente)

    repos = GithubClient.get_repos("raffytorres96")
    print(repos)
    save_repos(sessione, repos)
    
    print(RepoAnalyzer.get_stats(repos))