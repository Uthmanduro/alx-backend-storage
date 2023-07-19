#!/usr/bin/env python3
"""lists all documents in python"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """lists all documents in a collection"""
    schools = mongo_collection.find()
    if schools is None:
        return []
    return schools
