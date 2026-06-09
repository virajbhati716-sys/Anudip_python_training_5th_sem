emp_id = input("Enter Employee ID: ")

# 1. Count uppercase letters
upper_count = 0
for ch in emp_id:
    if ch.isupper():
        upper_count += 1

# 2. Count digits
digit_count = 0
digit_list = []

for ch in emp_id:
    if ch.isdigit():
        digit_count += 1
        digit_list.append(int(ch))

# 3. Extract joining year
year = emp_id[3:7]

# 4. Extract employee name
name = emp_id[7:-3]

# 5. Validation
valid = True

if not emp_id.startswith("EMP"):
    valid = False

if len(year) != 4 or not year.isdigit():
    valid = False

if len(emp_id[-3:]) != 3 or not emp_id[-3:].isdigit():
    valid = False

# 6 & 7. Digit list and sum of digits
digit_sum = sum(digit_list)

# 8. Display results
print("\nEmployee ID:", emp_id)

print("\nUppercase Letters:", upper_count)
print("Digits:", digit_count)

print("\nJoining Year:", year)
print("Employee Name:", name)

print("\nDigit List:", digit_list)
print("Sum of Digits:", digit_sum)

if valid:
    print("\nID Status: Valid")
else:
    print("\nID Status: Invalid")