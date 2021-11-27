from fastapi import APIRouter
import logging

from webapp.functions.vehicle_retrieval import regional_search, listing_retrieval
from webapp.api.base_model import VehicleDataRequest, VehicleSearchRequest

router = APIRouter()
log = logging.getLogger(__name__)


@router.post("/vehicledata/metrics")
def get_vehicle_stats(data: VehicleDataRequest):
    """Produces statistical metrics: min, med, max of requested vehicles
    Arguments, to be included in a dictionary object for submission.
    keys of the dictionary, and the type of the corresponding values are below

    Arguments:
    ---
    `longitude` float - longitudinal position of customer location

    `latitude` float - latitudinal position of customer location

    `year` int - year of car model

    `manufacturer` str - manufacturer name

    `condition` str - condition of car choices: 'fair', 'new', 'poor', 'good', 'parts'

    `miles` int - miles on odometer

    `type` str - e.g. - sedan, coupe, SUV

    `transmission` str - e.g. - automatic, manual

    `drive` str - e.g. front wheel drive, four wheel drive, or rear wheel drive.

    `color`: str - Paint color of car, e.g. red, cobalt, silver

    `fuel`: str - fuel type of car, e.g. gas, electric, diesel, other

    Returns:
    ---
    metrics for vehicle specified in nearby regions
    """
    print(regional_search(data.params))
    return regional_search(data.params)

@router.post("/vehicledata/listings")
def get_vehicle_listings(data: VehicleSearchRequest):
    """Produces listings based on given features and selected

    Arguments:
    ---
    `radius` int - distance customer is willing to travel

    `option` int - details type of search requested. Options are 1: regional, 2: basic radius, 3: flex/lucky search

    `longitude` float - longitudinal position of customer location

    'latitude` float - latitudinal position of customer location

    `search_option` str - lucky, regional, basic

    `year` int - year of car model

    `make` str - manufacturer name

    `condition` str - condition of car choices: 'fair', 'new', 'poor', 'good', 'parts'

    `miles` int - miles on odometer

    `type` str - e.g. - sedan, coupe, SUV

    `transmission` str - e.g. - automatic, manual

    `drive` str - e.g. front wheel drive, four wheel drive, or rear wheel drive.

    `color`: str - Paint color of car, e.g. red, cobalt, silver

    `fuel`: str - fuel type of car, e.g. gas, electric, diesel, other

    Returns:
    ---
    metrics for vehicle specified in nearby regions
    """

    return listing_retrieval(data.params)