#!/usr/bin/python3
"""
Module city.py with class City that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines the attributes of a particular City.
    Public attributes:
        state_id (str): state id
        name (str): name of the city
    """
    state_id = ""
    name = ""
