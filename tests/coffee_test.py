import unittest
from customer import Customer
from coffee import Coffee

class TestCoffee(unittest.TestCase):

    def test_valid_name(self):
        coffee = Coffee("Latte")
        self.assertEqual(coffee.name, "Latte")

    def test_invalid_name_too_short(self):
        with self.assertRaises(ValueError):
            Coffee("ab")

    def test_num_orders_and_average_price(self):
        coffee = Coffee("Espresso")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")

        customer1.create_order(coffee, 4.0)
        customer2.create_order(coffee, 6.0)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertEqual(coffee.average_price(), 5.0)

    def test_customers_unique(self):
        coffee = Coffee("Cappuccino")
        customer = Customer("Eve")

        customer.create_order(coffee, 4.5)
        customer.create_order(coffee, 5.5)

        customers = coffee.customers()
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0].name, "Eve")

if __name__ == "__main__":
    unittest.main()
