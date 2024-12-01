#!/usr/bin/python3
""" Class State (child class of BaseModel)"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State class inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
