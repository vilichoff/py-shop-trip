from dataclasses import dataclass
import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


@dataclass
class Shop:
    name: str
    products: dict
    location: list[int]

    def print_receipt(self, customer: "Customer") -> None:
        now = datetime.datetime.now()
        print(f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_price = 0.0
        for product, quantity in customer.product_cart.items():
            price = self.products.get(product, 0)
            item_total = price * quantity
            total_price += item_total
            print(f"{quantity} {product}s for {item_total} dollars")

        print(f"Total cost is {total_price} dollars")
        print("See you again!")

        return total_price
