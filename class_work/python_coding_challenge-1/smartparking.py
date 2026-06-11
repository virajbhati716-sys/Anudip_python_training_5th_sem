# Sample Data
parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]

# 1. Display vacant parking slot numbers
print("Vacant Parking Slots:")

for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        print(i + 1, end=" ")
print()

# 2. Count occupied and vacant slots
occupied_count = 0
vacant_count = 0

for slot in parking_slots:
    if slot == "Occupied":
        occupied_count += 1
    else:
        vacant_count += 1

print("\nOccupied Slots:", occupied_count)
print("Vacant Slots:", vacant_count)

# 3. Allocate first vacant slot
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        parking_slots[i] = "Occupied"
        print(f"\nVehicle Allocated to Slot {i + 1}")
        break

# 4. Calculate occupancy percentage
occupied_count = 0
for slot in parking_slots:
 if slot == "Occupied":
     occupied_count += 1

occupancy_percentage = (occupied_count / len(parking_slots)) * 100

print(f"Occupancy Percentage: {occupancy_percentage}%")

# 5. Store updated parking information in parking.txt
file = open("parking.txt", "w")

for i in range(len(parking_slots)):
    file.write(f"Slot {i + 1}: {parking_slots[i]}\n")

file.close()

print("Parking Details Saved Successfully.")
