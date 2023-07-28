students = []

def add_student():
    student = {}
    student['name'] = input("Enter student name: ")
    student['age'] = int(input("Enter student age: "))
    student['country'] = input("Enter student country: ")
    student['city'] = input("Enter student city: ")
    student['job'] = input("Enter student job: ")
    student['skills'] = input("Enter student skills: ")
    student['parent'] = input("Enter student parent: ")
    students.append(student)

def print_students():
    for student in students:
        print("Name:", student['name'])
        print("Age:", student['age'])
        print("Country:", student['country'])
        print("City:", student['city'])
        print("Job:", student['job'])
        print("Skills:", student['skills'])
        print("Parent:", student['parent'])
        print()

while True:
    choice = input("Do you want to add a new student? (yes/no): ")
    if choice.lower() == 'yes':
        add_student()
    elif choice.lower() == 'no':
        print("Student Data:")
        print_students()
        break
    else:
        print("Invalid choice! Please enter 'yes' or 'no'.")