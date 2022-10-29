#!/usr/bin/python3
"""
Module base_model.py defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes
    Methods:
        def __init__(self, *args, **kwargs)
        def __str__(self)
        def save(self)
        def to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """Initializes the class
        Args:
            *args (any): not used
            **kwargs (dictionary): key-value pairs of attributes
        """
        dt_format = "%Y-%m-%dT%H:%M:%S.%f"  # (ex:2017-06-14T22:31:03.285259)
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, dt_format)
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Prints instance as: [<class name>] (<self.id>) <self.__dict__>"""
        objs = '[{}] ({}) {}'
        return objs.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        temp_dict = self.__dict__.copy()
        temp_dict["created_at"] = self.created_at.isoformat()
        temp_dict["updated_at"] = self.updated_at.isoformat()
        temp_dict["__class__"] = self.__class__.__name__
        return temp_dict
