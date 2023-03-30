from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
import os


url = URL.create(
    drivername="postgresql",
    username=os.environ.get("DBUSER"),
    password=os.environ.get("PASSWORD"),
    host=os.environ.get("DBHOST"),
    database=os.environ.get("DBNAME"),
    port=os.environ.get("DBPORT")
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Book(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)


Base.metadata.create_all(engine)