#!/usr/bin/env python3
""" module for  Implementing an expiring web cache and tracker
"""
import requests
import redis
from functools import wraps, lru_cache

store = redis.Redis()


def count_url_access(method):
    """ Decorator counting how many times a URL is accessed """
    @wraps(method)
    def wrapper(url):
        count_key = "count:" + url
        store.incr(count_key)
        return method(url)
    return wrapper


@lru_cache(maxsize=None)
@count_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    res = requests.get(url)
    return res.text