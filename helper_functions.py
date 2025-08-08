import os
import textwrap

def print_wrapper(text):
    """
    Gets the termianl width and prints the given text wrapped to fit.
    """
    try:
        width = os.get_terminal_size().columns
    except OSError:
        # If the code doesn't work, just default the width to assume it should wrap at 80
        width = 80

    wrapped_text = textwrap.fill(text, width = width)

    print(wrapped_text)

def clear_screen():
    """
    Clears the terminal screen.
    This function is cross-platform and works on Windows, macOS, and Linux.
    """
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')