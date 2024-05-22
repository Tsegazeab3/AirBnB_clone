#!/usr/bin/python3
"""module of Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """manages review objects"""

    place_id = ""
    user_id = ""
    text = ""
