#!/usr/bin/python3
"""Base model"""
import uuid
from datetime import datetime as dt


datetime_format = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """actual base Class"""

    def __init__(self, *args, **kwargs):
        """
        Construct anew instance of BaseModel

        Args:
            *args: Unused positional arguments
            **kwargs: Dictionary representation of an instance.

        If kwargs is not empty:
            Each key has an attribute name
            Each value is the value of the corresponding attr name
            Convert datetime to datetime objects
        """
        if kwargs:
            if 'created_at' in kwargs:
                kwargs['created_at'] = dt.strptime(
                    kwargs['created_at'], datetime_format
                )
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = dt.strptime(
                    kwargs['updated_at'], datetime_format
                )
            kwargs.pop('__class__', None)
            self.__dict__ = kwargs
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        """Return a string representation of the instance

        The format is [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updated the public instance attribute with current time"""
        from models import storage
        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """function to return a dictionary containing all

        keys/values of __dict__ of the instance
        """
        dictf = self.__dict__.copy()
        """identify the class name of the instance"""
        dictf["__class__"] = self.__class__.__name__
        dictf['created_at'] = self.created_at.isoformat()
        dictf['updated_at'] = self.updated_at.isoformat()
        return dictf
