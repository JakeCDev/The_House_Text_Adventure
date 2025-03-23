#======================================================================
#Final Room - Ending of the Game
#room_14_final_room.py
#======================================================================

#Internal imports
import game_states
from text_effects import type_text, slow_dotted_text
from game_mechanics import visit_room, distort_name, full_reset_game
from start_menu import start_menu  #To return to the main menu
from ascii_art import ascii_art
from debug_mode import debug_menu
from color_scheme import YELLOW, MAGENTA, BLUE, CYAN, RED, GREEN, DIM_WHITE, BRIGHT_CYAN, BRIGHT_BLUE, RESET

#======================================================================

#External imports
import random
import time
import sys

#======================================================================

def colorize_rainbow_name(name, delay=0.04):
    colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]

    for char in name:
        if char.isspace():
            sys.stdout.write(" ")
        else:
            color = random.choice(colors)
            sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)

#======================================================================

def colorize_ending():
    art = ascii_art["ending"]
    glow_colors = [CYAN, BRIGHT_CYAN, BLUE, BRIGHT_BLUE]

    for char in art:
        if char in ["M", "8", "&", "'", ",", "."]:
            print(f"{YELLOW}{char}{RESET}", end="")  # Always yellow
        elif char == "*":
            print(f"{random.choice(glow_colors)}*{RESET}", end="")  # Glowing stars
        else:
            print(char, end="")

#======================================================================

#Final function room: 14 - The Ending
def room_14_final_room():
    #Room tracker
    room_name = "room_14_final_room"
    visit_count = game_states.room_visits.get(room_name, 0)

    type_text(f"\n{DIM_WHITE}You step through the doorway. The air is warm and familiar, like you have been here before{RESET}")
    time.sleep(1)

    type_text(f"{DIM_WHITE}A soft{RESET} {YELLOW}glow{RESET} {DIM_WHITE}fills the space ahead. It feels... safe{RESET}.")
    time.sleep(1)

    type_text("\nYour thoughts begin to clear. The memories return in waves...")
    time.sleep(1)
    print()
    slow_dotted_text("The Rain")
    time.sleep(.5)
    print()
    slow_dotted_text("The Road")
    time.sleep(.5)
    print()
    slow_dotted_text("The Crash")
    time.sleep(.5)
    print()
    slow_dotted_text("The House")
    time.sleep(1)

    type_text("\nSomewhere in the distance, a child cries. A lullaby hums softly in response.")
    type_text("The weight in your chest begins to fade. The fear loosens its grip.")
    time.sleep(1)

    type_text("\nYou feel something calling you forward. And then... you hear a name...")
    time.sleep(2)

    type_text("\n'", delay=0.04)
    colorize_rainbow_name(game_states.player_name, delay=0.04)
    type_text("'... Are you there, do you hear me?", delay=0.04)
    time.sleep(1)

    type_text("\nThe air seems to tremble.")
    time.sleep(1)

    type_text("\nYou feel a strange pull, a soft whisper keeps calling you forward.")
    time.sleep(1)

    type_text("\nThe name almost feels like a vague memory now...")
    time.sleep(1)

    slow_dotted_text(f'"{YELLOW}You\'re almost there{RESET}"')
    time.sleep(1)

    #Final Choice
    print("\nWhat do you want to do?")
    print(f"1. {GREEN}Step forward into the light{RESET}")

    while True:
        choice = input("> ").strip()

        if choice == "1":
            distorted_name = distort_name(game_states.player_name, stage=2)
            time.sleep(1)
            type_text("\n'", delay=0.04)
            colorize_rainbow_name(distorted_name, delay=0.04)
            type_text("'... The voice warps, muffled, as if the sound is slipping away", delay=0.04)
            end_game()
            return
        else:
            time.sleep(1)
            type_text(f"\n{YELLOW}Something urges you forward. There is no other path. You must move on{RESET}.")
            time.sleep(1)

#======================================================================
#End game function
def end_game():
    type_text(f"\nYou step forward as the {YELLOW}light{RESET} engulfs you.")
    type_text("The weight you've carried lifts, and the fear fades.")
    time.sleep(1)

    type_text("\nThe lullaby grows clearer. A soft melodic voice hums with it.")
    slow_dotted_text(f"\nFor the first time in what feels like lifetimes... you have this unexplainable sense of {GREEN}peace{RESET}")
    time.sleep(2)

    #third name call fully distorted
    distorted_name = distort_name(game_states.player_name, stage=3)
    time.sleep(1)
    type_text("\nA name now fully lost, distorted, incomprehensible... The world around you feels distant.", delay=0.04)
    time.sleep(1)
    type_text(f"The {YELLOW}light{RESET} grows stronger, blinding... you hear the voice one final time... '",
              delay=0.04)
    colorize_rainbow_name(distorted_name, delay=0.04)
    type_text("'", delay=0.04)
    time.sleep(1)

    slow_dotted_text(f"\n{GREEN}At last{RESET}")

    #Display ending artwork
    colorize_ending()

    type_text(f"\n{GREEN}FIN{RESET}.")
    time.sleep(1)
    type_text(f"{GREEN}Thank you for playing!{RESET}")
    time.sleep(1)
    print(f'{RED}"The House"{RESET}')
    print(f"{BRIGHT_CYAN}By: Jake Chrissinger{RESET}")
    time.sleep(1)
    time.sleep(2)

    input(f"\nPress {GREEN}Enter{RESET} to return to the main menu.")  #Pause before restarting
    full_reset_game()
    start_menu()  #Return to the main menu

#======================================================================
