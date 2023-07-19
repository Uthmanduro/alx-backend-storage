#!/usr/bin/env python3
"""change school topics"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    result = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
