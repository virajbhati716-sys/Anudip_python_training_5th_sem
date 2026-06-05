# Inventory Stock Alert System

stock = [25, 5, 0, 12, 3, 18, 0, 30]

# 1. Count out-of-stock products
out_of_stock = stock.count(0)

# 2. Products that need restocking (less than 10)
restock_required = [item for item in stock if item < 10]

# 3. Count available products
available_products = len([item for item in stock if item > 0])

# 4. Products with healthy stock (>= 15)
healthy_stock = [item for item in stock if item >= 15]

# Display results
print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock_required)
print("Available Products:", available_products)
print("Healthy Stock:", healthy_stock)