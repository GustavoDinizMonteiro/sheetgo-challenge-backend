import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def get_uri():
    if os.getenv('ENV') == 'dev':
        return os.getenv('TEST_DB_URI')
    return os.getenv('DB_URI')


engine = create_engine(get_uri())
Session = sessionmaker(engine)
Model = declarative_base()
