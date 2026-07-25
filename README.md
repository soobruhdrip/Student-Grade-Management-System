# Student Grade Management System

#### Video Demo: [Link](https://www.youtube.com/watch?v=H8w9U7698Bs)

#### Description:

The Student Grade Management System is a command-line application written in Python that allows users to manage student records and grades. This project was created as my final project for CS50's Introduction to Programming with Python. The goal of the project is to provide a simple and organized way to store, update, and view student information while demonstrating the Python concepts learned throughout the course.

The program stores student information in a CSV file named `students.csv`. Each student record contains the student's name and a list of grades. Using a CSV file allows the data to remain saved even after the program is closed, making the project more practical than storing data only in memory.

When the program starts, the user is presented with a menu containing the following options:

- Add Student
- Add Grade
- View Students
- Search Student
- Show Student Report
- Delete Student
- Exit

The Add Student feature allows the user to create a new student record. The program checks that the name is not empty and prevents duplicate student names.
The Add Grade feature lets the user add one or more grades to an existing student. Every grade is validated to ensure it is an integer between 0 and 100.
The View Students feature displays every student currently saved along with their grades. If a student has no grades yet, the program displays "None."
The Search Student feature searches for a student by name, ignoring uppercase and lowercase differences. It displays the student's grades, average score, and letter grade.

The Student Report feature calculates each student's average grade and converts it into a letter grade using the following grading system:

- A: 90–100
- B: 80–89
- C: 70–79
- D: 60–69
- F: Below 60

Students without grades are displayed as "N/A."

The Delete Student feature permanently removes a student from the CSV file.
The project is organized into multiple functions. The `main()` function controls the menu, while other functions such as `load_students()`, `save_students()`, `add_student()`, `add_grade()`, `view_students()`, `search_student()`, `show_averages()`, `delete_student()`, `calculate_average()`, and `get_letter_grade()` each perform one specific task. Separating the program into functions makes the code easier to read, test, and maintain.

The project also includes `test_project.py`, which contains automated tests written using `pytest`. These tests verify the correctness of important functions, including calculating averages, assigning letter grades, and loading student data.

### Requirements

This project uses only Python's built-in `csv` module and does not require any third-party packages. Therefore, the accompanying `requirements.txt` file is intentionally empty.
Overall, this project demonstrates many of the concepts learned throughout CS50P, including functions, loops, conditionals, file handling, exception handling, lists, dictionaries, user input validation, and automated testing with `pytest`.
