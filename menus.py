from colorama import Fore, Style, init
from character_classes import CHARACTER_CLASSES
from character_creation import CharacterClass
import textwrap

def game_start_menu():
    """
    Presents a menu to the player upon starting the game.
    """
    print("-"*10)
    print(f"{Fore.LIGHTGREEN_EX}[{Style.RESET_ALL}1{Fore.LIGHTGREEN_EX}]{Style.RESET_ALL}: New Game")
    print(f"{Fore.LIGHTGREEN_EX}[{Style.RESET_ALL}2{Fore.LIGHTGREEN_EX}]{Style.RESET_ALL}: Load Game")
    print(f"{Fore.LIGHTGREEN_EX}[{Style.RESET_ALL}3{Fore.LIGHTGREEN_EX}]{Style.RESET_ALL}: Quit")
    print("-"*10)

    print("Which would you like to do?")
    choice = input("> ")

    if choice == "1":
        class_choice_menu()
    elif choice == "2":
        print('sweet')
    else:
        print('dude!')

def class_choice_menu():
    """
    Displays a formatted, gamified menu for the player to choose their class.
    """
    # --- Configuration ---
    # Define a width for the menu. This makes it easy to adjust the size.
    menu_width = 70

    # --- Header ---
    # A decorative top border for the menu box.
    print(f"{Fore.YELLOW}╔{'═' * menu_width}╗{Style.RESET_ALL}")
    
    # A centered title. The .center() method is great for this.
    title = " C H O O S E   Y O U R   P A T H "
    print(f"{Fore.YELLOW}║{Style.BRIGHT}{Fore.CYAN}{title.center(menu_width)}{Style.RESET_ALL}{Fore.YELLOW}║")
    
    # A separator line to divide the title from the content.
    print(f"{Fore.YELLOW}╠{'═' * menu_width}╣{Style.RESET_ALL}")

    # --- Menu Items Loop ---
    # Using enumerate(..., 1) is a clean way to get a counter starting from 1.
    # .items() gives us both the key (e.g., "accountant") and the value (the dictionary)
    for index, (class_id, class_data) in enumerate(CHARACTER_CLASSES.items(), 1):
        
        # An empty line inside the box for spacing
        print(f"{Fore.YELLOW}║{' ' * menu_width}║")

        # --- The Class Name Line ---
        # We build the line piece by piece to calculate padding later.
        choice_str = f"  [{index}] "
        name_str = f"{class_data['class_name']}"
        
        # Combine the pieces with their colors
        line_content = (
            f"{Fore.LIGHTGREEN_EX}{choice_str}{Style.RESET_ALL}"
            f"{Style.BRIGHT}{Fore.WHITE}{name_str}{Style.RESET_ALL}"
        )

        # Calculate how much space is left to fill to reach the right border
        padding = menu_width - len(choice_str) - len(name_str)
        print(f"{Fore.YELLOW}║{line_content}{' ' * padding}║")

        # --- The Description ---
        # Indent the description and wrap it to the menu's width.
        # The 'initial_indent' and 'subsequent_indent' make it look neat.
        description_lines = textwrap.wrap(
            class_data['class_description'],
            width=menu_width - 6, # A little narrower than the box
            initial_indent='      ',
            subsequent_indent='      '
        )
        for line in description_lines:
            # Print each wrapped line of the description within the box borders
            desc_padding = menu_width - len(line)
            print(f"{Fore.YELLOW}║{Fore.LIGHTBLACK_EX}{line}{' ' * desc_padding}║")

    # --- Footer ---
    # An empty line before the bottom border for nice spacing.
    print(f"{Fore.YELLOW}║{' ' * menu_width}║")
    # The final bottom border of the box.
    print(f"{Fore.YELLOW}╚{'═' * menu_width}╝{Style.RESET_ALL}")

    print("\nWhat path shall you choose?")
    choice = input("> ").strip().lower()

    class_keys = list(CHARACTER_CLASSES.keys())

    if choice.isdigit() and 1 <= int(choice) <= len(class_keys):
        int_choice = int(choice)
        chosen_index = int_choice - 1
        chosen_class_key = class_keys[chosen_index]

        chosen_class_data = CHARACTER_CLASSES[chosen_class_key]

        class_object = CharacterClass(**chosen_class_data)

        return class_object