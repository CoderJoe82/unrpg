from colorama import Fore, Style
import os
import textwrap

def print_wrapper(text):
    """
    Gets the termianl width and prints the given text wrapped to fit.
    """
    try:
        box_width = int(os.get_terminal_size().columns * .75)
        if os.get_terminal_size().columns:
            width = box_width
        else:
            width = 80
    except OSError:
        # If the code doesn't work, just default the width to assume it should wrap at 80
        width = 80

    wrapped_text = textwrap.fill(text, width = width)

    print(wrapped_text)


def print_divider(symbol):
    """
    Makes a symbol to surround text that wraps the whole width that the text takes up just like print_wrapper.
    """
    try:
        box_width = int(os.get_terminal_size().columns * .75)
        if os.get_terminal_size().columns:
            width = box_width
        else:
            width = 80
    except OSError:
        width = 80

    print(symbol * width)

def clear_screen():
    """
    Clears the terminal screen.
    This function is cross-platform and works on Windows, macOS, and Linux.
    """
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def display_location_header(title):
    """
    Displays a stylized, boxed title card for a location or area.
    """

    title_text = title.upper()

    padding = 4
    box_width = len(title_text) + padding

    centered_title = title_text.center(box_width)

    styled_content = f"{Style.BRIGHT}{Fore.MAGENTA}{centered_title}{Style.RESET_ALL}"

    print(f"{Fore.YELLOW}╔{'═' * box_width}╗{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}║{styled_content}║{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}╚{'═' * box_width}╝{Style.RESET_ALL}")
    print() # Add a blank line for nice spacing before the description