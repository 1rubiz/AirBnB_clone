#!/usr/bin/python3


""" Base module """
import uuid
from datetime import datetime
# import the variable storage
import models


class BaseModel:
    """ class for all other classes to inherit from """
    def __init__(self, *args, **kwargs):
        """ Constructor and re-create an instance with
        this dictionary representation"""
        if len(kwargs) > 0:
	    for key, value in kwargs.items():
                if key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    # This happens because __class__ is not mandatory in output
                    continue

                setattr(self, key, value)
        else:
            # It generate a random UUID from uuid4
            self.id = str(uuid.uuid4())
            # assigns the current datetime when an instance is created
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ overriding the __str__ method that returns a custom
        string object """
        # Old-style: self.__class__.__name__
        mssg = "[{0}] ({1}) {2}".format(type(self).__name__, self.id, self.__dict__)
        return (mssg)

    # Public instance methods
    def save(self):
        """ updates the public instance attribute updated_at with
        the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance."""
        # Define a dictionary and key __class__ that add to this dictionary
        # with the class name of the object
        mydict = {}
        mydict["__class__"] = type(self).__name__
        # loop over dict items and the created_at and updated_at are
        # convert in ISO format
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                mydict[key] = value.isoformat()
            else:
                mydict[key] = value
        return (mydict)
