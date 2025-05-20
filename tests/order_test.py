import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):

    def test_valid_order(self):
        customer = Customer("Tom")
        coffee = Coffee("Flat White")
        order = Order(customer, coffee, 3.5)

        self.assertEqual(order.customer.name, "Tom")
        self.assertEqual(order.coffee.name, "Flat White")
        self.assertEqual(order.price, 3.5)

    def test_invalid_customer_type(self):
        coffee = Coffee("Americano")
        with self.assertRaises(TypeError):
            Order("NotACustomer", coffee, 4.0)

    def test_invalid_coffee_type(self):
        customer = Customer("Jerry")
        with self.assertRaises(TypeError):
            Order(customer, "NotACoffee", 4.0)

    def test_invalid_price_type(self):
        customer = Customer("Sam")
        coffee = Coffee("Mocha")
        with self.assertRaises(ValueError):
            Order(customer, coffee, "cheap")

    def test_invalid_price_range(self):
        customer = Customer("Sam")
        coffee = Coffee("Mocha")

        with self.assertRaises(ValueError):
            Order(customer, coffee, 0.5)

        with self.assertRaises(ValueError):
            Order(customer, coffee, 15.0)

if __name__ == "__main__":
    unittest.main()
