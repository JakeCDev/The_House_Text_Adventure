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
        slow_drip("Drip...", letter_delay=0.2, dot_delay=0.7, pause_after=0.2)
        time.sleep(0.2)

    #Slow text effect for dramatic intro
    type_text("""
Your world is in a haze. Darkness all around. A ringing fills your ears.  
For a moment, you can't recall who you are... or even where you are...  

The pain... A dull ache in your head. Stiffness in your neck. Something… something must have happened.  
Slowly, the fog in your mind begins to lift.  

Rain. You can hear it now, hammering against the windshield in an unrelenting fashion.  
The wind howls through unseen cracks, a chilling whisper you just can't quite make out echoes from the dark.  

The car... You try, but it won’t seem to restart...  

Your fingers tighten around the steering wheel as clarity settles in.  
Somehow, you must have lost control... Maybe the roads were too slick...  
For now, your car is half-buried in a ditch. The engine is dead.  
Headlights barely cut through the storm as the radio blares static...  

You reach for your phone. The screen flickers on, but there’s no signal...  
Nothing but static and emptiness for miles around, it would appear...  

Through the downpour, just barely brighter than a shadow... you see it.  
A house in the distance... with a single, flickering light from within.  

Maybe they could offer some help to get out of this storm...  

You could stay put. Wait for the rain to pass.  
But it doesn't look like it will let up anytime soon.  

There is just something about that house...  
It feels important... like it is calling you.  

Maybe there is someone who can help... or even a phone, perhaps.  
Or maybe… through fate, you were just meant to find this house.  
""")

#======================================================================
#Show storm ASCII art - Appears before user input for 'enter' in main.py
    print(ascii_art["storm"])
    time.sleep(1)

    return


#======================================================================

 