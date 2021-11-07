from fastapi import APIRouter
import logging

from app_here.functions.vehicle_retrieval import regional_search
from app_here.api.base_model import VehicleDataRequest

router = APIRouter()
log = logging.getLogger(__name__)


@router.post("/vehicledata/metrics")
def get_vehicle_stats(data: VehicleDataRequest):
    """Produces statistical metrics: min, med, max of requested vehicles
    Arguments
    ---
    `year` int - year of car model

    `make` str - manufacturer name

    `model` str - model name

    `mileage` int - miles on odometer

    `category` str - e.g. - sedan, coupe, SUV

    `transmission` str - e.g. - automatic, manual

    `drive_style` str - e.g. fwd, 4wd, or rwd.

    `color`: str - Paint color of car, e.g. red, blue, silver

    Returns:
    ---
    metrics for vehicle specified in nearby regions
    """
    return regional_search(data.year, data.make, data.model, data.mileage,
                           data.category, data.transmission, data.drive_style,
                           data.color)
