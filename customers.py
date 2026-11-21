
# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Name: Jace Fisher

# Reflection 1:
# I would use .get() when a key might be missing because it prevents errors.
# I would use bracket notation when I know the key exists and need its value.

# Reflection 2:
# Exercise 8 reminds me of using a PivotTable in Excel to organize sales.
# Python can be more useful for large datasets because it can process and
# summarize lots of information automatically.

# --------------------------------------------------
# EXERCISE 1 - One customer
# --------------------------------------------------

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1250
}

print("EXERCISE 1")

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# --------------------------------------------------
# EXERCISE 2 - Update and add
# --------------------------------------------------

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# --------------------------------------------------
# EXERCISE 3 - Safe lookup
# --------------------------------------------------

print("\nEXERCISE 3")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


# --------------------------------------------------
# EXERCISE 4 - Iterate
# --------------------------------------------------

print("\nEXERCISE 4")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), looping through a dictionary gives only the keys.
for key in customer:
    print(key)


# --------------------------------------------------
# EXERCISE 5 - Lookup table
# --------------------------------------------------

print("\nEXERCISE 5")

tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .10,
    "platinum": .15
}

tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
original_price = 200
discounted_price = original_price * (1 - discount_rate)

print("Tier:", tier)
print("Discount rate:", discount_rate)
print("Final price:", discounted_price)


# --------------------------------------------------
# EXERCISE 6 - List of dictionaries
# --------------------------------------------------

print("\nEXERCISE 6")

customer2 = {
    "name": "Bob",
    "tier": "bronze"
}

customer3 = {
    "name": "Charlie",
    "tier": "silver"
}

customers = [customer, customer2, customer3]

for person in customers:
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount

    print(
        f'{person["name"]}: {tier}, '
        f'${discount_amount:.2f} discount'
    )


# --------------------------------------------------
# EXERCISE 7 - Nested catalog
# --------------------------------------------------

print("\nEXERCISE 7")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product}")


# --------------------------------------------------
# EXERCISE 8 - Sales by region
# --------------------------------------------------

print("\nEXERCISE 8")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: {sales_summary[region]}")