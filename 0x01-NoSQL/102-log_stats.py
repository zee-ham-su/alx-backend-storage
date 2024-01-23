#!/usr/bin/env python3
"""  Python script that provides some stats about
Nginx logs stored in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of
documents in this collection
second line: Methods:
third line: <number> status check where <number> is
the count of documents with path "/status"
fourth line: IPs:
    <IP>: <count>
    ...
"""
import pymongo
from pymongo import MongoClient

Methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection):
    """
    Provide some stats about Nginx logs stored in MongoDB
    """
    total_logs = mongo_collection.count_documents({})

    method_counts = {}
    for method in Methods:
        method_counts[method] = mongo_collection.count_documents(
            {"method": method})

    status_check_count = mongo_collection.count_documents({"path": "/status"})

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(mongo_collection.aggregate(pipeline))

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")

    print(f"{status_check_count} status check")

    print("IPs:")
    for ip_info in top_ips:
        print(f"\t{ip_info['_id']}: {ip_info['count']}")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    log_stats(nginx_collection)
