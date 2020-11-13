"""
Loads the mongodb login information for technicians to connect to the necessary cluster.
"""

from pymongo import MongoClient

connection = open("../../../mongo_cluster.txt", "r")
cluster = MongoClient(connection.read())
