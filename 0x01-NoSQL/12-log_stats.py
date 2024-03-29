#!/usr/bin/env python3
"""  Python script that provides some stats about
Nginx logs stored in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of
documents in this collection
second line: Methods:
"""
import pymongo
from pymongo import MongoClient

Methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Provide some stats about Nginx logs stored in MongoDB
    """
    collections = {}
    if option:
        log_total = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {log_total}")
        return

    output = mongo_collection.count_documents(collections)
    print(f"{output} logs")
    print("Methods:")
    for method in Methods:
        log_stats(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
