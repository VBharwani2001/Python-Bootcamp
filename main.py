amount = 0
amount = input("Amount to pay:  ")
tip = 0
tip = input("How much tip do you prefer?: ")
people = input("Howmany people to divide with?:     ")
tip_amount = 0
tip_amount = (amount * tip)/100
individual_cost = amount/people
total_per_person = tip_amount+individual_cost
print("Each person would pay: " + total_per_person)
