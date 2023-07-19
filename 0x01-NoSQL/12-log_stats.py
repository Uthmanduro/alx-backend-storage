#!/usr/bin/env python3
"""scripts that logs stats"""
from pymongo import MongoClient


def getlogs():
    """gets the logs of items in the database"""
    client = MongoClient()
    db = client["logs"]
    collection = db.nginx
    logs = collection.count_documents({})
    get = collection.count_documents({"method": "GET"})
    post = collection.count_documents({"method": "POST"})
    put = collection.count_documents({"method": "PUT"})
    patch = collection.count_documents({"method": "PATCH"})
    delete = collection.count_documents({"method": "DELETE"})
    path = collection.count_documents({"path": "/status"})
    print("""{} logs\nMethods:
    method GET: {}\t
    method POST: {}\t
    method PUT: {}\t
    method PATCH: {}\t
    method DELETE: {}\n{} status check""".format(logs, get, post,\
            put, patch, delete, path))


if __name__ == "__main__":
    getlogs()



"""{logs} logs\nMethods:\t
    method GET: {get}\t
    method POST: {post}\t
    method PUT: {put}\t
    method PATCH: {patch}\t
    method DELETE: {delete}\n{path} status check
"""
