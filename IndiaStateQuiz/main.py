import turtle
import pandas
import random

# --------------------- Setup the Screen ---------------------
screen = turtle.Screen()
screen.title("India States Quiz")

# Original image size: 800x820
image_width = 800  # Width of the IndiaMap.gif
image_height = 820  # Height of the IndiaMap.gif
screen.setup(width=image_width, height=image_height)

# Register the map image
image = "IndiaMap.gif"
screen.addshape(image)
turtle.shape(image)

# --------------------- Load the Data ---------------------
try:
    data = pandas.read_csv("28_States.csv")
except FileNotFoundError:
    print("Error: '28_States.csv' file not found. Please ensure it is in the same directory as this script.")
    exit()

# Ensure that the CSV has the required columns
required_columns = {'state', 'x', 'y'}
if not required_columns.issubset(set(data.columns)):
    print(f"Error: '28_States.csv' must contain the columns: {required_columns}")
    exit()

all_states = data.state.to_list()
guessed_states = []

# --------------------- Hint System ---------------------
# Define hints for each state
state_hints = {
    "Jammuandkashmir": {
        "first_letter": "Starts with 'J'.",
        "letters_count": "Has 15 letters.",
        "region": "Located in Northern India."
    },
    "Ladakh": {
        "first_letter": "Starts with 'L'.",
        "letters_count": "Has 5 letters.",
        "region": "Located in Northern India."
    },
    # Add hints for all other states similarly
    "Himachalpradesh": {
        "first_letter": "Starts with 'H'.",
        "letters_count": "Has 15 letters.",
        "region": "Located in Northern India."
    },
    "Punjab": {
        "first_letter": "Starts with 'P'.",
        "letters_count": "Has 6 letters.",
        "region": "Located in Northern India."
    },
    "Uttarakhand": {
        "first_letter": "Starts with 'U'.",
        "letters_count": "Has 11 letters.",
        "region": "Located in Northern India."
    },
    "Haryana": {
        "first_letter": "Starts with 'H'.",
        "letters_count": "Has 7 letters.",
        "region": "Located in Northern India."
    },
    "Uttarpradesh": {
        "first_letter": "Starts with 'U'.",
        "letters_count": "Has 12 letters.",
        "region": "Located in Northern India."
    },
    "Rajasthan": {
        "first_letter": "Starts with 'R'.",
        "letters_count": "Has 9 letters.",
        "region": "Located in Northern India."
    },
    "Gujarat": {
        "first_letter": "Starts with 'G'.",
        "letters_count": "Has 7 letters.",
        "region": "Located in Western India."
    },
    "Madhyapradesh": {
        "first_letter": "Starts with 'M'.",
        "letters_count": "Has 14 letters.",
        "region": "Located in Central India."
    },
    "Bihar": {
        "first_letter": "Starts with 'B'.",
        "letters_count": "Has 5 letters.",
        "region": "Located in Eastern India."
    },
    "Jharkhand": {
        "first_letter": "Starts with 'J'.",
        "letters_count": "Has 9 letters.",
        "region": "Located in Eastern India."
    },
    "Westbengal": {
        "first_letter": "Starts with 'W'.",
        "letters_count": "Has 10 letters.",
        "region": "Located in Eastern India."
    },
    "Odisha": {
        "first_letter": "Starts with 'O'.",
        "letters_count": "Has 6 letters.",
        "region": "Located in Eastern India."
    },
    "Andhrapradesh": {
        "first_letter": "Starts with 'A'.",
        "letters_count": "Has 14 letters.",
        "region": "Located in Southern India."
    },
    "Telangana": {
        "first_letter": "Starts with 'T'.",
        "letters_count": "Has 9 letters.",
        "region": "Located in Southern India."
    },
    "Tamilnadu": {
        "first_letter": "Starts with 'T'.",
        "letters_count": "Has 9 letters.",
        "region": "Located in Southern India."
    },
    "Kerala": {
        "first_letter": "Starts with 'K'.",
        "letters_count": "Has 6 letters.",
        "region": "Located in Southern India."
    },
    "Karnataka": {
        "first_letter": "Starts with 'K'.",
        "letters_count": "Has 9 letters.",
        "region": "Located in Southern India."
    },
    "Maharasthra": {
        "first_letter": "Starts with 'M'.",
        "letters_count": "Has 11 letters.",
        "region": "Located in Western India."
    },
    "Chattisgarh": {
        "first_letter": "Starts with 'C'.",
        "letters_count": "Has 12 letters.",
        "region": "Located in Central India."
    },
    "Arunachalpradesh": {
        "first_letter": "Starts with 'A'.",
        "letters_count": "Has 17 letters.",
        "region": "Located in Northeastern India."
    },
    "Assam": {
        "first_letter": "Starts with 'A'.",
        "letters_count": "Has 5 letters.",
        "region": "Located in Northeastern India."
    },
    "Nagaland": {
        "first_letter": "Starts with 'N'.",
        "letters_count": "Has 8 letters.",
        "region": "Located in Northeastern India."
    },
    "Manipur": {
        "first_letter": "Starts with 'M'.",
        "letters_count": "Has 7 letters.",
        "region": "Located in Northeastern India."
    },
    "Mizoram": {
        "first_letter": "Starts with 'M'.",
        "letters_count": "Has 7 letters.",
        "region": "Located in Northeastern India."
    },
    "Tripura": {
        "first_letter": "Starts with 'T'.",
        "letters_count": "Has 7 letters.",
        "region": "Located in Northeastern India."
    },
    "Meghalaya": {
        "first_letter": "Starts with 'M'.",
        "letters_count": "Has 9 letters.",
        "region": "Located in Northeastern India."
    },
}

