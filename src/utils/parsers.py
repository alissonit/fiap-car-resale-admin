from src.application.models.car import Car


async def car_parser(car: Car):

    data = {
        "car_id": car.car_id if car.car_id else "",
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

    return data
