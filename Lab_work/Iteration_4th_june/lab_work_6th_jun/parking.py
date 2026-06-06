# Smart Parking System

slots = [1, 0, 1, 1, 0, 0, 1, 0]

# 1. Count occupied and available slots
occupied = 0
available = 0

for slot in slots:
    if slot == 1:
        occupied += 1
    else:
        available += 1

print("Occupied Slots:", occupied)
print("Available Slots:", available)

# 2. Find the first available slot
for i in range(len(slots)):
    if slots[i] == 0:
        print("\nFirst Available Slot:", i + 1)
        break

# 3. Display all available slot numbers
print("\nAvailable Slot Numbers:")
for i in range(len(slots)):
    if slots[i] == 0:
        print(i + 1)

# 4. Check whether occupancy exceeds 75%
occupancy = (occupied / len(slots)) * 100

print("\nOccupancy Percentage:", occupancy, "%")

if occupancy > 75:
    print("Parking Occupancy Exceeds 75%")
else:
    print("Parking Occupancy Does Not Exceed 75%")