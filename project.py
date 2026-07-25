import csv


def load_students():
    students = []

    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        pass

    return students


def save_students(students):
    with open("students.csv", "w", newline="") as file:
        fieldnames = ["name", "grades"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for student in students:
            writer.writerow(student)


def add_student():
    students = load_students()

    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student already exists.")
            return

    students.append({
        "name": name,
        "grades": ""
    })

    save_students(students)
    print("Student added successfully!")


def add_grade():
    students = load_students()

    if len(students) == 0:
        print("No students found.")
        return

    name = input("Enter student name: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():

            while True:
                try:
                    grade = int(input("Enter grade (0-100): "))

                    if 0 <= grade <= 100:
                        break
                    else:
                        print("Grade must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

            if student["grades"] == "":
                student["grades"] = str(grade)
            else:
                student["grades"] += "," + str(grade)

            save_students(students)
            print("Grade added successfully!")
            return

    print("Student not found.")


def view_students():
    students = load_students()

    if len(students) == 0:
        print("No students found.")
        return

    print("\n===== Students =====")

    for student in students:
        print(f"\nName: {student['name']}")

        if student["grades"] == "":
            print("Grades: None")
        else:
            print(f"Grades: {student['grades']}")


def calculate_average(grades):
    if grades == "":
        return None

    grades = grades.split(",")
    grades = [int(grade) for grade in grades]

    return sum(grades) / len(grades)


def get_letter_grade(average):
    if average is None:
        return "N/A"
    elif average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def show_averages():
    students = load_students()

    if len(students) == 0:
        print("No students found.")
        return

    print("\n===== Student Report =====")

    for student in students:
        average = calculate_average(student["grades"])
        letter = get_letter_grade(average)

        print(f"\nName: {student['name']}")

        if average is None:
            print("Grades: None")
            print("Average: N/A")
            print("Letter Grade: N/A")
        else:
            print(f"Grades: {student['grades']}")
            print(f"Average: {average:.2f}")
            print(f"Letter Grade: {letter}")


def search_student():
    students = load_students()

    if len(students) == 0:
        print("No students found.")
        return

    name = input("Enter student name: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():

            average = calculate_average(student["grades"])
            letter = get_letter_grade(average)

            print("\n===== Student Details =====")
            print(f"Name: {student['name']}")

            if average is None:
                print("Grades: None")
                print("Average: N/A")
                print("Letter Grade: N/A")
            else:
                print(f"Grades: {student['grades']}")
                print(f"Average: {average:.2f}")
                print(f"Letter Grade: {letter}")

            return

    print("Student not found.")


def delete_student():
    students = load_students()

    if len(students) == 0:
        print("No students found.")
        return

    name = input("Enter student name to delete: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def main():
    while True:
        print("\n===== Student Grade Management System =====")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Students")
        print("4. Search Student")
        print("5. Show Student Report")
        print("6. Delete Student")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            add_grade()

        elif choice == "3":
            view_students()

        elif choice == "4":
            search_student()

        elif choice == "5":
            show_averages()

        elif choice == "6":
            delete_student()

        elif choice == "7":
            print("Thank you for using Student Grade Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
