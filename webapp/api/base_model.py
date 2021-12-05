# import sys
# from typing import List

from pydantic import BaseModel, Field, validator


class VehicleDataRequest(BaseModel):
    """Model that handles vehicle data request to the API:
    Returns min, max and median values for described vehicle
    using the regional search method."""

    params: dict = Field(..., example={
        "latitude": 44.1758,
        "longitude": -120.809,
        "manufacturer": "toyota",
        "condition": "fair"
    }, description="a dicitonary with features for keys and corresponding values for values")


class VehicleSearchRequest(BaseModel):
    """Model returns a set of vehicles from one of three
    search algorithms: basic radius, regional_search, lucky_search"""

    params: dict = Field(..., example={
        "latitude": 43.98893819541224,
        "longitude": -120.35412099977503,
        "radius": 30,
        "option": 1,
        "manufacturer": "toyota",
        "condition": "fair"
    }, description="a dicitonary with features for keys and corresponding values for values")
