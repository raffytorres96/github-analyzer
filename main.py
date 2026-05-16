from github_analyzer.client import GithubClient
from github_analyzer.analyzer import RepoAnalyzer
from github_analyzer.database.database import get_engine, init_db

if __name__ == "__main__":

    init_db(get_engine())
    print(GithubClient.get_user("raffytorres96"))
    repos = GithubClient.get_repos("raffytorres96")
    print(repos)
    print(RepoAnalyzer.get_stats(repos))