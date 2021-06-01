import turtle
import pandas

# panda library to read csv
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

# create screen and add shape of image for turtle
screen = turtle.Screen()
screen.title("US states")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

guessed_states = []
while len(guessed_states) < 50:
    answer = turtle.textinput(title=f"{len(guessed_states)}/50",
                              prompt=f"{len(guessed_states)}/50 Guessed \nWhat is the other states name?")
    answer = answer.title()
    print(answer)
    if answer == "Exit":
        break
    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        guessed_states.append(answer)
    else:
        print("no such state found")

for i in range(len(guessed_states)):
    all_states.remove(guessed_states[i])

pandas.DataFrame(all_states).to_csv("states_need_to_be_remember.csv")
