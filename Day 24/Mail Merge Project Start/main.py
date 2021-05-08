#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
names =[]
with open('./../Mail Merge Project Start/Input/Names/invited_names.txt', "r") as data:
    names = data.readlines()
    print(names)

with open("./../Mail Merge Project Start/Input/Letters/starting_letter.txt") as data:
    message = data.read()
    for name in names:

        name = name.rstrip("\n")
        file = open(f"./Input/Names/invite_for_{name}.txt", "w")
        modified = message.replace("[name]", name)
        file.write(modified)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp