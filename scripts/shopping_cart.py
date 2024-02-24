"""
Reference:
How To Write Unit Tests in Python • Pytest Tutorial
https://www.youtube.com/watch?v=YbpKMIUjvK8

"""

from typing import List


class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items_in_cart: List[str] = []
        self.max_size = max_size

    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError("Cannot add more items\n")
        self.items_in_cart.append(item)

    def size(self) -> int:
        return len(self.items_in_cart)

    def get_items(self) -> List[str]:
        return self.items_in_cart

    def get_total_price(self, price_map):
        total_price = 0
        for lookup_item in self.items_in_cart:
            total_price += price_map.get(lookup_item)
        return total_price
