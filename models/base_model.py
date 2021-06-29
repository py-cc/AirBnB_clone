#!/usr/bin/python3
"""
Base Model - Module
"""
import uuid
import datetime

import models


class BaseModel:
    """
    BaseModel - Class
    """
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __init__(self, *args, **kwargs):
        """ Class constructor """
        if bool(kwargs) is True:
            for key in kwargs.keys():
                if key == "created_at" or key == "updated_at":
                    datetime_obj = datetime.datetime.strptime(
                        kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, datetime_obj)
                elif key != "__class__":
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            """ self.updated_at = datetime.datetime.now() """
            models.storage.new(self)

    def __str__(self):
        """ String representation """
        dic = dict(self.__dict__)
        dic["updated_at"] = self.updated_at
        dic["id"] = self.id
        dic["created_at"] = self.created_at
        return "[" + BaseModel.__name__ + "] " + "(" + self.id + ") " +\
            str(dic)

    def save(self):
        """ save method """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to dict method """
        dic = dict(self.__dict__)
        dic["__class__"] = self.__class__.__name__
        dic["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic["id"] = self.id
        dic["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return dic
