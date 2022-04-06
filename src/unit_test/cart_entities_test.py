import os
import sys
import unittest
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from domain.entity.item import Item
from domain.entity.product import Product
from domain.entity.cart import Cart



class TestCartUnit(unittest.TestCase):

    def test_constructor(self):
        cart = Cart(Item(Product(1, 'Microservices', 1.0, 99), 1))

        self.assertEqual(cart.items.product.get_id, 1)
        self.assertEqual(cart.items.product.get_name, "Microservices")
        self.assertEqual(cart.items.product.get_price, 1.0)
        self.assertEqual(cart.items.product.get_stock, 99)
        self.assertEqual(cart.items.get_quantity, 1)

    # def test_is_immutable(self):
    #     with self.assertRaises(FrozenInstanceError) as assert_error:
    #         value_object = Category(name='test')
    #         value_object.name = 'fake name'

if __name__ == "__main__":
    unittest.main()
