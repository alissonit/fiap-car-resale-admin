from fastapi_login import LoginManager
from datetime import datetime


from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import Provide, inject

from src.application.ports.car import CarPort
from src.application.models.car import Car

from src.adapters.driving.rest.v1.login import manager

from src.adapters.driving.rest.v1.dto.cars import (
    RegisterCarV1Request,
    RegisterCarV1Response,
    DeleteCarV1Response
)
from src.configuration.dependency_injection import Container


router = APIRouter()


@router.post("/api/v1/cars", response_model=RegisterCarV1Response)
@inject
async def register_car(
    response: Response,
    car_request: RegisterCarV1Request,
    car_port: CarPort = Depends(Provide[Container.car_repository]),
    auth: LoginManager = Depends(manager)
) -> RegisterCarV1Response:
    """
    Register a car
    """

    car = Car(
        car_user_id=car_request.car_user_id,
        car_brand=car_request.car_brand,
        car_model=car_request.car_model,
        car_year=car_request.car_year,
        car_color=car_request.car_color,
        car_price=car_request.car_price,
        car_type=car_request.car_type,
        car_condition=car_request.car_condition,
        car_transmission=car_request.car_transmission,
        car_mileage=car_request.car_mileage,
        car_engine=car_request.car_engine,
        car_fuel=car_request.car_fuel,
        car_description=car_request.car_description,
        car_armored=car_request.car_armored,
        car_sold=car_request.car_sold,
        car_created_at=datetime.now()
    )

    car = await car_port.register_car(car)

    response.status_code = status.HTTP_201_CREATED

    return car


@router.put("/api/v1/cars", response_model=RegisterCarV1Response)
@inject
async def update_car(
        response: Response,
        car_request: RegisterCarV1Request,
        car_port: CarPort = Depends(Provide[Container.car_repository]),
        auth: LoginManager = Depends(manager)
) -> RegisterCarV1Response:
    """
    Update a car
    """
    car = Car(
        car_id=car_request.car_id,
        car_user_id=car_request.car_user_id,
        car_brand=car_request.car_brand,
        car_model=car_request.car_model,
        car_year=car_request.car_year,
        car_color=car_request.car_color,
        car_price=car_request.car_price,
        car_type=car_request.car_type,
        car_condition=car_request.car_condition,
        car_transmission=car_request.car_transmission,
        car_mileage=car_request.car_mileage,
        car_engine=car_request.car_engine,
        car_fuel=car_request.car_fuel,
        car_description=car_request.car_description,
        car_armored=car_request.car_armored,
        car_created_at=datetime.now()
    )

    car = await car_port.update_car(car)

    response.status_code = status.HTTP_201_CREATED

    return car


@router.delete("/api/v1/cars/{car_id}", response_model=DeleteCarV1Response)
@inject
async def delete_car(
        response: Response,
        car_id: int,
        car_port: CarPort = Depends(Provide[Container.car_repository]),
        auth: LoginManager = Depends(manager)
) -> DeleteCarV1Response:
    """
    Delete a car
    """
    car = await car_port.delete_car(car_id)

    response.status_code = status.HTTP_200_OK

    return DeleteCarV1Response(car_id=car.car_id)
