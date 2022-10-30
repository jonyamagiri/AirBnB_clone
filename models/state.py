#!/usr/bin/python3
"""
Module state.py with class State that inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Defines the attributes of a particular State.
    Public attributes:
        name (str): name of the state
    """
    name = ""
