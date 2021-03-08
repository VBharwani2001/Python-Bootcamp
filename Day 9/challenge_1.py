student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    value = ""
    score = student_scores[key]
    if score > 90:
        value = "Outstanding"
    elif score > 80 and score < 91:
        value = "Exceeds Expectations"
    elif score > 70 and score < 81:
        value = "Acceptable"
    else:
        value = "Fail"

    student_grades[key] = value


# 🚨 Don't change the code below 👇
print(student_grades)
