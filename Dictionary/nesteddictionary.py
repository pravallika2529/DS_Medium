# Store student details using nested dictionaries
# Find the student with the highest marks

students = {
    "101": {
        "name": "Pravallika",
        "age": 19,
        "marks": 95
    },
    "102": {
        "name": "Lahari",
        "age": 19,
        "marks": 88
    },
    "103": {
        "name": "Manasvi",
        "age": 19,
        "marks": 100
    }
}

max_marks = -1
top_student = ""

for roll_no, details in students.items():
    if details["marks"] > max_marks:
        max_marks = details["marks"]
        top_student = details["name"]

print("Student with highest marks:", top_student)
print("Marks:", max_marks)
