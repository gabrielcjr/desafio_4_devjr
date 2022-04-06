from dataclasses import FrozenInstanceError, dataclass, is_dataclass
import unittest
from datetime import datetime
from domain.entity.product import Product
from domain.entity.cart import Cart
from src.domain.entity.item import Item


class TestCartUnit(unittest.TestCase):

    def test_constructor(self):
        cart = Cart(Item(Product(1, 'Microservices', 1.0, 99), 1))

        self.assertEqual(cart.items.product.get_id, 1)
        self.assertEqual(cart.items.product.get_name, "Microservices")
        self.assertEqual(cart.items.product.get_price, 1.0)
        self.assertEqual(cart.items.product.get_stock, 99)
        self.assertEqual(cart.items.get_quantity, 1)

    # def test_if_created_at_is_generated_in_constructor(self):
    #     category1 = Category(name="Movie 1")
    #     category2 = Category(name="Movie 2")
    #     self.assertNotEqual(
    #         category1.created_at.timestamp(), category2.created_at.timestamp()
    #     )

    # def test_is_immutable(self):
    #     with self.assertRaises(FrozenInstanceError) as assert_error:
    #         value_object = Category(name='test')
    #         value_object.name = 'fake name'

if __name__ == "__main__":
    unittest.main()
