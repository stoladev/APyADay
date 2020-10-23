from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://stoladev:123123abcabc@cluster0.1tg5d.mongodb.net/"
    "bug_tracker_db?retryWrites=true&w=majority"
)


def verify_user(username, password):
    db = cluster["bug_tracker_db"]
    collection = db["users"]

    accounts = collection.find({username: username})

    for x in accounts:
        print(x)
