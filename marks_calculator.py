"""
Student Marks Calculator
------------------------
- Accepts the student's name and marks in three subjects.
- Calculates total, average and percentage.
- Displays PASS / FAIL based on the passing rule below.

Passing rule:
    A student PASSES only if
      1. marks in EACH subject are at least 40, AND
      2. overall percentage is at least 40.
    Otherwise the student FAILS.
"""

MAX_MARKS_PER_SUBJECT = 100
PASS_MARKS_PER_SUBJECT = 40
PASS_PERCENTAGE = 40.0
NUM_SUBJECTS = 3


def get_name():
    """Ask for a non-empty student name."""
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("  Name cannot be empty. Please try again.")


def get_marks(subject_number):
    """Ask for marks of one subject and validate (0 to MAX_MARKS_PER_SUBJECT)."""
    while True:
        raw = input(f"Enter marks for Subject {subject_number} (0-{MAX_MARKS_PER_SUBJECT}): ").strip()
        try:
            marks = float(raw)
        except ValueError:
            print("  Invalid input. Please enter a number.")
            continue
        if 0 <= marks <= MAX_MARKS_PER_SUBJECT:
            return marks
        print(f"  Marks must be between 0 and {MAX_MARKS_PER_SUBJECT}.")


def calculate_results(marks_list):
    """Return total, average and percentage for the given marks."""
    total = sum(marks_list)
    average = total / len(marks_list)
    percentage = (total / (len(marks_list) * MAX_MARKS_PER_SUBJECT)) * 100
    return total, average, percentage


def is_pass(marks_list, percentage):
    """Apply the passing rule."""
    all_subjects_passed = all(m >= PASS_MARKS_PER_SUBJECT for m in marks_list)
    return all_subjects_passed and percentage >= PASS_PERCENTAGE


def display_report(name, marks_list, total, average, percentage, passed):
    """Print the result sheet."""
    line = "=" * 40
    print("\n" + line)
    print("          STUDENT MARKS REPORT")
    print(line)
    print(f"Name        : {name}")
    for i, m in enumerate(marks_list, start=1):
        print(f"Subject {i}   : {m:g}")
    print("-" * 40)
    print(f"Total       : {total:g} / {len(marks_list) * MAX_MARKS_PER_SUBJECT}")
    print(f"Average     : {average:.2f}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Status      : {'PASS' if passed else 'FAIL'}")
    print(line)
    print(
        f"Rule: at least {PASS_MARKS_PER_SUBJECT} in every subject "
        f"AND overall {PASS_PERCENTAGE:g}% or more."
    )
    print(line + "\n")


def main():
    print("=== Student Marks Calculator ===\n")
    while True:
        name = get_name()
        marks_list = [get_marks(i) for i in range(1, NUM_SUBJECTS + 1)]

        total, average, percentage = calculate_results(marks_list)
        passed = is_pass(marks_list, percentage)
        display_report(name, marks_list, total, average, percentage, passed)

        again = input("Calculate for another student? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you! Goodbye.")
            break
        print()


if __name__ == "__main__":
    main()
