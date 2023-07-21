#!/usr/bin/env python3
"""list top students"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    pipeline = [
        {
            '$unwind': '$topics'
        },
        {
            '$group': {
                '_id': '$_id',
                'name': {'$first': '$name'},
                'averageScore': {'$avg': '$topics.score'},
            }
        },
        {
            '$sort': {'averageScore': -1}
        },
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': 1,
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
