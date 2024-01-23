#!/usr/bin/env python3
""" module to find by specific topic """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Find by specific topic
    """
    return mongo_collection.find({"topics": topic})
