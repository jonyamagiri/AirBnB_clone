#!/usr/bin/python3
"""
Module user.py with class User that inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines the attributes of a particular User.
    Public attributes:
        email (str): user email
        password (str): user password
        first_name (str): user's first name
        last_name (str): user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
