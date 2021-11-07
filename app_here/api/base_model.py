# import sys
# from typing import List

from pydantic import BaseModel, Field, validator


class VehicleDataRequest(BaseModel):
    """Model that handles vehicle data request to the API:
    Returns min, max and median values for described vehicle"""

    year: int = Field(..., example=2013)
    make: str = Field(..., example='Toyota')
    model: str = Field(..., example='Corolla')
    mileage: int = Field(..., example=90000)
    category: str = Field(..., example='sedan')
    transmission: str = Field(..., example='Automatic')
    drive_style: str = Field(..., example='fwd')
    color: str = Field(..., example='red')
