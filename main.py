import turtle
from turtle import Turtle
import pandas
data = pandas.read_csv("50_states.csv")


screen = turtle.Screen()


screen.title("U.S. States Game")
image = "blank_states_img.gif"

state = data.state
state_list = state.to_list()
list2 = state.to_list()
cor = []



screen.addshape(image)
turtle.shape(image)

while len(cor) < 50:


    answer_state = screen.textinput(title = f"{len(cor)}/50correct state", prompt= " What's another state name").title()
    if answer_state == "Exit":
        dum = [n for n in cor if n not in state_list]
        new_data = pandas.DataFrame(dum)
        new_data.to_csv("missedstate.csv")
        print(f"{dum} are the missed states")
        break
    if answer_state in state_list:
        cor.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)






screen.exitonclick()