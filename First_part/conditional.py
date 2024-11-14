BRANCHING AND DECISION MAKING 

# Get the student's score
score = int(input("Enter your score (0-100): "))

# Step 1: Using if statement

if score >= 90:
    print("Excellent! You've scored an A.")
    
# Step 2: Using if-else statement to check pass/fail

if score >= 50:
    print("You passed the exam.")
else:
    print("You failed the exam.")

    
# Step 3: Using if-elif-else statement for grade categorization

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Step 4: Nested if statement to check if the student needs improvement

if score < 50:
    print("You failed, but don't worry! You can improve with more practice.")
    if score < 30:
        print("Consider seeking extra help, your score is quite low.")
    else:
        print("You can pass with some effort, focus on areas of weakness.")
