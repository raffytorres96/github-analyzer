from github_analyzer.client import GithubClient
from github_analyzer.analyzer import RepoAnalyzer


if __name__ == "__main__":

    print(GithubClient.get_user("raffytorres96"))
    repos = GithubClient.get_repos("raffytorres96")
    print(repos)
    print(RepoAnalyzer.get_stats(repos))