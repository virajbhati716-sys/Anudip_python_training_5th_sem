vehicle = input("Enter Vehicle Number: ")

# 1. Extract state code
state_code = vehicle[:2]

# 2. Extract district code
district_code = vehicle[2:4]

# 3. Extract vehicle series
series = vehicle[4:6]

# 4. Extract vehicle number
vehicle_number = vehicle[6:]

# 5. Count letters and digits
letters = 0
digits = 0

for ch in vehicle:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

# 6. Verify format
valid = True

if len(vehicle) != 10:
    valid = False
elif not vehicle[:2].isalpha():
    valid = False
elif not vehicle[2:4].isdigit():
    valid = False
elif not vehicle[4:6].isalpha():
    valid = False
elif not vehicle[6:].isdigit():
    valid = False

# 7. Display result
print("\nVehicle Number:", vehicle)
print("State Code:", state_code)
print("District Code:", district_code)
print("Series:", series)
print("Vehicle Number:", vehicle_number)

print("\nTotal Letters:", letters)
print("Total Digits:", digits)

if valid:
    print("\nVehicle Number Status: Valid")
else:
    print("\nVehicle Number Status: Invalid")