#!/usr/bin/python3
"""create an instance of the FileStorage module"""

from models.engine.file_storage import FileStorage

# create a unique instance
storage = FileStorage()
# load stored data from JSON file
storage.reload()
