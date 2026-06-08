# E-Commerce Product Sales Analysis

sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Display products sold more than 20 times
print("Products Sold More Than 20 Times:")
for product, count in sales.items():
    if count > 20:
        print(product)

# 2. Find the best-selling product
best_product = ""
best_sales = 0

for product, count in sales.items():
    if count > best_sales:
        best_sales = count
        best_product = product

print("\nBest Selling Product:", best_product, "(", best_sales, ")", sep="")

# 3. Find the least-selling product
least_product = ""
least_sales = float('inf')

for product, count in sales.items():
    if count < least_sales:
        least_sales = count
        least_product = product

print("\nLeast Selling Product:", least_product, "(", least_sales, ")", sep="")

# 4. Calculate total products sold
total_sold = 0
for count in sales.values():
    total_sold += count

print("\nTotal Units Sold:", total_sold)

# 5. Create a list of products requiring promotion
promotion_list = []

for product, count in sales.items():
    if count < 15:
        promotion_list.append(product)

print("\nProducts Requiring Promotion:")
print(promotion_list)

# 6. Count products having sales between 10 and 30
sales_count = 0

for count in sales.values():
    if 10 <= count <= 30:
        sales_count += 1

print("\nProducts Having Sales Between 10 and 30:", sales_count)