# Function to provide a random hint type for a given state
def give_hint(state_name):
    hints = state_hints.get(state_name, {})
    if not hints:
        return "No hints available for this state."
    hint_type = random.choice(list(hints.keys()))
    return f"Hint: {hints[hint_type]}"

# --------------------- Place State on Map ---------------------
def place_state(state_name):
    guessed_states.append(state_name)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == state_name]
    if not state_data.empty:
        try:
            x_coord = float(state_data.x.item())
            y_coord = float(state_data.y.item())
            t.goto(x_coord, y_coord)
            t.write(state_name, align="center", font=("Arial", 10, "normal"))
        except ValueError:
            print(f"Error: Invalid coordinates for {state_name}.")
    else:
        print(f"Error: Coordinates for {state_name} not found in the CSV.")

# --------------------- Main Game Loop ---------------------
while len(guessed_states) < len(all_states):
    # Prompt user for input
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{len(all_states)} States Correct",
        prompt="What's another state's name? Type 'Hint' for a clue or 'Exit' to quit."
    )

    if answer_state is None:
        # Treat closing the dialog as exit
        break

    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state == "Hint":
        # Provide a hint for a random unguessed state
        available_hints = [state for state in all_states if state not in guessed_states]
        if available_hints:
            hinted_state = random.choice(available_hints)
            hint = give_hint(hinted_state)
            user_response = screen.textinput(title="Hint", prompt=hint + "\n\nDo you want to reveal this state? (Yes/No)")
            if user_response and user_response.lower() in ['yes', 'y']:
                place_state(hinted_state)
        else:
            screen.textinput(title="Hint", prompt="No hints available!")
        continue  # Continue to the next iteration

    if answer_state in all_states and answer_state not in guessed_states:
        place_state(answer_state)
    else:
        # Notify the user of an incorrect guess
        screen.textinput(title="Incorrect", prompt="Incorrect! Try again or get a hint.")

# --------------------- End of Game ---------------------
# Save the missing states to a CSV file
missing_states = [state for state in all_states if state not in guessed_states]
if missing_states:
    new_data = pandas.DataFrame(missing_states, columns=["state"])
    new_data.to_csv("States_to_learn.csv", index=False)
    print("Game Over. The missing states have been saved to 'States_to_learn.csv'.")

# Display a congratulatory message if all states are guessed
if len(guessed_states) == len(all_states):
    final_turtle = turtle.Turtle()
    final_turtle.hideturtle()
    final_turtle.penup()
    final_turtle.goto(0, 0)
    final_turtle.write("Congratulations!\nYou've guessed all the states!", align="center", font=("Arial", 24, "bold"))

# Keep the Turtle window open until closed by the user
turtle.mainloop()
