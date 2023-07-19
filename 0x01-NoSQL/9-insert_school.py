#!/usr/bin/env python3
"""insert a document in python"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection"""
    new_id = mongo_collection.insert_one(kwargs).inserted_id
    return new_id
