from scripts.shopping_cart import ShoppingCart
import pytest
from unittest.mock import Mock
from scripts.item_database import ItemDatabase


@pytest.fixture
def cart():
    # All the setup for the cart here...
    # This fixture is created new for every test function.
    # You can put this file in the '/tests/conftest.py' file.
    return ShoppingCart(5)


def test_pass_function():
    pass


def test_can_add_item_to_cart(cart):
    # cart: ShoppingCart = ShoppingCart(5)  # 'cart' was created as a fixture and passed as an argument,
    cart.add("apple")
    assert cart.size() == 1


def test_when_item_added_cart_contains_item(cart):
    # cart: ShoppingCart = ShoppingCart(5)  # 'cart' was created as a fixture and passed as an argument,
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_when_more_than_max_items(cart):
    # cart: ShoppingCart = ShoppingCart(5)  # 'cart' was created as a fixture and passed as an argument,
    for _ in range(5):  # Prefill the cart with 5 items.
        cart.add("apple")

    with pytest.raises(OverflowError):
        cart.add("apple")  # Prefill allows only raises on the 6th item.


def test_can_get_total_price(cart):
    # cart: ShoppingCart = ShoppingCart(5)  # 'cart' was created as a fixture and passed as an argument,
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()

    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0

    # item_database.get = Mock( price_map={'apple':1.0,'orange':2.0} )
    # item_database.get = Mock( return_value = 1.0 )
    item_database.get = Mock(side_effect=mock_get_item)
    # item_database.get()  # Future implementation.

    assert cart.get_total_price(item_database) == 3.0
