from customer import Customer
from coffee import Coffee



c1 = Customer("Alice")
c2 = Customer("Bob")

print("Customers created:")
print(f" - {c1.name}")
print(f" - {c2.name}")
print()


latte = Coffee("Latte")
espresso = Coffee("Espresso")

print("Coffees created:")
print(f" - {latte.name}")
print(f" - {espresso.name}")
print()

order1 = c1.create_order(latte, 3.5)
order2 = c1.create_order(espresso, 4.5)
order3 = c2.create_order(latte, 5.0)

print("Alice's Coffees:", [coffee.name for coffee in c1.coffees()])
print("Latte's Customers:", [customer.name for customer in latte.customers()])

