from fastapi_login import LoginManager


from fastapi import APIRouter, Depends, Response, status


from src.adapters.driving.rest.v1.login import manager

from src.adapters.driving.rest.v1.dto.cars import (
    RegisterCarV1Request,
    RegisterCarV1Response,
    DeleteCarV1Response
)

from src.application.use_cases.cars import CarUseCase


router = APIRouter()


@router.post("/api/v1/cars", response_model=RegisterCarV1Response)
async def register_car(
    response: Response,
    car_request: RegisterCarV1Request,
    auth: LoginManager = Depends(manager)
) -> RegisterCarV1Response:
    """
    Register a car
    """

    car = await CarUseCase.register_car(car_request)

    response.status_code = status.HTTP_201_CREATED

    return car


@router.put("/api/v1/cars", response_model=RegisterCarV1Response)
async def update_car(
        response: Response,
        car_request: RegisterCarV1Request,
        auth: LoginManager = Depends(manager)
) -> RegisterCarV1Response:
    """
    Update a car
    """

    car = await CarUseCase.update_car(car_request)

    response.status_code = status.HTTP_200_OK

    return car


@router.delete("/api/v1/cars/{car_id}", response_model=DeleteCarV1Response)
async def delete_car(
        response: Response,
        car_id: int,
        auth: LoginManager = Depends(manager)
) -> DeleteCarV1Response:
    """
    Delete a car
    """
    car = await CarUseCase.delete_car(car_id)

    response.status_code = status.HTTP_200_OK

    return DeleteCarV1Response(car_id=car["car_id"])
