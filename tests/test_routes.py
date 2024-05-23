import pytest
from starlette.testclient import TestClient
from unittest.mock import AsyncMock
from src.configuration.dependency_injection import Container
from src.application.models.users import User
from src.application.ports.users import UserPort
from src.application.models.car import Car
from src.application.ports.car import CarPort
from main import app


@pytest.fixture
def car() -> Car:
    return Car(
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


@pytest.fixture
def user() -> User:
    return User(
        user_email="test@hotmail.com",
        user_name="test",
        user_password="test",
        user_phone="11999999999"
    )


@pytest.fixture
def mock_car_port(car):
    return AsyncMock(
        spec=CarPort,
        register_car=AsyncMock(return_value=car),
        update_car=AsyncMock(return_value=car),
        delete_car=AsyncMock(return_value=car)
    )


@pytest.fixture
def mock_user_port(user):
    return AsyncMock(
        spec=UserPort,
        register_user=AsyncMock(return_value=user),
        list_users=AsyncMock(return_value=[user]),
        list_by_user_email=AsyncMock(return_value=user),
        list_by_user_id=AsyncMock(return_value=user),
        update_user=AsyncMock(return_value=user),
        delete_user=AsyncMock(return_value=user)
    )


@pytest.fixture
def container(mocker, mock_user_port, mock_car_port):
    container = Container()
    container.engine.override(mocker.Mock())
    container.user_repository.override(mock_user_port)
    container.car_sale_adapter.override(mock_car_port)
    return container


@pytest.fixture
def client(container):
    app.container = container
    return TestClient(app)


def test_register_user(mocker, client):
    # Given
    response = client.post("/fiap-car-resale/admin/api/v1/users", json={

        "user_email": "test2@hotmail.com",
        "user_name": "test2",
        "user_password": "test2",
        "user_phone": "11999999999"
    })

    # Then
    assert response.status_code == 200


def test_list_users(mocker, client):

    # Given
    response = client.get("/fiap-car-resale/admin/api/v1/users")

    # Then
    assert response.status_code == 401


def test_list_by_user_email(client):
    # Given
    response = client.get(
        "/fiap-car-resale/admin/api/v1/users/test@hotmail.com")

    # Then
    assert response.status_code == 401


def test_register_car(client):
    # Given
    response = client.post("/fiap-car-resale/admin/api/v1/cars")

    # Then
    assert response.status_code == 401


def test_update_car(client):
    # Given
    response = client.put("/fiap-car-resale/admin/api/v1/cars")

    # Then
    assert response.status_code == 401


def test_delete_car(client):
    # Given
    response = client.delete("/fiap-car-resale/admin/api/v1/cars/1")

    # Then
    assert response.status_code == 401
