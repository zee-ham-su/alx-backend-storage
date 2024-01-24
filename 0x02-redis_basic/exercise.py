#!/usr/bin/env python3
""" a module for  Redis class and methods
"""
import uuid
import redis
from typing import Union


class Cache:
    """ cache class tht uses Redis for storing data
    """
    def __init__(self, host='localhost', port=6379, db=0):
        """ init methid to store an instance of
        the redis client
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the provided data in Redis using a randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)
