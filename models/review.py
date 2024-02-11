#!/usr/bin/python3
"""Defines the review class"""
from models.base_models import BaseModel

class Review(BaseModel):
    """represents a review 
    Attributes:
    place_id (str): the place id.
    user_id (str): the user id.
    text (str): The text of the review."""

    place_id = ""
    user_id = ""
    text = ""
