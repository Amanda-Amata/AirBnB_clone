#!/usr/bin/python3
""" Defines the BaseModel class. """
import models
from uuid import uuid4
from datetime import datetime

class BaseModels:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialises a new BaseModel

        Args:
        *args (any): unused.
        **kwargs (dict): key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self_id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def to_dict(self):
        """Returns the dictionary of the BaseModel instance.
        includes the key/value pair __class__representing the class name ofthe object"""

        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """returns the print/str representation of the BaseModel instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) ()".format(clname, self.id, self.__dict__)
