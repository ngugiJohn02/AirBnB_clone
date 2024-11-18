#!/usr/bin/python3
from models.base_model import BaseModel

# Create an instance of BaseModel
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)

# Save the instance (updates `updated_at`)
my_model.save()
print(my_model)

# Convert instance to dictionary
my_model_json = my_model.to_dict()
print(my_model_json)

# Print keys and values in dictionary
print("JSON of my_model:")
for key, value in my_model_json.items():
    print(f"\t{key}: ({type(value)}) - {value}")

