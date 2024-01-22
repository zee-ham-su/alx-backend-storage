#!/usr/bin/env python3
""" 10-change school topics"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """ many rows update """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
