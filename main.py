#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

# Initialize the storage system (FileStorage in this case)
storage = FileStorage()

# Create a new BaseModel instance
my_model = BaseModel()

# Save the model using the storage system
my_model.save(storage)

# Access stored objects
print(storage.all())  # Prints all saved objects

