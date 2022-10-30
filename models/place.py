#!/usr/bin/python3
"""
Module place.py with class Place that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines the attributes of a particular Place.
    Public attributes:
        city_id (str): City id
        user_id (str): User id
        name (str): name of the place
        description (str): description of the place
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum number of guests allowed
        price_by_night (int): price by night
        latitude (float): latitude
        longitude (float): longitude
        amenity_ids (list): amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_bathrooms = 0
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
