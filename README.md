# Student Grade Management System

A command-line application written in Python for managing student records and grades. This project was developed as the final project for **Harvard University's CS50's Introduction to Programming with Python (CS50P)**.

## Features

- Add new students
- Add grades to existing students
- View all student records
- Search for students by name (case-insensitive)
- Generate student reports with averages and letter grades
- Delete student records
- Persistent data storage using CSV

## Grading System

| Average | Grade |
|---------:|:-----:|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

Students without grades are displayed as **N/A**.

## Technologies Used

- Python 3
- CSV module (built-in)
- Pytest

## Project Structure

```
Student-Grade-Management-System/
│
├── project.py
├── test_project.py
├── students.csv
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/student-grade-management-system.git
```

Move into the project directory:

```bash
cd student-grade-management-system
```

## Running the Program

```bash
python project.py
```

## Running the Tests

```bash
pytest test_project.py
```

## Project Design

Student records are stored in a CSV file (`students.csv`), allowing data to persist between program runs. Each record contains the student's name and a list of grades.

The application is organised into separate functions, including:

- `main()`
- `load_students()`
- `save_students()`
- `add_student()`
- `add_grade()`
- `view_students()`
- `search_student()`
- `show_averages()`
- `delete_student()`
- `calculate_average()`
- `get_letter_grade()`

This modular structure improves readability, maintainability, and testing.

## Requirements

The project uses only Python's built-in `csv` module and therefore does not require any third-party packages. The included `requirements.txt` file is intentionally empty.

## Video Demonstration

**Video Demo:** *(Add your YouTube link here)*

## Author

**Subhradeep Chandra**

Final Project for **CS50's Introduction to Programming with Python (CS50P)**.
