
print("----------------Day 2 Exersice----------------")

two_digit_num = input("Please enter two digit number: ")
first_num = int(two_digit_num[0])
second_num = int(two_digit_num[1])
print(first_num + second_num)

print("----------------Day 2 BMI Calculator----------------")
height = float(input("whats your hight in meter? "))
weight = float(input("whats your weight in Kg's? "))
calculatedBMI = str(int(weight/(height**2)))
print("Calculated BMI is " + calculatedBMI)

print("Testing Day 2 branch in GIT")
print("-----Day 2 Life in week challenge -------")
total_days = 90*365
total_weeks = 90*52
total_months = 90 * 12
age = int(input("What is your current age? "))
days_lived = age * 365
weeks_lived = age * 52
months_lived = age*12

days_to_live = total_days - days_lived
weeks_to_live = total_weeks - weeks_lived
months_to_live = total_months - months_lived
print(
    f"You have {days_to_live} days, {weeks_to_live} weeks & {months_to_live} months left to live")

print("\n-------------------Day 2 Final Tip calculator challenge----------------------\n")
amount = float(input("Amount to pay:  $"))
tip = float(input("How much tip do you prefer in %?: "))
people = float(input("How many people to divide with?:     "))
tip_amount = ((amount * tip)/100)/people
individual_cost = amount/people
total_per_person = tip_amount+individual_cost
print("Each person would pay: " + str(total_per_person))
print("\n-------------Thank you - Day 2 complete-------------")
