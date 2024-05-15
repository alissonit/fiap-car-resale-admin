import requests


class CarSaleAdapter:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_car_sale(self, car_id):
        url = f"{self.base_url}/car/{car_id}"
        response = requests.get(url)
        return response.json()
