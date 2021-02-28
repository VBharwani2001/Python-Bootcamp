student_heights = input("Enter students height: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
number = 0
for i in student_heights:
    total_height = total_height + i
    number += 1


average = round(total_height/number)
print(total_height)
print(average)
