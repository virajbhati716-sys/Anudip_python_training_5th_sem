FILE_NAME = "marks.txt"


# Load student records from file
def load_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                sid, name, marks = line.strip().split(",")
                students.append([sid, name, int(marks)])
    except FileNotFoundError:
        print("marks.txt not found!")

    return students


# Calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


# Generate report card file
def generate_report(students):
    with open("report_card.txt", "w") as file:
        file.write("ID,Name,Marks,Grade\n")

        for sid, name, marks in students:
            grade = calculate_grade(marks)
            file.write(f"{sid},{name},{marks},{grade}\n")

    print("Report Cards Generated Successfully")


# Display topper
def display_topper(students):
    topper = students[0]

    for student in students:
        if student[2] > topper[2]:
            topper = student

    print("\nTopper:")
    print(f"{topper[1]} ({topper[2]})")


# Count pass and fail students
def count_pass_fail(students):
    passed = 0
    failed = 0

    for sid, name, marks in students:
        if marks >= 40:
            passed += 1
        else:
            failed += 1

    print("\nPassed Students:", passed)
    print("Failed Students:", failed)


# Display merit certificate holders
def merit_students(students):
    print("\nMerit Certificate Holders:")

    for sid, name, marks in students:
        if marks >= 90:
            print(name)


# Main Program
students = load_students()

display_topper(students)
count_pass_fail(students)
merit_students(students)
generate_report(students)