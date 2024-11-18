#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """
    A base class for other models.
    Handles initialization, serialization, and deserialization of instances.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        - If `kwargs` is not empty, it uses the dictionary to set attributes.
        - Otherwise, it initializes default attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # Convert string datetime to datetime object
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns the string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance:
        - Adds a `__class__` key with the class name.
        - Converts `created_at` and `updated_at` to ISO format strings.
        """
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

