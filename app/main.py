import json
from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    data_path = Path(__file__).resolve().parent.parent / "config.json"

    with open(data_path, encoding="utf-8") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]

    customers = []
    for customer_data in data["customers"]:
        car = Car(**customer_data["car"])
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car,
        )
        customers.append(customer)

    shops = [Shop(**shop_data) for shop_data in data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trips = []
        for shop in shops:
            cost = round(
                customer.get_total_trip_cost(shop, fuel_price),
                2,
            )
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
            trips.append((shop, cost))

        shop, best_cost = min(trips, key=lambda item: item[1])

        if best_cost > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
            print()
            continue

        print(f"{customer.name} rides to {shop.name}\n")

        start_location = customer.location[:]
        customer.location = shop.location

        shop.print_receipt(customer)
        print()

        customer.money = round(customer.money - best_cost, 2)
        customer.location = start_location

        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money} dollars\n")
