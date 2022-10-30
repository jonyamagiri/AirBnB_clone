#!/usr/bin/python3
"""
Module review.py with class Review that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the attributes of a Review submitted.
    Public attributes:
        place_id (str): Place id
        user_id (str): User id
        text (str): text of the review submitted
    """
    place_id = ""
    user_id = ""
    text = ""
