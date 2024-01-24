#!/usr/bin/env python3
""" a module for  Redis class and methods
"""
import uuid
import redis
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Enclose the adorned function within a wrapper
        and return the wrapper.
        """
        key = method.__qualname__
        self._redis.incr(key)
        result = method(self, *args, **kwargs)
        return result

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator designed to store the history of inputs
    and outputs for a function in Redis lists.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Enclose the adorned function within a wrapper
        and provide the wrapper as the result."""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        outcome = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", outcome)
        return outcome
    return wrapper


class Cache:
    """ cache class tht uses Redis for storing data
    """
    def __init__(self, host='localhost', port=6379, db=0):
        """ init methid to store an instance of
        the redis client
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the provided data in Redis using a randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)

    def get(self, key: str, fn: Callable = None) -> Union[str,
                                                          bytes, int, None]:
        """ Fetches information from Redis using the specified
        key and optionally employs a conversion function.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Union[str, bytes, None]:
        """ Fetches a string data from Redis using the given key
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """ Fetches integer data from Redis using the given key.
        """
        return self.get(key, fn=int)
