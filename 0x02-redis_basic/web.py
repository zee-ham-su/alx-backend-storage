#!/usr/bin/env python3
""" module for  Implementing an expiring web cache and tracker
"""
import requests
import redis
from functools import wraps

store = redis.Redis()


def count_url_access(method):
    """Decorator that keeps track of the number of
    times a URL is accessed."""
    @wraps(method)
    def wrapper(url):
        cache_key = "cache:" + url
        cached_content = store.get(cache_key)

        if cached_content:
            return cached_content.decode("utf-8")

        access_count_key = "access_count:" + url
        store.incr(access_count_key)  # Increment access count

        html_content = method(url)

        store.set(cache_key, html_content)
        store.expire(cache_key, 10)  # Set cache expiration time
        return html_content

    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """Fetches the HTML content of a given URL."""
    response = requests.get(url)
    return response.text
