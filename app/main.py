import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop

def shop_trip():
    with open("config.json") as f:
        config = json.load(f)

    FUEL_PRICE = config["FUEL_PRICE"]

    shops = [Shop(s["name"], s["location"], s["products"]) for s in config["shops"]]
    customers = []

    for c in config["customers"]:
        car = Car(c["car"]["brand"], c["car"]["fuel_consumption"])
        cust = Customer(c["name"], c["product_cart"], c["location"], c["money"], car)
        customers.append(cust)

    for cust in customers:
        print(f"{cust.name} has {cust.money} dollars")

        costs = [(cust.trip_cost(shop, FUEL_PRICE), shop) for shop in shops]
        for cost, shop in costs:
            print(f"{cust.name}'s trip to the {shop.name} costs {cost:.2f}")

        affordable = [ (cost, shop) for cost, shop in costs if cost <= cust.money ]

        if not affordable:
            print(f"{cust.name} doesn't have enough money to make a purchase in any shop")
            continue

        affordable.sort(key=lambda x: x[0])
        best_cost, best_shop = affordable[0]

        print(f"{cust.name} rides to {best_shop.name}")
        cust.buy_from(best_shop, FUEL_PRICE)
