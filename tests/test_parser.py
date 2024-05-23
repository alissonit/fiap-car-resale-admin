from src.application.models.car import Car
from src.utils.parsers import car_parser
import asyncio


def test_car_parser():
    # Given
    car = Car(
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

    expected_data = {
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

    # When
    result = asyncio.run(car_parser(car))

    # Then
    assert result == expected_data
