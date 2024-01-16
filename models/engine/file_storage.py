#!/usr/bin/python3
'''FileStorage class file'''
from models.base_model import BaseModel
import json
import models


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects (only if the JSON file (__file_path) exists)."""
        try:
            with open(self.__file_path) as f:
                new_dict = json.load(f)

            for keys in new_dict.keys():
                self.__objects[keys] = BaseModel(**dic[keys])
        except FileNotFoundError:
            pass
