"""
Reference:
How To Write Unit Tests in Python • Pytest Tutorial
https://www.youtube.com/watch?v=YbpKMIUjvK8

"""

from typing import List


class ShoppingCart:
    def __init__(self) -> None:
        pass

    def add(self, item: str):
        pass

    def size(self) -> int:
        return 0

    def get_items(self) -> List[str]:
        return []

    def get_total_price(self, price_map):
        pass
