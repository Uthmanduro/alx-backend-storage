#!/usr/bin/env python3
"""writing to strings"""
import uuid
import redis
from typing import Union, Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs for a particular function"""
    key = method.__qualname__
    inputs, outputs = key + ':inputs', key + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


def count_calls(method: Callable) -> Callable:
    """a generator function that count how many times the class is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function that performs the operation"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """creates the cache class"""
    def __init__(self):
        """initialize the redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """returns a string"""
        random_id = str(uuid.uuid4())
        self._redis.mset({random_id: data})
        return random_id

    def get(self, key: str, fn: Optional[Callable] = None) -> str:
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
