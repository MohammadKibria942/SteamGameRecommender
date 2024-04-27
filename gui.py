import sys
import pandas as pd
import PySimpleGUI as sg

# Path for the steam data
path = "FinalData/steam_clean.csv"

ds = pd.read_csv(path)

gamesList = []
appidList = []

# Function to filter game names based on user input for autofill
def get_autofill_options(input_text):
    return [name for name in ds.name if input_text.lower() in name.lower()]

# Set the layout for the main menu with centered text and buttons
layout_main_menu = [
    [sg.Text("Game Recommender!", size=(40, 1), font=("Verdana", 36), justification='center')],
    [sg.Text(size=(100, 10))],  # Spacer element for vertical centering
    [sg.Text("Please enter the number of games you want to add (1-3): ", font=("Verdana", 12), justification='center')],
    [sg.Input(key='-NUM_GAMES-', size=(10, 1), justification='center')],
    [sg.Button("Start", size=(10, 1), pad=(5, 5), button_color=('white', 'teal')), sg.Button("Exit", size=(10, 1), pad=(5, 5), button_color=('white', 'red'))],
]

window_main_menu = sg.Window("Steam Game Recommender", layout_main_menu, size=(1280, 720), element_justification='center', finalize=True)

while True:
    event, values = window_main_menu.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        sys.exit(0)
    elif event == 'Start':
        try:
            n = int(values['-NUM_GAMES-'])
            if n < 1 or n > 3:
                raise ValueError
            break
        except ValueError:
            sg.popup_error("Please enter a valid integer between 1 and 3.")

window_main_menu.close()


# Set the layout for the autofill input
layout_game_input = [
    [sg.Text("Game Recommender!", size=(40, 1), font=("Verdana", 36), justification='center')],
    [sg.Text(size=(100, 12))],  # Spacer element for vertical centering
    [sg.Text("Enter the name of the game you want to add:", size=(40, 1), font=("Helvetica", 16), justification='center')],
    [sg.Input(enable_events=True, key='-INPUT-', size=(50, None), justification='center')],
    [sg.Listbox(values=[], size=(50, 5), enable_events=True, key='-LISTBOX-')],
    [sg.Button("Submit", key='-SUBMIT-', size=(10, 1), pad=(5, 5), button_color=('white', 'green'))]
]

window_game_input = sg.Window("Steam Game Recommender", layout_game_input, size=(1280, 720), element_justification='center', finalize=True)

# While loop to ask for the names of the games the user wants to enter
i = 0
while i < n:
    event, values = window_game_input.read()

    if event == sg.WIN_CLOSED:
        sys.exit(0)
    elif event == '-INPUT-':
        # Get autofill options based on input text
        autofill_options = get_autofill_options(values['-INPUT-'])
        window_game_input['-LISTBOX-'].update(autofill_options)
    elif event == '-LISTBOX-':
        # If a suggestion is clicked, update the input field with the selected suggestion
        game = values['-LISTBOX-'][0]
        window_game_input['-INPUT-'].update(game)
    elif event == '-SUBMIT-':
        if values['-LISTBOX-']:
            game = values['-LISTBOX-'][0]
            gamesList.append(game)
            sg.popup_ok("Game Submitted: " + game, auto_close=True, auto_close_duration=2)
            i += 1

window_game_input.close()

sg.popup_ok("Results Ready", title="Results Ready", auto_close=True, auto_close_duration=3)  # Set duration in case user does not click the button

# Appends the appid of the inputted games to the appid list
for game in gamesList:
    appid = ds.loc[ds['name'] == game, 'appid'].values
    if len(appid) > 0:
        appidList.append(appid[0])

print("Games List:", gamesList)
print("AppID List:", appidList)
