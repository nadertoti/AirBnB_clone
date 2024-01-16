#!/usr/bin/python3
'''FileStorage class super file'''
from models.base_model import BaseModel
import json
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    '''class for file storage.'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''objects for dictionary that will be using.'''
        return self.__objects

    def new(self, obj):
        '''attribute instance new'''
        new_value = obj.__class__.__name__ + "." + obj.id
        self.__objects[new_value] = obj

    def save(self):
        '''saves to json file'''
        save_value = {}
        for key, value in self.__objects.items():
            save_value[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(save_value, f)

    def reload(self):
        '''loads from json file without errors'''
        try:
            with open(self.__file_path) as f:
                dict_value = json.load(f)

            for keys in dict_value.keys():
                self.__objects[keys] = BaseModel(**dict_value[keys])
        except FileNotFoundError:
            pass
