# Inventory Management System

inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# Display products with stock less than 10
print("Products with stock less than 10:")
for product, stock in inventory.items():
    if stock < 10:
        print(product, ":", stock)

# Count products having stock more than 50
count = 0
for stock in inventory.values():
    if stock > 50:
        count += 1

print("\nProducts with stock more than 50:", count)

# Find the product with minimum stock
min_product = ""
min_stock = float('inf')

for product, stock in inventory.items():
    if stock < min_stock:
        min_stock = stock
        min_product = product

print("\nProduct with Minimum Stock:", min_product, "-", min_stock)

# Create a list of products requiring restocking
restock = []

for product, stock in inventory.items():
    if stock < 20:
        restock.append(product)

print("\nProducts Requiring Restocking:")
print(restock)

# Calculate total inventory count
total_stock = 0

for stock in inventory.values():
    total_stock += stock

print("\nTotal Inventory Count:", total_stock)