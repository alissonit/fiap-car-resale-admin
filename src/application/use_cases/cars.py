import logging

from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from src.application.ports.car import CarPort

from src.adapters.driving.rest.v1.dto.cars import (
    RegisterCarV1Request,
    RegisterCarV1Response,
    DeleteCarV1Response
)
from src.configuration.dependency_injection import Container


router = APIRouter()


class CarUseCase:
    """Class to manage car use cases
    """

    @staticmethod
    @inject
    async def register_car(
        car_request: RegisterCarV1Request,
        car_port: CarPort = Depends(Provide[Container.car_sale_adapter]),
    ) -> RegisterCarV1Response:
        """
        Register a car
        """

        car = await car_port.register_car(car_request)

        logging.info("Car registered: %s", car)

        return car

    @staticmethod
    @inject
    async def update_car(
            car_request: RegisterCarV1Request,
            car_port: CarPort = Depends(Provide[Container.car_sale_adapter]),
    ) -> RegisterCarV1Response:
        """
        Update a car
        """

        car = await car_port.update_car(car_request)

        logging.info("Car updated: %s", car)

        return car

    @staticmethod
    @inject
    async def delete_car(
            car_id: int,
            car_port: CarPort = Depends(Provide[Container.car_sale_adapter]),
    ) -> DeleteCarV1Response:
        """
        Delete a car
        """
        car = await car_port.delete_car(car_id)

        logging.info("Car deleted: %s", car)

        return car
