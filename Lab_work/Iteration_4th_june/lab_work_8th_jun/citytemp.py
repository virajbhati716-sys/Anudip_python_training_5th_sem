# City Temperature Monitoring System

temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Display cities having temperature above 40°C
print("Cities Above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)

# 2. Find the hottest city
hottest_city = ""
max_temp = 0

for city, temp in temperature.items():
    if temp > max_temp:
        max_temp = temp
        hottest_city = city

print("\nHottest City:", hottest_city, "(", max_temp, "°C)", sep="")

# 3. Find the coolest city
coolest_city = ""
min_temp = float('inf')

for city, temp in temperature.items():
    if temp < min_temp:
        min_temp = temp
        coolest_city = city

print("\nCoolest City:", coolest_city, "(", min_temp, "°C)", sep="")

# 4. Calculate average temperature
total = 0
for temp in temperature.values():
    total += temp

average = total / len(temperature)

print("\nAverage Temperature:", average, "°C")

# 5. Create a list of pleasant cities
pleasant_cities = []

for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)

print("\nPleasant Cities:")
print(pleasant_cities)

# 6. Count cities with temperature between 35°C and 40°C
count = 0

for temp in temperature.values():
    if 35 <= temp <= 40:
        count += 1

print("\nCities Between 35°C and 40°C:", count)