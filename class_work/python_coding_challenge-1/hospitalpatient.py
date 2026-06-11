# Function to display all patient records
def display_records():
    print("All Patient Records:")
    with open("patients.txt", "r") as file:
        for line in file:
            print(line.strip())


# Function to display critical patients
def display_critical_patients():
    print("\nCritical Patients:")
    with open("patients.txt", "r") as file:
        for line in file:
            pid, name, status = line.strip().split(",")
            if status == "Critical":
                print(name)


# Function to count patients under each status
def count_patients():
    normal = 0
    stable = 0
    critical = 0

    with open("patients.txt", "r") as file:
        for line in file:
            pid, name, status = line.strip().split(",")

            if status == "Normal":
                normal += 1
            elif status == "Stable":
                stable += 1
            elif status == "Critical":
                critical += 1

    print("\nPatient Count:")
    print("Normal :", normal)
    print("Stable :", stable)
    print("Critical :", critical)


# Function to search patient by ID
def search_patient(patient_id):
    found = False

    with open("patients.txt", "r") as file:
        for line in file:
            pid, name, status = line.strip().split(",")

            if pid == patient_id:
                print("\nPatient Found:")
                print(line.strip())
                found = True
                break

    if not found:
        print("\nPatient not found.")


# Function to save critical patients in another file
def save_critical_patients():
    with open("patients.txt", "r") as file, open("critical_patients.txt", "w") as outfile:
        for line in file:
            pid, name, status = line.strip().split(",")

            if status == "Critical":
                outfile.write(line)

    print("\nCritical Patient Report Generated Successfully")


# Main Program
display_records()
display_critical_patients()
count_patients()

patient_id = input("\nEnter Patient ID to search: ")
search_patient(patient_id)

save_critical_patients()
            
