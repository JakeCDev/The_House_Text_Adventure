#======================================================================
#Game Intro
#game_intro.py
#======================================================================

#External imports
import time
import random

#Internal imports
from text_effects import type_text, slow_drip  # Import text effects
from ascii_art import ascii_art  # Import ASCII art dictionary

#======================================================================

#Create game intro function - leading to car/first room
def game_intro():
    #Repeating "Drip..." effect
    for _ in range(3):
        slow_drip("Drip...", letter_delay=0.3, dot_delay=0.7, pause_after=0.2)
        time.sleep(0.5)

    #Slow text effect for dramatic intro
    type_text("""
The world is a haze. Darkness surrounds you. A ringing fills your ears.  
For a moment, you can’t recall who you are… or even where you are…  

Pain. A dull ache throbs in your head. Stiffness in your neck. Something… something must have happened.  
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

Something about that house draws you in, its faint light calling to you through the rain.  
Maybe there’s someone inside who can help… or a phone to call for help.  

Or perhaps, through some twist of fate, this house is a place you were always meant to find.  
""")
#======================================================================
#Show storm ASCII art - Appears before user input for 'enter' in main.py
    print(ascii_art["storm"])
    time.sleep(1)

    return


#======================================================================

 