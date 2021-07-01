#!/usr/bin/python3
"""
file storage - Module
"""
import json
from models.base_model import BaseModel
form models.user import User


class FileStorage:
    """
    FileStorage - Class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all - method """
        return self.__objects

    def new(self, obj):
        """ new - method """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ save - method """
        for key, value in self.__objects.items():
            if not isinstance(value, dict):
                self.__objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """ reload - method """
        try:
            with open(self.__file_path, 'r') as file:
                j_file = json.load(file)
            for key, value in j_file.items():
                self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
