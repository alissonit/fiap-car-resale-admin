from fastapi_login import LoginManager


from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import Provide, inject

from src.application.ports.car import CarPort

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
    car_port: CarPort = Depends(Provide[Container.car_sale_adapter]),
    auth: LoginManager = Depends(manager)
) -> RegisterCarV1Response:
    """
    Register a car
    """

    car = await car_port.register_car(car_request)

    response.status_code = status.HTTP_201_CREATED

    return car


@router.put("/api/v1/cars", response_model=RegisterCarV1Response)
@inject
async def update_car(
        response: Response,
        car_request: RegisterCarV1Request,
        car_port: CarPort = Depends(Provide[Container.car_sale_adapter]),
        auth: LoginManager = Depends(manager)
) -> RegisterCarV1Response:
    """
    Update a car
    """

    car = await car_port.update_car(car_request)

    response.status_code = status.HTTP_200_OK

    return car


@router.delete("/api/v1/cars/{car_id}", response_model=DeleteCarV1Response)
@inject
async def delete_car(
        response: Response,
        car_id: int,
        car_port: CarPort = Depends(Provide[Container.car_sale_adapter]),
        auth: LoginManager = Depends(manager)
) -> DeleteCarV1Response:
    """
    Delete a car
    """
    car = await car_port.delete_car(car_id)

    response.status_code = status.HTTP_200_OK

    return DeleteCarV1Response(car_id=car.car_id)
