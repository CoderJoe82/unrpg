from locations import display_welcome_message
from helper_functions import clear_screen,  print_wrapper, display_location_header, print_divider
from menus import game_start_menu
from locations import LOCATIONS
from colorama import Fore, Style
from data_manager import DataManager

def main():
    # --- DATA MANAGEMENT OBJECT ---
    """
    This object will be what holds our data and creates our save files to hold all the things that happen as the game progresses.
    """
    data_manager = DataManager()

    # === The main game State ===
    game_state = {
    "player" : None,
    "current_location_id" : None,
    "game_time" : 0,
    "world_events" : {
        "met_the_king" : False,
        "goblin_cave_cleared" : False,
        "secret_bridge_revealed" : False,
    },
    "is_running" : True,
    "npcs" : {

            }
    }

    """
    This is the main function where our game will run.
    """
    clear_screen()
    display_welcome_message()
    player_character = game_start_menu()

    if player_character and player_character != "quit":
        game_state['player'] = player_character
        game_state['current_location_id'] = "golga_city"
    else:
        game_state['is_running'] = False

    # --- Main game loop ---
    while game_state['is_running']:
        # --- Reading the game state ---
        player= game_state['player']
        current_location_id = game_state['current_location_id']
        # More to add here later.

        if not current_location_id:
            print("Error: Player has no location!")
            break

        location_data = LOCATIONS[current_location_id]



        # --- Get input and update the state ---

        # This is where the game's logic will live.
        # You'll have a big function here to handle input.
        # process_player_input(action, game_state)
        clear_screen()

        display_location_header(location_data['name'])


        print_divider('-')
        print_wrapper(location_data['description'])
        exits_label = f"{Style.BRIGHT}Exits:{Style.RESET_ALL}"
        exits_string = ",  ".join(location_data['exits'])
        full_exits_line = exits_label + exits_string
        print(f"\n{full_exits_line}")
        print_divider('-')

        print("Make your chice, adventurer!")
        action = input("> ").lower().strip() # <--- Going to change this later. Not very clear what instructions it's waiting on.


        if action == "quit":
            game_state['is_running'] = False
        elif action == "stats":
            print(f'HP: {player.current_health}/{player.max_health}')
            for stat, value in player.stats.items():
                print(f"{stat.capitalize()}: {value}")
            input("\nPress Enter to continue...")


    print("Thank you for playing!")

# This is the entry point of our program.
# The code inside this 'if' block will only run when the script is executed directly.
if __name__ == "__main__":
    main()