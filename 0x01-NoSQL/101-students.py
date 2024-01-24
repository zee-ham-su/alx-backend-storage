#!/usr/bin/env python3
""" 101-students """


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    pipeline = [
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]

    students = list(mongo_collection.aggregate(pipeline))

    for student in students:
        student["_id"] = str(student["_id"])

    return students