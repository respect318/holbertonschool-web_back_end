#!/usr/bin/env python3
def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the given MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The document fields to insert.

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
