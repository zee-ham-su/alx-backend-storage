#!/usr/bin/env python3
""" module that inserts a new doc in
collection based on kwargs """

import pymongo


def insert_school(mongo_collection, **kwargs):
    """ insert new doc in collection """
    return mongo_collection.insert_one(kwargs).inserted_id
