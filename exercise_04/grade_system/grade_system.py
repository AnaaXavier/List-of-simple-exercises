def calculate_GPA(total_grades):
    return total_grades / 5

total_grades = 0
assignment_count = 1

try:
    while assignment_count <= 5:
        user_grades_input = float(input(f"Enter the {assignment_count}º grade: "))
        
        if user_grades_input < 0 or user_grades_input > 10:
            print(f"\033[93mThe grades must be between 1 and 10!\033[0m")
            continue

        total_grades += user_grades_input
        assignment_count += 1

    gpa = calculate_GPA(total_grades)
    
    if gpa >= 6 and gpa < 10:
        print(f"\033[92mYour GPA is: {gpa}. You are approved!\033[0m")
        
    else:
        print(f"\033[91mYour GPA is: {gpa}. You are not approved.\033[0m")

except ValueError as e:
    print(f"\033[93mAn error occurred: {e}. Please, enter any number that is not zero and do not leave the input empty/null!\033[0m")