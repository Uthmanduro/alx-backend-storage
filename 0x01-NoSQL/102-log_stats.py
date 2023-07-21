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
    print("IPs:")
    ips = list(collection.aggregate([
        {'$group': {'_id': "$ip", 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}]))
    for ip in ips:
        print("\t{}: {}".format(ip['_id'], ip['count']))


if __name__ == "__main__":
    getlogs()
