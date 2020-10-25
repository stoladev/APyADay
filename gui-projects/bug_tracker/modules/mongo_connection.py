from pymongo import MongoClient

connection = open("../modules/mongo_cluster.txt", "r")
cluster = MongoClient(connection.read())
