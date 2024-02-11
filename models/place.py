#!/usr/bin/python3
""" Defines the place class"""
from models.base_model import BaseModel

class Place(BaseModel):
    """Represent a place.

    City_id (str): the city id
    User_id (str): the user id
    name (str): the name of the place
    Description (str): the description of the place
    Number_rooms (int): the number of rooms
    Number_bathrooms (int): the number of bathrooms
    Max_guest (int): number of guest
    Price_by_night (int): the price per night
    Latitude (float): the latitude of the place
    longitude (float): the longitude of the place
    amenity_ids (list): list of amenity ids """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
