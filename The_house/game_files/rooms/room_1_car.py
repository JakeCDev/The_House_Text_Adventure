#======================================================================
#Car room:1 (Starting Room)
#rooms/room_1_car.py
#======================================================================

#Imports
import game_states
from game_mechanics import visit_room, check_inventory, universal_wait
from text_effects import type_text
from ascii_art import ascii_art
from debug_mode import debug_menu
from pause_menu import pause_menu
from color_scheme import YELLOW, BLUE, RED, DIM_WHITE, RESET
from sound_manager import stop_music, play_ambient_loop, play_sound_effect
import random

#======================================================================

#Car function room: 1
def room_1_car():

    #Room tracker
    room_name = "room_1_car"  #Store name as variable
    visit_count = game_states.room_visits.get(room_name, 0)

    #Smooth fade out intro music when entering the car and loop in quiet wind
    stop_music(fade_out=2000)
    play_ambient_loop("wind", "wind_loop.wav", volume=0.3)

    if visit_count == 0:  #Present
        type_text("\nYou sit in your broken-down car on the side of the road.")
        play_sound_effect("thunder_1.wav", volume=0.4)
        type_text(f"The {BLUE}rain{RESET} hammers against the windshield. The road ahead is dark and empty, not a single {DIM_WHITE}soul{RESET} in sight.")

    elif visit_count == 1:  #Past
        type_text("\nThe radio hums softly, playing a song you almost recognize, but the engine is still dead.")
        play_sound_effect("thunder_1.wav", volume=0.35)
        type_text(f"The interior lights are all dimly {YELLOW}lit{RESET}... but you don’t remember turning them on.")
        type_text("A bouquet of fresh flowers rests on the passenger seat...")

    elif visit_count == 2:  #Future
        type_text("\nThe car is different... No longer a broken down vehicle but a brand new vehicle yet, it still won't start...")
        play_sound_effect("thunder_2.wav", volume=0.5)
        type_text(f"You peer down the middle of an empty stretch of road, surrounded by trees, the asphalt slick with rain.")
        type_text(f"Somewhere in the distance, you think you hear tires screeching... or was it just {YELLOW}thunder{RESET}?")

    elif visit_count == 3:  #Eerie
        type_text(f"\n{RED}Movement{RESET} flickers in the rearview...")
        play_sound_effect("thunder_2.wav", volume=0.6)
        type_text("You whip around. Nothing. The seat is empty, just as it should be.")
        type_text("You must be exhausted... or maybe you hit your head harder than you thought?")


    else:  #Altered Reality
        type_text("\nYour car has warped completely...")
        play_sound_effect("thunder_3.wav", volume=0.7)
        type_text("The steering wheel is completely missing, the tires have twisted into melted spirals, and the dashboard drips as if made of wax.")
        type_text(f"The {BLUE}rain{RESET} falls in slow motion... The road stretches on forever in both directions as far as you can see...")

#======================================================================

    #Car art
    print(ascii_art["car"])

#======================================================================

    #Car choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Wait in the car")
        print("3. Head north up the road")
        print("4. Check Inventory")

        choice = input("> ").strip()

        if choice == "1":
            look_around_car()  #Call look around car function

        elif choice == "2":
            universal_wait()  #Call random lore text/random module
            input("\nPress Enter to continue.")  #Pause before re-displaying menu

        elif choice == "3":
            type_text(f"\nYou step out into the cold dark night. A dim {YELLOW}light{RESET} glows in the distance.")
            play_sound_effect("thunder_2.wav", volume=0.4)
            type_text("You should hurry on out of the storm.")
            game_states.room_visits[room_name] += 1  #Update visit count
            visit_room("room_2_road")  #Move to the road
            break  #Exit the interaction loop

        elif choice == "4":
            check_inventory(room_1_car)  #Call inventory function

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")

#======================================================================

#Looking around the car
def look_around_car():
    while True:
        type_text("\nYou scan the inside of your car. What do you want to check?")
        print("1. Glove compartment")
        print("2. Trunk")
        print(f"3. {RED}Nevermind{RESET}")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nYou open the glove compartment. Just old receipts, junk mail, and some change.")
            print(ascii_art["mail"])

        elif choice == "2":
            type_text("\nYou pop the trunk. Nothing but an old musty blanket, a tire iron, and some old clothes.")
            print(ascii_art["clothes"])

        elif choice == "3":
            return  #Exit back to the car menu

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        elif choice == "pause":
            pause_menu()

        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")

#======================================================================

#End

#======================================================================