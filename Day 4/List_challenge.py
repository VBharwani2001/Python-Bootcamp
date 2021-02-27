import random
print("--------------DAY 4 List challenge----------")
names_in_group = input("Please give the name of people on the table:\n")
names = names_in_group.split(", ")
name_paying = random.randint(0, (len(names) - 1))
print(f"{names[name_paying]} is paying todays bill")
