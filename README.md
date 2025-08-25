# unrpg
Me learning how to make an rpg game with pygame using a.i. but not only to make it, but teach me.

V-0.0.23
---
-Finished major refactoring in current phasing steps finished.

V-0.0.22
---
-Added 'phasing' functionality for the character creation screen.
-Added some helper functions to make creating things easier.
-Did some refactoring of the code after it was finished.

V-0.0.21
---
-Added a race selection screen
-Added race buttons for all races currently in the game, set up to automatically adjust perfectly even vertically if I add another later.
-Added a pygame line as a divider to the right side of the buttons for separating the buttons from the race descriptions once you click the race buttons one by one.

V-0.0.21
---
-HUGE refactoring of my character_creation_screen.py file. Split it into individual objects.
-Added a WelcomePhase and RaceSelectionPhase file and severely condensed the CharacterCreationScreen object.

V-0.0.20
---
-I've moved on from character creation data for the moment, with plans to go back later and add other things
-Added a new welcome screen for when the player clicks new game.
-Added event handlers for people to go back to the main menu with a button from the welcome screen as well.

V-0.0.19
---
-Added a layout of future plans in character class that aren't crucial for now.
-Added an event handler method in MainMenu.
-Refactored game.py to make switching game states much simpler than I had previously tried.

V-0.0.18
---
-Added a function to get all the data of each piece of gear.
-Added a function to grab the resistance and stat and status effects bonuses from all character gear
-Added a function to apply all those bonuses to the Character object init.
-Refactored quite a bit.

V-0.0.17
---
-Adjusted some minor details for refactoring in my previous functions and also changed get finalized stats function too include our new functions

V-0.0.16
---
-Finally have checking all the player's gear out and then adding them all together for stat modifiers and also added a dictionary for holding any special statuses and their true or false flags

V-0.0.15
---
-Got a function working to loop over all the character's gear and grab any passive buffs or debuffs, and those are all shoved into a list.

V-0.0.14
---
-Worked on getting a function started to loop over the character's equipped gear and gather all the stat bonuses from it and put it into the character's stat bonuses container.

v-0.0.13
---
-Changed _get_starting_equipment to _get_starting_inventory
-Added a new EQUIPMENT dictionary with keys of each equipment location for the characters
-Added a _check_if_slot_full helper function to use for when someone tries to equip something

v-0.0.12
---
I just get going and forget to commit and push. Bad habit, huh?
-Added all the weapon files, and armor files for a start point of levels 1 - 10, like everything else.
-Added all the class and race data that was missing.
-Built multiple database 'lists' to hold all the data of every item and spell and ability, and a master equipment list
-Added new item types
-A few more refactors and bug fixes.

V-0.0.11
---
Yes. That's right! I feel like I skipped three minor versions this upload!
-Added all sorts of Character methods
-Added the actual character_classes file filled with character classes, all having their starting abilities and starting equipment all added.
-Added three functions: load_all_abilities load_all_armors() load_all_weapons() to give the game master dictioinaries with all oft hose things
-Refined some things already in my code

V-0.0.8
---
-Added a Character method to get final stats on creation
-Added a Character method to get all the player's starting abilities on character creation

V-0.0.7
---
-Finished (currently) CharacterClass and CharacterRace object.

V-0.0.6
---
-Finished building out the inits for CharacterClass and CharacterRace.
-Started adding methods for both classes. More methods are next on the list.

V-0.0.5
---
-Added .json files for a few weapons of sevearl types for level 1 - 10.
-Added a .json file for shields.
-Added a CharacterClass class to hold data to pass through to create any character we could want later, including the player. (no methods yet. That's next.)

V-0.0.4
---
-Added spells for all magic types up to level 10 for now.

V-0.0.3
---
-Added the main menu buttons on the start up page.

v-0.0.2
---
-Added a new folder called engine to store our Game class object.
-Added a menus and mainmenu and button file for code clarity.
-Added a Button object to create buttons later.

V-0.0.1
---
-Added the main game core function.