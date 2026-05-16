from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from github_analyzer.database.models import Base

def get_engine():
    engine = create_engine("sqlite:///data/database.db")

    return engine

def get_session(engine):

    Session1 = sessionmaker(bind=engine)
    session = Session1()

    return session

def init_db(engine):

    Base.metadata.create_all(engine)