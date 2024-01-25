#!/usr/bin/env python3
""" module for  Implementing an expiring web cache and tracker
"""
import requests
import redis
from functools import wraps, lru_cache
from time import time

store = redis.Redis()


def count_url_access(method):
    """ Decorator counting how many times a URL is accessed """
    @wraps(method)
    def wrapper(url):
        count_key = "count:" + url
        store.incr(count_key)
        return method(url)
    return wrapper


def timed_lru_cache(maxsize, timeout):
    """ LRU Cache decorator with timeout """
    def decorator(method):
        cached_method = lru_cache(maxsize)(method)

        @wraps(method)
        def wrapper(url):
            cache_key = (url,)
            result = cached_method(url)
            store.setex(cache_key, timeout, result)
            return result

        return wrapper

    return decorator


@count_url_access
@timed_lru_cache(maxsize=None, timeout=10)
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    res = requests.get(url)
    return res.text
