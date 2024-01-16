#!/usr/bin/python3
'''BaseModel class file'''
from datetime import datetime
import uuid
import models


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize the instance with unique id and current datetime."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
            self.id = kwargs['id']
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary containing all keys/values of __dict__ of the instance."""
        new_dict = self.__dict__.copy()
        new_dict['id'] = self.id
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['__class__'] = type(self).__name__
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
