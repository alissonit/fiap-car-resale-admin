from abc import ABC, abstractmethod

from src.application.models.car import Car


class CarPort(ABC):
    """
    Interface for Car Port
    """

    @abstractmethod
    async def register_car(self, car: Car) -> Car:
        """
        Register Car
        """
        pass

    @abstractmethod
    async def update_car(self, car: Car) -> Car:
        """
        Update Car
        """
        pass

    @abstractmethod
    async def delete_car(self, car_id: str) -> Car:
        """
        Delete Car
        """
        pass
