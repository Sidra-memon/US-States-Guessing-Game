import pandas
import turtle
# Load data
data = pandas.read_csv("50_states.csv")
# Set up the screen
sc = turtle.Screen()
sc.setup(600, 400)
sc.bgpic('blank_states_img.gif')
sc.update()
# List to store all guessed state names
guessed_states = []
# Game loop
game_on = True
while game_on:
    # Get user input
    state_name = turtle.textinput("State name", "Guess the state").title()
    # Append the guessed state to the list
    guessed_states.append(state_name)
    if state_name == "Exit":
        break
    # Check if the guessed state is correct and display it on the map
    start = data[data.state == state_name]
    if not start.empty:
        x = int(start.iloc[0].x)
        y = int(start.iloc[0].y)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x, y)
        turtle.write(state_name)
# Print all guessed states at the end of the game
y=guessed_states
print(y)
df = pandas.DataFrame(data)
state_list = data["state"].to_list()
# prints the missing and additional elements in list2
missing_states=list(set(state_list)-set(y))
# dg = pandas.DataFrame(z
# print(z)
sc.exitonclick()
# # Save the missing states to a CSV file
# create a Pandas DataFrame from the dictionary
# dict = {'States': missing_states}
dl = pandas.DataFrame(missing_states)
# write the DataFrame to a CSV file
dl.to_csv('State1.csv')

