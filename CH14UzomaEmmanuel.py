# Emmanuel Uzoma
# Date: April 9, 2025
# Program: CH14 Grade Counter
# Description:
# This program uses functions and a dictionary to collect students' names and
# their corresponding letter grades (A-F, case-insensitive). It counts how many
# students received each grade and then prints a formatted grade report.

# Constants for valid grade letters
VALID_GRADES = ['A', 'B', 'C', 'D', 'F']

def main():
    print("Welcome to the Letter Grade Counter Program!")
    gradebook = fillGradeBook()
    grade_counts = countGrades(gradebook)
    gradeReport(grade_counts)

def fillGradeBook():
    """Prompts user for number of students, gets names and grades, and fills the dictionary."""
    gradebook = {}
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students < 1:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    for i in range(1, num_students + 1):
        name = input(f"Enter name of student #{i}: ").strip()
        while True:
            grade = input(f"Enter letter grade for {name} (A-F): ").strip().upper()
            if grade in VALID_GRADES:
                break
            else:
                print("Invalid grade. Please enter A, B, C, D, or F.")
        gradebook[name] = grade

    return gradebook

def countGrades(gradebook):
    """Counts number of each letter grade and returns as a list [A, B, C, D, F]."""
    count_list = [0, 0, 0, 0, 0]  # Indices: 0=A, 1=B, 2=C, 3=D, 4=F

    for grade in gradebook.values():
        grade = grade.upper()
        if grade == 'A':
            count_list[0] += 1
        elif grade == 'B':
            count_list[1] += 1
        elif grade == 'C':
            count_list[2] += 1
        elif grade == 'D':
            count_list[3] += 1
        elif grade == 'F':
            count_list[4] += 1

    return count_list

def gradeReport(counts):
    """Prints the grade report."""
    print("\nGRADE REPORT")
    print(f"Number of A grades: {counts[0]}")
    print(f"Number of B grades: {counts[1]}")
    print(f"Number of C grades: {counts[2]}")
    print(f"Number of D grades: {counts[3]}")
    print(f"Number of F grades: {counts[4]}")

# Run the program
main()
