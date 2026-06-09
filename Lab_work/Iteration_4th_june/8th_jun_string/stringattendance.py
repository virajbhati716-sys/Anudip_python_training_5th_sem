attendance = "PPAPPPAAPPPPAPP"

# 1. Count Present and Absent days
present = attendance.count("P")
absent = attendance.count("A")

# 2. Calculate attendance percentage
total_days = len(attendance)
percentage = (present / total_days) * 100

# 3. Find longest consecutive streak of Presence
current_p = 0
longest_p = 0

for ch in attendance:
    if ch == "P":
        current_p += 1
        if current_p > longest_p:
            longest_p = current_p
    else:
        current_p = 0

# 4. Find longest consecutive streak of Absence
current_a = 0
longest_a = 0

for ch in attendance:
    if ch == "A":
        current_a += 1
        if current_a > longest_a:
            longest_a = current_a
    else:
        current_a = 0

# 5. Check attendance status
if percentage < 75:
    status = "Below 75%"
else:
    status = "75% or Above"

# Display Results
print("Attendance Record:")
print(attendance)

print("\nPresent Days:", present)
print("Absent Days:", absent)

print("\nAttendance Percentage:", round(percentage, 2), "%")

print("\nLongest Present Streak:", longest_p)
print("Longest Absent Streak:", longest_a)

print("\nAttendance Status:", status)