import math
from dataclasses import dataclass
from typing import TYPE_CHECKING

from app.car import Car

if TYPE_CHECKING:
    from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: float
    car: Car

    def get_total_trip_cost(self, shop: "Shop", fuel_price: float) -> float:
        distance = math.hypot(
            shop.location[0] - self.location[0],
            shop.location[1] - self.location[1],
        )

        fuel_cost = self.car.get_fuel_amount(distance) * fuel_price * 2

        products_cost = 0.0
        for product, quantity in self.product_cart.items():
            price = shop.products.get(product, 0)
            products_cost += price * quantity

        return fuel_cost + products_cost
