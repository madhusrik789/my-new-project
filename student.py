
# Student Marks Calculator
# Variables and data
student_name = "Rahul"
marks = [85, 78, 92, 88, 75]
total = 0
# Loop to calculate total
for mark in marks:
    total = total + mark
# Arithmetic operations
average = total / len(marks)
percentage = (total / 500) * 100
# Display results
print("Student Name:", student_name)
print("Marks:", marks)
print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage)
# Conditional statement
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
else:
    print("Grade: C")
    print("remarks: needs improvements")