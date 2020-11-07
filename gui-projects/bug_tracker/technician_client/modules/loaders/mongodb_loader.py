"""
Loads the mongodb login information to connect to the necessary cluster.
"""

from pymongo import MongoClient

connection = open("../modules/loaders/mongo_cluster.txt", "r")
cluster = MongoClient(connection.read())
