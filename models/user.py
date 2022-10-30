#!/usr/bin/python3
"""
Module user.py with class User that inherits from BaseModel.
With public attributes: email, password, first_name, last_name.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines the class User that inherits from BaseModel.
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
