from pymongo import MongoClient

connection = open("../modules/loaders/mongo_cluster.txt", "r")
cluster = MongoClient(connection.read())
