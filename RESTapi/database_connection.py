import pymongo
from config import MONGODB_CONNECTION_STRING


def connect(database: str):
    """
    Function who creates a connection to a mongo database
    :param database: a string with name of the database
    :return: a cluster object or None if connection is unsuccessful
    """
    try:
        cluster = pymongo.MongoClient(MONGODB_CONNECTION_STRING)

        _database = cluster[database]
    except Exception as error:
        _database = None
        print(error.__str__())

    return _database

