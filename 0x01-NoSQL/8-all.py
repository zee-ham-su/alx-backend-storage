#!/usr/bin/env python3
""" module that inserts a document in the collection school """

import pymongo


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
