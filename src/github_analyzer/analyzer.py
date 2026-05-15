from collections import Counter

class RepoAnalyzer:

    @classmethod
    def get_stats(cls, repos: list):

        statistiche = {}

        stelle = sum(repo.stargazers_count for repo in repos)

        linguaggi = [repo.language for repo in repos]
        contatore1 = Counter(linguaggi)

        recent_repo = max(repos, key=lambda repo: repo.updated_at)

        fork = [repo for repo in repos if repo.fork]
        original = [repo for repo in repos if not repo.fork]


        statistiche.update({
            "Linguaggio più diffuso": contatore1.most_common(1),
            "Numero stelle": stelle,
            "Repo più recente": recent_repo,
            "Numero repos originali": len(original),
            "Numero repos forks": len(fork)
            })
        
        return statistiche