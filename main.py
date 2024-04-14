import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Correct guesses: {len(guessed_states)}/50", prompt="Enter the name of a state").title()

    if answer_state == "Exit":
        un_guessed_states = []
        for state in state_list:
            if state not in guessed_states:
                un_guessed_states.append(state)
        new_data = pandas.DataFrame(un_guessed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        answer_turtle = turtle.Turtle()
        answer_turtle.hideturtle()
        answer_turtle.penup()
        state_data = data[data.state == answer_state]
        answer_turtle.goto(int(state_data.x), int(state_data.y))
        answer_turtle.write(answer_state)
        guessed_states.append(answer_state)
