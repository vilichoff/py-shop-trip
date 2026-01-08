import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in config["shops"]
    ]
    customers = []
    for customer_data in config["customers"]:
        car = Car(
            customer_data["car"]["brand"],
            customer_data["car"]["fuel_consumption"],
        )
        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            car,
        )
        customers.append(customer)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        costs = [
            (customer.trip_cost(shop, fuel_price), shop)
            for shop in shops
        ]
        for cost, shop in costs:
            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{cost:.2f}"
            )

        affordable = [
            (cost, shop)
            for cost, shop in costs
            if cost <= customer.money
        ]

        if not affordable:
            print(
                f"{customer.name} doesn't have enough money to make a "
                "purchase in any shop"
            )
            continue

        affordable.sort(key=lambda x: x[0])
        best_cost, best_shop = affordable[0]

        print(f"{customer.name} rides to {best_shop.name}")
        customer.buy_from(best_shop, fuel_price)
