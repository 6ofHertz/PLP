
#Control flow example for grading students marks.
#Asks for user input and grade student's performance

#Prompt user 4 marks.
marks = int(input("Enter the student's marks (0-100):"))

#Grading system based on the marks
if marks > 70:
    print("Grade: Distinction")
elif marks >=60:
    print("Grade: Credit")
elif marks >=50:
    print("Pass")
else:
    print("Grade: Fail")