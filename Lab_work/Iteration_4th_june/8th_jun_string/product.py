review = "This product is excellent excellent excellent and very useful"

# Convert review into list of words
words = review.split()

# 1. Count total words
total_words = len(words)

# 2. Create dictionary containing word frequencies
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# 3. Find most frequently used word
max_count = 0
most_frequent = ""

for word in frequency:
    if frequency[word] > max_count:
        max_count = frequency[word]
        most_frequent = word

# 4. Find words appearing only once
once_words = []

for word in frequency:
    if frequency[word] == 1:
        once_words.append(word)

# 5. Count words having more than 5 characters
count_long = 0

for word in words:
    if len(word) > 5:
        count_long += 1

# 6. Display words in reverse order
reverse_words = words[::-1]

# 7. Create a list of unique words
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

# Display Results
print("Total Words:", total_words)

print("\nWord Frequencies:")
for word, count in frequency.items():
    print(word, "->", count)

print("\nMost Frequent Word:", most_frequent)

print("\nWords Appearing Once:")
print(once_words)

print("\nWords Having More Than 5 Characters:", count_long)

print("\nWords in Reverse Order:")
print(reverse_words)

print("\nUnique Words:")
print(unique_words)