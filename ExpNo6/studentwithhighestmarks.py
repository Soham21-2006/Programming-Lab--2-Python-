# Dictionary of students and marks
students = {"Amit": 85, "Soham": 92, "Riya": 88}
# Find student with highest marks
top_student = max(students, key=students.get)
# Display result
print("Top Student:", top_student)
print("Marks:", students[top_student])