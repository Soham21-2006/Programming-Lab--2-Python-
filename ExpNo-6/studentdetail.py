student = {
    "name": "Soham",
    "roll_no": 101,
    "class": "SYBtech",
    "age": 18,
    "marks": {
        "Math": 85,
        "Science": 90,
        "English": 78
    }
}

print("Student Details:")
for key, value in student.items():
    print(key, ":", value)