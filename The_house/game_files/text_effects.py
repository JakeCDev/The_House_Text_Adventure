#======================================================================
#Text effect functions
#Text_effects.py
#======================================================================

#Internal imports
import game_states
from color_scheme import BLUE, RESET

#=====================================================================
#Outer imports
import time
import sys
import os

#======================================================================

#Slow type - type_text("")
def type_text(text, delay=0.04):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

#======================================================================

#Blinking text -
#def blinking_text

#======================================================================

#slow drip
def slow_drip(text, letter_delay=.2, dot_delay=0.7, pause_after=0.2):
    #Separate the word from the dots (assumes text ends with "...")
    if text.endswith("..."):
        word = text[:-3]
        dots = "..."
    else:
        word = text
        dots = ""

    #Print each letter of the word with a delay
    for char in word:
        print(char)
        time.sleep(letter_delay)

    #Print each dot with a delay
    for dot in dots:
        time.sleep(dot_delay)
        print(dot)

    #Add an extra newline and a short pause after printing
    print()
    time.sleep(pause_after)


#======================================================================

#slow type with dots - slow_dotted_text
def slow_dotted_text(text, dot_delay=0.4, char_delay=0.25): #adjust to change times, char delay for text

    #Type out the main text normally
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)

    #Print dots one at a time on the same line
    for dot in " . . . ":
        time.sleep(dot_delay)  # Delay before each dot
        sys.stdout.write(dot)
        sys.stdout.flush()

    print()  #Move to the next line after effect completes

#======================================================================

#rain drip
def rain_drip(repeats=3, delay=0.25, pause_between=0.6):
    for _ in range(repeats):
        print(BLUE + "D" + RESET)
        time.sleep(delay)
        print(BLUE + "r" + RESET)
        time.sleep(delay)
        print(BLUE + "i" + RESET)
        time.sleep(delay)
        print(BLUE + "p" + RESET)
        time.sleep(delay)
        print(BLUE + "." + RESET)
        time.sleep(delay)
        print(BLUE + "." + RESET)
        time.sleep(delay)
        print(BLUE + "." + RESET)
        time.sleep(pause_between)
        print()

#======================================================================