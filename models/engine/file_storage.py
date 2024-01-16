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
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects (only if the JSON file (__file_path) exists)."""
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                class_name, obj_id = key.split('.')
                obj_dict = {}
                for k, v in value.items():
                    if k == 'created_at' or k == 'updated_at':
                        obj_dict[k] = datetime.strptime(
                            v, '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        obj_dict[k] = v
                obj = eval(class_name)(**obj_dict)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
