#======================================================================
#Game Intro
#game_intro.py
#======================================================================

#External imports
import time
import random
from color_scheme import RED, BRIGHT_RED, GREEN, BRIGHT_GREEN, BLUE, BRIGHT_BLUE, YELLOW, BRIGHT_YELLOW, CYAN, BRIGHT_CYAN, MAGENTA, BRIGHT_MAGENTA, WHITE, DIM_WHITE, RESET
import random

#======================================================================

#Internal imports
from text_effects import type_text, slow_drip, rain_drip  # Import text effects
from ascii_art import ascii_art  # Import ASCII art dictionary

#======================================================================

#storm cloud art and rain mechanics

def colorize_rain(rain_art):

    rain_colors = [BLUE, CYAN, BRIGHT_BLUE, BRIGHT_CYAN, DIM_WHITE]

    for line in rain_art.strip("\n").splitlines():
        colored_line = ""
        for char in line:
            if char in ["/", "\\", "|"]:
                color = random.choice(rain_colors)
                colored_line += f"{color}{char}{RESET}"
            else:
                colored_line += char
        print(colored_line)

#======================================================================

#Create game intro function - leading to car/first room
def game_intro():
    #Repeating rain effect
    rain_drip()
    time.sleep(0.5)

    #Slow text effect for dramatic intro
    type_text(f"\n{DIM_WHITE}The world is a haze...", delay=0.12)
    type_text("Darkness surrounds you...", delay=0.11)
    type_text("A ringing fills your ears...", delay=0.10)
    type_text("\nFor a moment, you can’t recall who you are...", delay=0.085)
    type_text("or even where you are...", delay=0.07)
    time.sleep(0.8)
    type_text(f"\n{RED}Pain...{RESET}", delay=0.15)
    time.sleep(0.8)

    # Stage 4: Regain clarity – normal pacing resumes
    type_text("""
A dull ache throbs in your head. Stiffness in your neck. Something… something must have happened.
Slowly, the fog in your mind begins to lift.  

Rain. You hear it clearly now, hammering against the windshield.  
The wind howls through cracks, a chilling whisper you can’t quite make out, echoing from the dark.  

The car… You try to start it, but it won’t turn over…  

Your fingers tighten around the steering wheel as the haze fades.  
You must have lost control. Maybe the roads were too slick…  

For now, your car is half-buried in a ditch, the engine dead.  
Headlights barely cut through the storm as the radio blares static on every station…  

You reach for your phone. The screen flickers to life, but there’s no signal…  
Nothing visible but the storm and darkness for miles around…  

But wait… Through the downpour, just barely brighter than a shadow… you see it.  
A house in the distance… with a single, flickering light from within.  

You could stay put and wait for the storm to pass.  
But it doesn’t look like it will let up anytime soon…  

Something about that house draws you in, its faint {YELLOW}light{RESET} calling to you through the rain.  
Maybe there’s someone inside who can help… or a phone to call for help.  

Or perhaps, through some twist of fate, you were always meant to find this place.  
""")

#Show storm ASCII art - appears before user input for enter in main.py
    for line in ascii_art["storm"].strip("\n").splitlines(): #strips away the blank line after the print
        print(f"{DIM_WHITE}{line}{RESET}")
    colorize_rain(ascii_art["rain"])
    time.sleep(1)

    return
#======================================================================


 