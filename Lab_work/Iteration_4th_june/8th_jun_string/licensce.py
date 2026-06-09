license_key = input("Enter License Key: ")

# 1 & 6. Create a list containing all groups
groups = license_key.split("-")

# Verify groups
valid = True

# Check exactly 4 groups
if len(groups) != 4:
    valid = False

# Check each group contains exactly 4 characters
for group in groups:
    if len(group) != 4:
        valid = False

# 3. Count total letters
total_letters = 0
for ch in license_key:
    if ch.isalpha():
        total_letters += 1

# 4. Count vowels
vowels = 0
for ch in license_key:
    if ch.upper() in "AEIOU":
        vowels += 1

# 5. Remove hyphens and display merged key
merged_key = license_key.replace("-", "")

# Display Results
print("\nLicense Key:")
print(license_key)

print("\nGroups:")
print(groups)

print("\nNumber of Groups:", len(groups))

print("\nTotal Letters:", total_letters)
print("Total Vowels:", vowels)

print("\nMerged Key:")
print(merged_key)

if valid:
    print("\nLicense Key Status: Valid")
else:
    print("\nLicense Key Status: Invalid")