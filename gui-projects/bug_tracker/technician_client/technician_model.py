import pymongo


class Model:
    def __init__(self):
        self.database = self.connect_to_database()

    @staticmethod
    def connect_to_database():
        # MongoDB Connection
        mongodb_url = open("../mongo_cluster.txt", "r")
        connection = mongodb_url.read()
        cluster = pymongo.MongoClient(connection)
        return cluster
