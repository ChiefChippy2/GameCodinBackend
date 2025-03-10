import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
load_dotenv('./env/.env')


class Database(object):
    @classmethod
    def get_database(cls):

        CONNECTION_STRING = os.environ['DATABASE_CONNECTION_STRING']
        client = MongoClient(CONNECTION_STRING, server_api=ServerApi('1'))
        return client['GameCodin']
