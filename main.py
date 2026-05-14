from src.github_analyzer.client import GithubClient


if __name__ == "__main__":

    print(GithubClient.get_user("raffytorres96"))
    print(GithubClient.get_repos("raffytorres96"))