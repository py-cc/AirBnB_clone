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
        dic = dict(self.__dict__)
        dic["updated_at"] = self.updated_at
        dic["id"] = self.id
        dic["created_at"] = self.created_at
        return "[" + BaseModel.__name__ + "] " + "(" + self.id + ") " +\
               str(dic)

    def save(self):
        """ save method """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ to dict method """
        dic = dict(self.__dict__)
        dic["__class__"] = self.__class__.__name__
        dic["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic["id"] = self.id
        dic["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return dic


if __name__ == '__main__':
    my_model = BaseModel()
    my_model.name = "Holberton"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))