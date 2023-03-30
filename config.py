from typing import Dict
from os import environ

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY =  environ.get("SECRET_KEY")
    PORT = environ.get("PORT")
    DBHOST=environ.get("DBHOST")
    DBPORT=environ.get("DBPORT")
    DBNAME=environ.get("DBNAME")
    SECRETKEY=environ.get("SECRETKEY")

class Production(BaseConfig):
    DEBUG = False
   


class Developement(BaseConfig):
    pass