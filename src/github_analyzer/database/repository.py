from github_analyzer.models import GithubUser, GithubRepo
from github_analyzer.database.models import UserRecord, RepoRecord

def save_user(session, user: GithubUser) -> UserRecord:

    existing = session.query(UserRecord).filter_by(login=user.login).first()

    if existing:
        existing.public_repos = user.public_repos
        existing.followers = user.followers
        existing.html_url = user.html_url
        existing.created_at = user.created_at
        existing.name = user.name
        existing.location = user.location
        existing.bio = user.bio
        existing.hireable = user.hireable
        existing.email = user.email

        record = existing
    else:
        record = UserRecord(
        login=user.login,
        public_repos=user.public_repos,
        followers=user.followers,
        html_url=user.html_url,
        created_at=user.created_at,
        name=user.name,
        location=user.location,
        bio=user.bio,
        hireable=user.hireable,
        email=user.email
    )
        session.add(record)

    session.commit()

    return record

def save_repos(session, repos: list):
    for repo in repos:
        existing = session.query(RepoRecord).filter_by(full_name=repo.full_name).first()

        if existing:
            existing.owner = repo.owner
            existing.html_url = repo.html_url
            existing.fork = repo.fork
            existing.forks = repo.forks
            existing.size = repo.size
            existing.visibility = repo.visibility
            existing.created_at = repo.created_at
            existing.updated_at = repo.updated_at
            existing.stargazers_count = repo.stargazers_count
            existing.language = repo.language
            existing.description = repo.description

            record = existing

        else:
            record = RepoRecord(
                full_name=repo.full_name,
                owner=repo.owner,
                html_url=repo.html_url,
                fork=repo.fork,
                forks=repo.forks,
                size=repo.size,
                visibility=repo.visibility,
                created_at=repo.created_at,
                updated_at=repo.updated_at,
                stargazers_count=repo.stargazers_count,
                language=repo.language,
                description=repo.description
            )
            session.add(record)
        
    session.commit()