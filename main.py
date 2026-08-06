# ==================================================
# PREPTRACK — BOILERPLATE CODE
# ==================================================

print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)

# --------------------------------------------------
# 1. COLLECT STUDENT DETAILS
# --------------------------------------------------

# Validate student name
while True:
    student_name = input("Enter student name: ").strip()
    if student_name != "":
        break
    print("Student name cannot be empty.")

registration_number = input("Enter registration number: ")

graduation_year = int(input("Enter graduation year: "))

# Validate attendance
while True:
    attendance = float(input("Enter attendance percentage: "))
    if 0 <= attendance <= 100:
        break
    print("Attendance should be between 0 and 100.")

# Accept only yes or no
while True:
    project_input = input(
        "Has the student completed the required project? Enter yes or no: "
    ).strip().lower()

    if project_input == "yes" or project_input == "no":
        break
    print("Please enter only yes or no.")

# Convert into Boolean
if project_input == "yes":
    project_completed = True
else:
    project_completed = False

# Accept only yes or no
while True:
    profile_input = input(
        "Is the student profile verified? Enter yes or no: "
    ).strip().lower()

    if profile_input == "yes" or profile_input == "no":
        break
    print("Please enter only yes or no.")

# Convert into Boolean
if profile_input == "yes":
    profile_verified = True
else:
    profile_verified = False


# --------------------------------------------------
# 2. INITIALIZE COUNTERS AND VARIABLES
# --------------------------------------------------

total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0


# --------------------------------------------------
# 3. PROCESS SEVEN PRACTICE DAYS
# --------------------------------------------------

for day in range(1, 8):

    # Accept only valid input
    while True:
        score = int(
            input(
                f"Enter Day {day} score from 0 to 100, "
                "or -1 for absent: "
            )
        )

        if score == -1 or (0 <= score <= 100):
            break

        print("Enter a valid score.")

    # Handle absence
    if score == -1:
        absent_days += 1
        continue

    # Increase counters
    attempted_days += 1
    total_score += score

    # Highest and Lowest score
    if not first_attempt_found:
        highest_score = score
        highest_score_day = day

        lowest_score = score
        lowest_score_day = day

        first_attempt_found = True

    else:
        if score > highest_score:
            highest_score = score
            highest_score_day = day

        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day

    # Classify score
    if 75 <= score <= 100:
        strong_days += 1

    elif 60 <= score <= 74:
        satisfactory_days += 1

    elif 40 <= score <= 59:
        improvement_days += 1

    else:
        critical_days += 1

        if not critical_score_found:
            critical_score_found = True
            first_critical_day = day
            first_critical_score = score

    # Pass and Fail
    if score >= 40:
        passed_days += 1
    else:
        failed_days += 1


# --------------------------------------------------
# 4. CALCULATE THE AVERAGE
# --------------------------------------------------

if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0


# --------------------------------------------------
# 5. CREATE ELIGIBILITY CONDITIONS
# --------------------------------------------------

graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027
)

attendance_eligible = attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)


# --------------------------------------------------
# 6. DETERMINE FINAL STATUS
# --------------------------------------------------

final_status = ""
primary_blocker = ""
next_action = ""

if attempted_days == 0:
    final_status = "Not Ready"
    primary_blocker = "No practice attempted"
    next_action = "Start solving practice questions."

elif critical_score_found:
    final_status = "Not Ready"
    primary_blocker = "Critical score found"
    next_action = "Improve weak topics and avoid critical scores."

elif attempted_days < 6:
    final_status = "Not Ready"
    primary_blocker = "Fewer than six practice attempts"
    next_action = "Complete at least six practice days."

elif passed_days < 4:
    final_status = "Not Ready"
    primary_blocker = "Fewer than four passed days"
    next_action = "Increase the number of passed practice days."

elif average_score < 70:
    final_status = "Not Ready"
    primary_blocker = "Average score below 70"
    next_action = "Improve your average score."

elif attendance < 75:
    final_status = "Not Ready"
    primary_blocker = "Attendance below 75%"
    next_action = "Improve your attendance."

elif not graduation_eligible:
    final_status = "Not Eligible"
    primary_blocker = "Graduation year not eligible"
    next_action = "Check placement eligibility criteria."

elif not project_completed:
    final_status = "Not Ready"
    primary_blocker = "Project not completed"
    next_action = "Complete the required project."

elif not profile_verified:
    final_status = "Not Ready"
    primary_blocker = "Profile not verified"
    next_action = "Verify your student profile."

elif placement_ready:
    final_status = "Ready for Mock Interview"
    primary_blocker = "None"
    next_action = "Attend the mock interview with confidence."


# --------------------------------------------------
# 7. DISPLAY FINAL REPORT
# --------------------------------------------------

print()
print("=" * 50)
print("              PREPTRACK REPORT")
print("=" * 50)

print(f"Student Name           : {student_name}")
print(f"Registration Number    : {registration_number}")
print(f"Graduation Year        : {graduation_year}")
print(f"Attendance             : {attendance}%")

print()
print(f"Attempted Days         : {attempted_days}")
print(f"Absent Days            : {absent_days}")
print(f"Passed Days            : {passed_days}")
print(f"Failed Days            : {failed_days}")

print()
print(f"Strong Days            : {strong_days}")
print(f"Satisfactory Days      : {satisfactory_days}")
print(f"Needs Improvement Days : {improvement_days}")
print(f"Critical Days          : {critical_days}")

print()
print(f"Total Score            : {total_score}")
print(f"Average Score          : {average_score:.2f}")

# Display highest and lowest only if practice attempted
if attempted_days > 0:
    print(f"Highest Score          : {highest_score} (Day {highest_score_day})")
    print(f"Lowest Score           : {lowest_score} (Day {lowest_score_day})")

# Display first critical score details
if critical_score_found:
    print(
        f"First Critical Score   : {first_critical_score} (Day {first_critical_day})"
    )

print()
print(f"Final Status           : {final_status}")
print(f"Primary Blocker        : {primary_blocker}")
print(f"Next Action            : {next_action}")

print("=" * 50)