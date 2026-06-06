# Online Quiz Evaluation

correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

# 1. Calculate score
score = 0
wrong = 0

print("Incorrectly Answered Question Numbers:")

for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1
    else:
        wrong += 1
        print(i + 1)

# 2. Count correct and wrong answers
print("\nCorrect Answers:", score)
print("Wrong Answers:", wrong)

# 3. Calculate percentage
percentage = (score / len(correct)) * 100

print("Score:", score, "out of", len(correct))
print("Percentage:", percentage, "%")

# 4. Determine Pass/Fail
if percentage >= 60:
    print("Result: Pass")
else:
    print("Result: Fail")