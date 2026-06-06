# Flight Booking Analysis

bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# 1. Display confirmed passengers
print("Confirmed Passengers:")
for p in bookings:
    if p[2] == "Confirmed":
        print(p[0], p[1])

# 2. Count passengers travelling to Delhi
delhi_count = 0
for p in bookings:
    if p[1] == "Delhi":
        delhi_count += 1

print("\nPassengers Travelling to Delhi:", delhi_count)

# 3. Count booking status
confirmed = 0
waiting = 0
cancelled = 0

for p in bookings:
    if p[2] == "Confirmed":
        confirmed += 1
    elif p[2] == "Waiting":
        waiting += 1
    elif p[2] == "Cancelled":
        cancelled += 1

print("\nConfirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)

# 4. Create waiting list
waiting_list = []

for p in bookings:
    if p[2] == "Waiting":
        waiting_list.append(p[0])

print("\nWaiting List:")
print(waiting_list)

# 5. Find most booked destination
destinations = {}

for p in bookings:
    destination = p[1]
    if destination in destinations:
        destinations[destination] += 1
    else:
        destinations[destination] = 1

most_booked = ""
max_count = 0

for destination, count in destinations.items():
    if count > max_count:
        max_count = count
        most_booked = destination

print("\nMost Booked Destination:")
print(most_booked)