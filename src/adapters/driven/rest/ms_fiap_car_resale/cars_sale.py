import requests

from src.application.models.car import Car
from src.application.ports.car import CarPort


class CarSaleAdapter(CarPort):
    """
    Class Repository for Car
    """

    def __init__(self) -> None:
        self.car_sale_uri = "http://localhost:7000/fiap-car-resale/api/v1"

    async def get_sales(self) -> Car:

        response = requests.get(f"{self.car_sale_uri}/sales")
        return response.json()

    async def register_car(self, car: Car) -> Car:
        """
        Register Car
        """

        data = {
            "car_armored": car.car_armored,
            "car_brand": car.car_brand,
            "car_color": car.car_color,
            "car_condition": car.car_condition,
            "car_description": car.car_description,
            "car_engine": car.car_engine,
            "car_fuel": car.car_fuel,
            "car_mileage": car.car_mileage,
            "car_model": car.car_model,
            "car_price": car.car_price,
            "car_sold": car.car_sold,
            "car_transmission": car.car_transmission,
            "car_type": car.car_type,
            "car_user_id": car.car_user_id,
            "car_year": car.car_user_id
        }

        response = requests.post(f"{self.car_sale_uri}/cars", json=data)
        return response.json()

    async def update_car(self, car: Car) -> Car:
        """
        Update Car
        """

        data = {
            "car_id": car.car_id,
            "car_armored": car.car_armored,
            "car_brand": car.car_brand,
            "car_color": car.car_color,
            "car_condition": car.car_condition,
            "car_description": car.car_description,
            "car_engine": car.car_engine,
            "car_fuel": car.car_fuel,
            "car_mileage": car.car_mileage,
            "car_model": car.car_model,
            "car_price": car.car_price,
            "car_sold": car.car_sold,
            "car_transmission": car.car_transmission,
            "car_type": car.car_type,
            "car_user_id": car.car_user_id,
            "car_year": car.car_user_id
        }

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

