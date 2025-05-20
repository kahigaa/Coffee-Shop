import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")

        with self.assertRaises(ValueError):
            Customer("a" * 16)

        c = Customer("Anna")
        self.assertEqual(c.name, "Anna")

    def test_create_order(self):
        c = Customer("John")
        coffee = Coffee("Mocha")
        c.create_order(coffee, 3.5)
        self.assertEqual(len(c.orders()), 1)

if __name__ == "__main__":
    unittest.main()
