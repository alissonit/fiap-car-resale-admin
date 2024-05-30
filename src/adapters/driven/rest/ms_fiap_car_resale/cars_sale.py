import requests
import os
from src.application.models.car import Car
from src.utils.parsers import car_parser

from src.configuration.settings import FIAP_SALE_URL


class CarSaleAdapter:
    """
    Class Repository for Car
    """

    def __init__(self) -> None:
        self.car_sale_uri = f"{FIAP_SALE_URL}/fiap-car-resale/api/v1"

    async def get_sales(self) -> Car:

        response = requests.get(f"{self.car_sale_uri}/sales")
        return response.json()

    async def register_car(self, car: Car) -> Car:
        """
        Register Car
        """

        data = await car_parser(car)

        response = requests.post(f"{self.car_sale_uri}/cars", json=data)
        return response.json()

    async def update_car(self, car: Car) -> Car:
        """
        Update Car
        """

        data = await car_parser(car)

        response = requests.put(f"{self.car_sale_uri}/cars", json=data)
        return response.json()

    async def delete_car(self, car_id: int) -> Car:
        """
        Delete Car
        """

        data = {
            "car_id": car_id
        }

        response = requests.delete(
            f"{self.car_sale_uri}/cars/{car_id}", json=data)
        return response.json()
