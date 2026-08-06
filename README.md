# preptrack-nagaraj
# PrepTrack – Placement Preparation Performance Analyzer

## Project Overview

PrepTrack is a Python-based console application developed to analyze a student's placement preparation performance. The application collects student information such as attendance, project completion status, profile verification status, and seven days of practice scores. It processes the collected data, performs various performance analyses, and finally determines whether the student is ready for a mock interview or identifies the primary reason they are not placement-ready.

---

## Features Implemented

- Student profile input
- Student name validation
- Attendance percentage validation
- Yes/No input validation for project completion
- Yes/No input validation for profile verification
- Seven-day practice score processing
- Absent day handling
- Score classification into:
  - Strong
  - Satisfactory
  - Needs Improvement
  - Critical
- Passed and failed day counting
- Highest score detection
- Lowest score detection
- First critical score detection
- Total score calculation
- Average score calculation
- Placement readiness evaluation
- Final status generation
- Primary blocker identification
- Next action recommendation
- Detailed performance report generation

---

## Python Concepts Used

The project uses the following Python concepts:

- Variables
- Data Types
- Input and Output
- Conditional Statements (if, elif, else)
- Loops (for and while)
- Boolean Values
- Comparison Operators
- Logical Operators
- Arithmetic Operators
- Input Validation
- Counters
- String Methods
- Nested Conditions
- Continue Statement
- Formatted Output using f-strings

---

## How to Run

Clone the repository and navigate to the project folder.

Run the program using:

```bash
python main.py
```

If your system uses Python 3 separately, run:

```bash
python3 main.py
```

Follow the on-screen instructions and enter the required details.

---

## Test Result Summary

The application was tested using different input combinations to verify its correctness.

The following scenarios were tested:

- Valid student details
- Empty student name
- Invalid attendance values
- Invalid Yes/No inputs
- Student absent for some practice days
- Student with critical scores
- Student with low average score
- Student with insufficient passed days
- Student with incomplete project
- Student with unverified profile
- Placement-ready student

All validations, calculations, classifications, and final status generation worked as expected.

---

## Individual Contribution

**Name:** Nagaraj Dharmadas

**Repository URL:**
(https://github.com/nagaraj-d0/preptrack-nagaraj.git)

**My Main Contribution:**

Developed the complete PrepTrack application for analyzing student placement preparation performance. Implemented input validation, score processing, placement eligibility checking, and report generation.

**Features I Implemented:**

- Student profile input
- Student name validation
- Attendance validation
- Yes/No validation
- Practice score validation
- Seven-day score processing
- Score classification
- Pass and fail counting
- Highest and lowest score detection
- Critical score detection
- Average score calculation
- Placement readiness evaluation
- Final report generation

**Python Concepts I Used:**

- Variables
- Loops
- Conditional Statements
- Boolean Logic
- Input Validation
- Arithmetic Operations
- Comparison Operators
- Logical Operators
- Counters
- String Handling
- f-Strings

**Most Difficult Logic:**

Implementing the placement readiness evaluation by checking multiple eligibility conditions in the correct priority order while ensuring only the first major blocker is displayed in the final report.

**Problem I Faced:**

Handling user input validation correctly while preventing invalid values from affecting the program flow and calculations.

**How I Solved It:**

I used while loops for continuous input validation and applied conditional statements to ensure only valid data was accepted before processing further.

---

## Code Review Completed

The project code was reviewed to improve readability, maintainability, and correctness.

The review included checking:

- Variable naming
- Code formatting
- Input validation
- Logic correctness
- Output formatting
- Readability

---

## Feedback Received

The following feedback was received during code review:

- Improve input validation.
- Make the code easier to read.
- Add meaningful comments.
- Display reports in a more organized format.
- Handle edge cases such as no practice attempts.

---

## Improvements Made After Review

Based on the feedback received, the following improvements were made:

- Added validation for empty student names.
- Added attendance range validation.
- Added validation for Yes/No inputs.
- Improved score validation.
- Added protection against division by zero.
- Improved report formatting.
- Displayed highest and lowest scores only when practice was attempted.
- Displayed first critical score only when applicable.
- Improved overall code readability using proper indentation and comments.