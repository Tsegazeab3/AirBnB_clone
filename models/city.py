#!/usr/bin/python3
"""module of user class"""

from models.base_model import BaseModel


class City(BaseModel):
    """city object"""

    state_id = ""
    name = ""
