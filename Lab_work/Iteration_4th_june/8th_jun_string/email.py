email = input("Enter Email Address: ")

# 1. Extract username
username = email.split("@")[0]

# 2. Extract domain name
domain = email.split("@")[1].split(".")[0]

# 3. Extract extension
extension = email.split(".")[-1]

# 4. Count digits in username
digit_count = 0
for ch in username:
    if ch.isdigit():
        digit_count += 1

# 5. Count special characters
special_count = 0
for ch in email:
    if not ch.isalnum() and ch != "@":
        special_count += 1

# 6. Validate email
valid = True

# Check exactly one @
if email.count("@") != 1:
    valid = False

# Check at least one . after @
elif "." not in email.split("@")[1]:
    valid = False

# Display results
print("\nEmail:", email)

print("\nUsername:", username)
print("Domain:", domain)
print("Extension:", extension)

print("\nDigits Found:", digit_count)
print("Special Characters Found:", special_count)

if valid:
    print("\nEmail Status: Valid")
else:
    print("\nEmail Status: Invalid")