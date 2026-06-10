file = open("data.txt", "r")

content = file.read()

# Count vowels
vowels = 0
for ch in content.lower():
    if ch in "aeiou":
        vowels += 1

# Count characters
characters = len(content)

# Count lines
lines = content.count("\n") + 1

print("Number of vowels =", vowels)
print("Number of characters =", characters)
print("Number of lines =", lines)

file.close()
