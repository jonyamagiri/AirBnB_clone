#!/usr/bin/python3
"""
Module file_storage.py that serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json


class FileStorage:
    """Defines the FileStorage class that serializes instances to a JSON file
     and deserializes JSON file to instances
    Attributes:
        __file_path (str): path to the JSON file (ex: file.json)
        __objects (dictionary) : stores all objects by <class name>.id
    Methods:
         def all(self)
         def new(self, obj)
         def save(self)
         def reload(self)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        self.__objects["{}.{}".format(obj_cls_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode="w") as fdump:
            temp_dict = {}
            temp_dict.update(self.__objects)
            for key, value in temp_dict.items():
                temp_dict[key] = value.to_dict()
            json.dump(temp_dict, fdump)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
         (__file_path) exists; otherwise, do nothing.
        """
        # defer the import of BaseModel to only when it is needed to prevent
        # circular imports error
        
        from models.base_model import BaseModel
        try:
            with open(self.__file_path) as fload:
                obj_dict = json.load(fload)
                for item in obj_dict.values():
                        cls_name = item["__class__"]
                        del item["__class__"]
                        self.new(eval(cls_name)(**item))
        except FileNotFoundError:
            return
