import json

# Load data
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except:
    students = []


def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_data()

    print("Student Added Successfully!")


def view_students():
    if len(students) == 0:
        print("No Students Found")
    else:
        print("\nStudent List")
        for student in students:
            print(student)


def search_student():
    name = input("Enter Student Name: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print(student)
            found = True

    if not found:
        print("Student Not Found")


def filter_course():
    course = input("Enter Course Name: ")

    found = False

    for student in students:
        if student["course"].lower() == course.lower():
            print(student)
            found = True

    if not found:
        print("No Student Found In This Course")


def delete_student():
    name = input("Enter Student Name To Delete: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            save_data()
            print("Student Deleted")
            return

    print("Student Not Found")


def generate_report():
    with open("report.txt", "w") as file:

        file.write("NayePankh Foundation Report\n")
        file.write("===========================\n\n")

        file.write(f"Total Students: {len(students)}\n\n")

        for student in students:
            file.write(
                f"Name: {student['name']} | "
                f"Age: {student['age']} | "
                f"Course: {student['course']}\n"
            )

    print("Report Generated Successfully!")


while True:

    print("\n===== NayePankh Foundation =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Filter By Course")
    print("5. Delete Student")
    print("6. Generate Report")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        filter_course()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        generate_report()

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")