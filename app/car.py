from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def get_fuel_amount(self, distance: float) -> float:
        fuel_amount = distance / 100 * self.fuel_consumption
        return fuel_amount
