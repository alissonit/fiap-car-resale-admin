import pytest
import requests
from unittest.mock import MagicMock
from src.application.models.car import Car
from src.application.ports.car import CarPort
from src.adapters.driven.rest.ms_fiap_car_resale.cars_sale import CarSaleAdapter


class ResponseObject:

    @staticmethod
    def json():
        return {
            "car_id": 1,
            "car_user_id": 1,
            "car_brand": "Toyota",
            "car_model": "Corolla",
            "car_year": 2021,
            "car_color": "Black",
            "car_price": 30000.00,
            "car_type": "Sedan",
            "car_condition": "New",
            "car_transmission": "Automatic",
            "car_mileage": 10.500,
            "car_engine": 1.8,
            "car_fuel": "Gasoline",
            "car_description": "Brand new car",
            "car_armored": False,
            "car_sold": False
        }


@pytest.fixture
def car_sale_adapter():
    return CarSaleAdapter()


@pytest.fixture
def mock_car():
    return Car(
        car_id=1,
        car_user_id=1,
        car_brand="Toyota",
        car_model="Corolla",
        car_year=2021,
        car_color="Black",
        car_price=30000.00,
        car_type="Sedan",
        car_condition="New",
        car_transmission="Automatic",
        car_mileage=10.500,
        car_engine=1.8,
        car_fuel="Gasoline",
        car_description="Brand new car",
        car_armored=False,
        car_sold=False
    )


@pytest.mark.asyncio
async def test_get_sales(car_sale_adapter: CarPort):

    expected_data = ResponseObject
    # Mock the requests.get method
    requests.get = MagicMock(return_value=expected_data)

    # When
    result = await car_sale_adapter.get_sales()

    # Then
    assert result == expected_data.json()


@pytest.mark.asyncio
async def test_register_car(car_sale_adapter: CarPort, mock_car):

    expected_data = ResponseObject
    # Mock the requests.post method
    requests.post = MagicMock(return_value=expected_data)

    # When
    result = await car_sale_adapter.register_car(mock_car)

    # Then
    assert result == expected_data.json()


@pytest.mark.asyncio
async def test_update_car(car_sale_adapter: CarPort, mock_car):
    # Given
    expected_data = ResponseObject
    # Mock the requests.put method
    requests.put = MagicMock(return_value=expected_data)

    # When
    result = await car_sale_adapter.update_car(mock_car)

    # Then
    assert result == expected_data.json()


@pytest.mark.asyncio
async def test_delete_car(car_sale_adapter: CarPort):
    # Given
    car_id = 1
    expected_data = ResponseObject

    # Mock the requests.delete method
    requests.delete = MagicMock(return_value=expected_data)

    # When
    result = await car_sale_adapter.delete_car(car_id)

    # Then
    assert result == expected_data.json()
