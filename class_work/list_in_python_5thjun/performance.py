# Student Performance Analyzer

marks = [78, 45, 92, 35, 88, 40, 99, 56]

# 1. Display passed students
passed = []
for m in marks:
    if m >= 40:
        passed.append(m)

# 2. Count failed students
failed_count = 0
for m in marks:
    if m < 40:
        failed_count += 1

# 3. Find highest and lowest marks without max() and min()
highest = marks[0]
lowest = marks[0]

for m in marks:
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m

# 4. Create merit list (marks above 75)
merit_list = []
for m in marks:
    if m > 75:
        merit_list.append(m)

# Display results
print("Passed Students:", passed)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit_list)