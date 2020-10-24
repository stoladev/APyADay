from pymongo import MongoClient

connection = open("../modules/mongo_cluster.txt", "r")
cluster = MongoClient(connection.read())

# def verify_user(username, password):
#     for x in accounts:
#         print(x)
