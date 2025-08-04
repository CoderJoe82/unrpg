from colorama import Fore, Style, init
from helper_functions import print_wrapper

welcome_message = f"""
Welcome to a world poised on a knife's edge between the primal and the profound.
Here, civilization did not conquer nature, it formed a pact. Great cities of stone are woven with living wood, and the hum of magic coexists with the whisper of the wind.
---
But this world is a story waiting for its author. That author is {Style.BRIGHT}you{Style.RESET_ALL}.
Your path is an unwritten page. Who will you be?

Will you be a {Fore.GREEN}hero{Style.RESET_ALL}, whose deeds are sung by bards in taverns?
A {Fore.CYAN}scholar{Style.RESET_ALL}, piecing together the forgotten secrets of this world?
A shrewd {Fore.YELLOW}merchant{Style.RESET_ALL}, building an empire on coin and charisma?
A simple {Fore.GREEN}farmer{Style.RESET_ALL}, a dedicated {Fore.CYAN}healer{Style.RESET_ALL}, or a treasure-hungry {Fore.YELLOW}delver{Style.RESET_ALL} of forgotten ruins?

Or... do the {Fore.RED}shadows{Style.RESET_ALL} beckon? Ambition is a sharp blade.
You could become a master {Fore.RED}thief{Style.RESET_ALL}, a feared {Fore.RED}assassin{Style.RESET_ALL}, or even a would-be tyrant, seeking to unravel the balance of this world and weave it in your own dark image.

{Style.BRIGHT}Be warned: the world listens.{Style.RESET_ALL}
Every choice, from the smallest kindness to the most calculated cruelty, sends ripples across the land. An act of mercy today may save a kingdom tomorrow. A petty crime could ignite a war.

Your story begins now.
"""

def display_welcome_message():
    """
    Displays the stylized welcome message and game introduction.
    """
    # This ensures colorama works correctly on all systems
    init(autoreset=True)

    # ASCII Art Title
    title = "Unnamed RPG"
    box_width = len(title) + 6
    
    print(Fore.YELLOW + "╔" + "═" * box_width + "╗")
    print(Fore.YELLOW + "║" + " " * 3 + Style.BRIGHT + Fore.CYAN + title + Style.RESET_ALL + Fore.YELLOW + " " * 3 + "║")
    print(Fore.YELLOW + "╚" + "═" * box_width + "╝")
    print() # Add a little space

    print("-" * (box_width + 2))
    # The Welcome Prose
    print_wrapper(welcome_message)


    print("-" * (box_width + 2))
    print("\n")

LOCATIONS = {
    "golga_city" : {
        "name" : "Golga City",
        "type" : "city",
        "size" : "large",
        "description" : f"""
You are looking upon {Style.BRIGHT}{Fore.GREEN}Golga City{Style.RESET_ALL}, a marvel of symbiotic architecture where civilization and the natural world are not at odds, but in partnership.

To the east, the {Style.BRIGHT}{Fore.WHITE}Duke's Spire{Style.RESET_ALL} rises from a mighty foundation of grey river-stone. The fortress itself is carved from the heartwood of a single, petrified titanwood tree, its grain like polished alabaster. Stone buttresses, themselves covered in flowering moss, arc up to support balconies of living wood, from which banners of woven sun-petals flutter.

Dominating the skyline is the {Fore.MAGENTA}Mages' Conclave{Style.RESET_ALL}, an opulent tower of twisting, iridescent living coral that pulses with a soft, internal violet light. Floating motes of raw magic drift around its peak like fireflies, and its great, arched windows are not glass, but thinly-sliced, translucent agate, depicting ancient constellations.

At the city's heart lies the {Fore.YELLOW}Great Market{Style.RESET_ALL}, a sprawling plaza of smooth, cobbled stone. A grand fountain, sculpted from granite to resemble interlocked hands, offers up a constant flow of water purified by a cluster of glowing filter-lilies at its center. The air is a symphony of smells: sizzling glade-boar from food stalls, the sharp tang of alchemical reagents, and the earthy perfume of fresh soil from the farmer's stands.

The residential districts are a harmonious blend of styles. Some are cozy {Fore.GREEN}earth-homes{Style.RESET_ALL} burrowed into gentle, grass-covered hillsides. Others are stout buildings of timber and stone, their slate roofs heavy with lush, green moss and rooftop gardens. In the artisan quarter, you hear the rhythmic *chink* of a gem-cutter's chisel against the gentle hum of a Lumina-weaver's loom. A large building of amber resin and polished oak stands proudly; a sign written in glowing moss identifies it as {Fore.CYAN}The Cultivarium{Style.RESET_ALL}, the city's revered house of healing where Restorative Spores hang thick in the air.

To the west, the sharp scent of salt and sea-pollen blows in from the {Fore.BLUE}Dock Ward{Style.RESET_ALL}. Massive granite breakwaters, worn smooth by ages of tide, protect a harbor bustling with activity. Piers of hardened mangrove roots, strong as steel, jut out into the bay. Here, skiffs carved from enormous seed pods are loaded with goods from stone warehouses whose roofs are living patches of sod, insulating them from the sun's heat.

From where you stand, several paths are clear. A well-trodden road leads {Fore.YELLOW}north{Style.RESET_ALL} towards the warm, inviting light of a large inn. The main gate lies to the {Fore.YELLOW}south{Style.RESET_ALL}, leading out of the city. The grand avenues to the {Fore.YELLOW}east{Style.RESET_ALL} wind towards the Duke's Spire and the Mages' Conclave, while the distinct smell of salt and sea-pollen draws you {Fore.YELLOW}west{Style.RESET_ALL}, towards the Dock Ward.

((ooc note: Not other directions but north are worked on as of this moemnt.))
""",
        "exits" :  [f'{Fore.YELLOW}north{Style.RESET_ALL}', 'east', 'south', 'west']
    },
}