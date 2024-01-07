from turtle import Screen
import pandas as pd

from write import Write

IMAGE = "Resource/india.gif"
STATES = "states.csv"
screen = Screen()
screen.setup(width=500, height=550)
screen.bgpic(IMAGE)
screen.title("INDIA")
df = pd.read_csv(STATES)
state_list = df["State Name"].to_list()
capital_list = df["Capital"].to_list()
states_user_guessed = []
pen = Write()
# x = screen.textinput(title="Input", prompt="Enter a sate name")
game_on = True
while game_on:
    user_input = screen.textinput(title=f"{len(states_user_guessed)}/36 States and UT Correct",
                                  prompt="Enter a State/UT name").lower()
    if user_input == "exit" or user_input == "quit" or user_input == "help":
        pen.screen_write(text=f"{len(states_user_guessed)}/50 states correct", x=0, y=0)
        game_on = False

    if user_input.title() in state_list:
        states_user_guessed.append(user_input)
        state_info = df[df["State Name"] == user_input.title()]
        state_capital = state_info["Capital"].to_list()[0]
        pen.screen_write(text=f"{user_input.title()}\n C: {state_capital}", x=int(state_info.x), y=int(state_info.y))

screen.exitonclick()
