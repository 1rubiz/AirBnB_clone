#!/usr/bin/python3
"""Review class for AirBnB"""
from . base_model import BaseModel

class Review(BaseModel):
    """Review class that inherits from basemodel"""
    place_id = ""
    user_id = ""
    text = ""
