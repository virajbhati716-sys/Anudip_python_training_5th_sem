# Smart Railway Reservation System

seats = {
    1: "Booked",
    2: "Available",
    3: "Booked",
    4: "Available",
    5: "Booked",
    6: "Booked",
    7: "Available",
    8: "Booked",
    9: "Available",
    10: "Booked"
}

# 1. Display all available seat numbers
print("Available Seats:")
for seat_no, status in seats.items():
    if status == "Available":
        print(seat_no, end=" ")
print()

# 2. Count booked and available seats
booked = 0
available = 0

for status in seats.values():
    if status == "Booked":
        booked += 1
    else:
        available += 1

print("Booked Seats:", booked)
print("Available Seats:", available)

# 3. Reserve the first available seat
for seat_no, status in seats.items():
    if status == "Available":
        seats[seat_no] = "Booked"
        print("Seat", seat_no, "Reserved Successfully.")
        break

# 4. Cancel booking for a given seat number
seat = int(input("Enter seat number to cancel booking: "))

if seat in seats:
    if seats[seat] == "Booked":
        seats[seat] = "Available"
        print("Booking Cancelled Successfully.")
    else:
        print("Seat is already available.")
else:
    print("Invalid Seat Number")

# 5. Store updated reservation status in reservations.txt
file = open("reservations.txt", "w")

for seat_no, status in seats.items():
    file.write(str(seat_no) + "," + status + "\n")

file.close()

print("Reservation Details Saved Successfully.")

# 6. Display occupancy percentage
booked = 0

for status in seats.values():
    if status == "Booked":
        booked += 1

occupancy = (booked / len(seats)) * 100

print("Occupancy Percentage:", occupancy, "%")



    
