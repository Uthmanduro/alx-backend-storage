#!/usr/bin/env python3
"""writing to strings"""
import uuid
import redis
from typing import Union, Callable, Optional


class Cache:
    """creates the cache class"""
    def __init__(self):
        """initialize the redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """returns a string"""
        random_id = str(uuid.uuid4())
        self._redis.set(random_id, data)
        return random_id

    def get(self, key: str, fn: Optional[Callable]) -> str:
        """converts data back tp desired format"""
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        else:
            return data

    def get_str(self, data: str) -> str:
        """returns a str representation of the data"""
        return data.decode('utf-8', 'strict')

    def get_int(self, data: str) -> str:
        """returns an int representation of the data"""
        return int(data)
