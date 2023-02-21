import turtle
import pandas
from navigator import Navigator

screen = turtle.Screen()
screen.setup(730, 500)
screen.title("STATES GUESSING GAME")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
t = Navigator()

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

guessed_state = []
while len(guessed_state) < 50:
    answer = screen.textinput(f"{len(guessed_state)}/50 States Correct", "What's the State Name").title()
    if answer == "Exit":
        states_to_learn = [state for state in state_list if state not in guessed_state]

        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("States_to_learn.csv")
        break
    for states in state_list:
        if answer == states:
            guessed_state.append(answer)
            state_data = data[data.state == answer]
            t.new_turtle(states, int(state_data.x), int(state_data.y))
