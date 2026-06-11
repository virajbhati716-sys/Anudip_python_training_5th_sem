# Online Shopping Cart Analyzer

cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

# 1. Calculate total cart value
total_value = sum(cart)

# 2. Find most expensive and cheapest products
most_expensive = max(cart)
cheapest = min(cart)

# 3. Count premium shipping eligible products (price > 1000)
premium_count = 0
for price in cart:
    if price > 1000:
        premium_count += 1

# 4. Generate discount list (price > 1500)
discount_products = []
for price in cart:
    if price > 1500:
        discount_products.append(price)

# 5. Calculate average product price
average_price = total_value / len(cart)

# Display Results
print("Total Cart Value: ₹", total_value)
print("Most Expensive Product: ₹", most_expensive)
print("Cheapest Product: ₹", cheapest)
print("Premium Shipping Eligible Products:", premium_count)
print("Discount Eligible Products:")
print(discount_products)
print("Average Product Price: ₹", average_price)