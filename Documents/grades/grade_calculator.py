# Galvez, Mitchie T.
# List to store subjects and grades
grade_calculator = []

# User input
subjects = int(input("Enter the number of subjects: "))
while subjects <= 0:
    print("Number of subjects must be greater than 0.")
    subjects = int(input("Enter the number of subjects: "))

for i in range(subjects):
    subject_name = input(f"Enter the name of subject {i+1}: ")
    grade = float(input(f"Enter the grade for {subject_name}: "))

# Check if grade is valid (0 to 100 only)
    while grade < 0 or grade > 100:
        print("Invalid grade. 0 to 100 only.")
        grade = float(input(f"Enter the grade for {subject_name}: "))

    grade_calculator.append((subject_name, grade))

# Calculate average grade
average_grade = sum(grade for subject, grade in grade_calculator) / len(grade_calculator)

print(f"Average Grade: {average_grade:.2f}")

# Determine result
if average_grade >= 95:
    print("LATIN HONORS")
elif average_grade >= 75:
    print("PASSED")
else:
    print("FAILED")