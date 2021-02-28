student_scores = input("Enter students scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_number = 0
for number in student_scores:
    if number > highest_number:
        highest_number = number

print(f"{highest_number} is the highest number in the list")
