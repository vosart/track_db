from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("postgresql://gvcsomvr:0BUcGunEZWVJ2XJcYBviZDW2DpJkzpCs@hattie.db.elephantsql.com/gvcsomvr")
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

