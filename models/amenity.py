#!/usr/bin/python3
"""
Module amenity.py with class Amenity that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines the amenities offered by a User.
    Public attributes:
        name (str): name of the amenity
    """
    name = ""
