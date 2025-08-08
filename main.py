from locations import display_welcome_message
from helper_functions import clear_screen
from menus import game_start_menu

def main():
    """
    This is the main function where our game will run.
    """
    clear_screen()
    display_welcome_message()
    game_start_menu()

# This is the entry point of our program.
# The code inside this 'if' block will only run when the script is executed directly.
if __name__ == "__main__":
    main()