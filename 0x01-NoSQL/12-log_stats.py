#!/usr/bin/env python3
"""scripts that logs stats"""
from pymongo import MongoClient


def getlogs():
    """gets the logs of items in the database"""
    client = MongoClient()
    db = client["logs"]
    collection = db.nginx
    logs = collection.count_documents({})
    print("{} logs".format(logs))
    method_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in method_list:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    path = collection.count_documents({"path": "/status"})
    print("{} status check".format(path))


if __name__ == "__main__":
    getlogs()
