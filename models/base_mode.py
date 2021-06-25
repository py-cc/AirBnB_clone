#!/usr/bin/python3
"""
Base Model - Module
"""
import uuid
import datetime


class BaseModel:
    """
    BaseModel - Class
    """
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __str__(self):
        """ String representation """
        return "[" + BaseModel.__name__ + "] " + "(" + self.id + ") " +\
               str(self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        return self.__dict__


if __name__ == '__main__':
    my_model = BaseModel()
    my_model.name = "Holberton"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
