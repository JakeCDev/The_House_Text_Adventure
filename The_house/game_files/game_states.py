#======================================================================
#Game states - permanent status checker/trackers
#game_states.py
#======================================================================

#Imports

#=====================================================================

#Tracks the player's current room - starts with first room
current_room = "room_1_car"

last_room = None

#======================================================================

#Tracks how many times each room has been visited - used for shifting room states - present,past,future,eerie,altered
room_visits = {
    "room_1_car": 0,
    "room_2_road": 0,
    "room_3_porch": 0,
    "room_4_entryway": 0,
    "room_5_office": 0,
    "room_6_kitchen": 0,
    "room_7_basement": 0,
    "room_8_living_room": 0,
    "room_9_dining_room": 0,
    "room_10_upstairs_hallway": 0,
    "room_11_bedroom_a": 0,
    "room_12_bedroom_b": 0,
    "room_13_attic": 0
}

#======================================================================

#Player inventory list - starts empty
inventory = []

#======================================================================

#Store the player chosen name (set during get_player_name())
player_name = "Unknown"  #Default before they enter a name

#======================================================================

#Item descriptions
item_descriptions = {
    "Screwdriver": "A rusty screwdriver. Could be useful for prying something open...",
    "Locked Box": "A small, rusted lockbox. The lid is sealed shut. You’ll need something to pry it open.",
    "Lockbox Opened": "The rusted box you found, now opened. Inside were old photos, burnt papers, and a obituary.",
    "Skeleton Key": "A heavy brass key. Looks important. Might unlock something upstairs...",
    "Red Fuse": "A red-colored fuse. Looks intact. You might need this somewhere.",
    "Green Fuse": "A green-colored fuse. Looks intact. You might need this somewhere.",
    "Blue Fuse": "A blue-colored fuse. Looks intact. You might need this somewhere.",
    "Safe Order Hint": "Down below, where there is no sight. At the table, in flickering light. Where the clock forgets what’s wrong from right.",
    "Fuse Order Hint": "Scrawled in the margins, barely readable, R.G.B",
    "Attic Hint": "It's all hidden in the attic.",
    "Basement Safe Password Hint": "You found a number '6' etched into the concrete walls of the basement.",
    "Dining Room Safe Password Hint": "You found a number '7' scratched into the wood of the dining table.",
    "Living Room Safe Password Hint": "The clock in the living room flickered strangely, displaying the time '3:00'. This might be important.",
    "Map": """
                                                    [ Attic ]
                                                        |
                                                  [ Bedroom A ]        [ Bedroom B ]
                                                        |                  |
                    [?????]                             [ Upstairs Hallway ]                          
                       |                                        |   
[ Basement ] ---- [ Kitchen ] -------------------------- [ Dining Room ]
                       |                                        |
                   [ Office ] ---- [ Entryway ] -------- [ Living Room ]
                                        |                   
                                    [ Porch ]          
                                        |                   
                                    [ Road ]            
                                        |                   
                                     [ Car ]    """,
    "Driver's License": "A worn-out driver's license. The name is hard to read..."
}

#======================================================================

#Room nickname dictionary
room_aliases = {
    "car": "room_1_car",
    "start": "room_1_car",
    "road": "room_2_road",
    "porch": "room_3_porch",
    "entryway": "room_4_entryway",
    "entry way": "room_4_entryway",
    "entry": "room_4_entryway",
    "office": "room_5_office",
    "kitchen": "room_6_kitchen",
    "basement": "room_7_basement",
    "living room": "room_8_living_room",
    "dining room": "room_9_dining_room",
    "upstairs hallway": "room_10_upstairs_hallway",
    "upstairs": "room_10_upstairs_hallway",
    "hallway": "room_10_upstairs_hallway",
    "hall": "room_10_upstairs_hallway",
    "bedroom b": "room_11_bedroom_b",
    "bedroom a": "room_12_bedroom_a",
    "attic": "room_13_attic",
    "final room": "room_14_final_room",
    "final": "room_14_final_room",
    "finale": "room_14_final_room",
    "end": "room_14_final_room"
}

#======================================================================

#room audio map

#Tracks what background sounds should be playing for each room (used for debug syncing)

room_sound_map = {
    "start_menu": {"music": ("intro_music.wav", 0.4)},
    "game_intro": {"music": ("intro_music.wav", 0.4), "ambience": {"rain": ("rain_loop.wav", 0.2)}},
    "room_1_car": {"ambience": {"rain": ("rain_loop.wav", 0.2), "wind": ("wind_loop.wav", 0.3)}},
    "room_2_road": {"ambience": {"rain": ("rain_loop.wav", 0.8), "wind": ("wind_loop.wav", 0.9)}},
    "room_3_porch": {"ambience": {"spooky": ("spooky_loop.wav", 0.2), "rain": ("rain_loop.wav", 0.4), "wind": ("wind_loop.wav", 0.5)}},
    "room_4_entryway": {"ambience": {"house": ("house_loop.wav", 0.6)}},
    "room_5_office": {"ambience": {"house": ("house_loop.wav", 0.6), "tick": ("clock_tick.wav", 0.4)}},
    "room_6_kitchen": {"ambience": {"house": ("house_loop.wav", 0.6)}},
    "room_7_basement": {"ambience": {"ghost": ("ghost_whisper.wav", 0.6), "drip": ("drip_sound.wav", 0.6)}},
    "room_8_living_room": {"ambience": {"vintage": ("vintage_loop.wav", 0.6)}},
    "room_9_dining_room": {"ambience": {"house": ("house_loop.wav", 0.6)}},
    "room_10_upstairs_hallway": {"ambience": {"house": ("house_loop.wav", 0.6)}},
    "room_12_bedroom_a": {"ambience": {"house": ("house_loop.wav", 0.6)}},
    "room_11_bedroom_b": {"ambience": {"house": ("house_loop.wav", 0.6)}},
    "room_13_attic": {"ambience": {"ominous": ("ominous_loop.wav", 0.6)}},
    "room_14_final_room": {"ambience": {"ethereal": ("ethereal_loop.wav", 0.6)}}
}

#======================================================================

#Front door mechanics - porch/entry room shared door.
door_open = False  #Starts locked - tracks if door locked/closed or unlocked/open
door_checked = False  #Has the player tried opening the front door - prevents re checking since now the door opens and they can enter instead
door_disappeared = False  #Entryway front door disappears when the player leaves the entryway - removes option to check door
front_door_warning_shown = False  #Checks disappeared = true and if so they get alerted the door vanished when they re enter entryway first time.

#======================================================================

#Puzzle trackers

#Fuse box
power_restored = False  #Tracks if the fuse puzzle is completed
fuse_box = ["Empty", "Empty", "Empty"]  #List stores fuses placed in the fuse box
incorrect_fuse_attempts = 0  #Tracks failed fuse puzzle attempts

#======================================================================

#Track whether the fuse order hint has been found
fuse_order_hint_found = False

#======================================================================

#Track whether the safe order hint has been found
safe_order_hint_found = False

#======================================================================

#Basement safe
safe_unlocked = False  #Tracks if the basement safe has been opened
incorrect_safe_attempts = 0  #Tracks failed safe puzzle attempts

#======================================================================

#Lockbox & Screwdriver Tracking
just_used_screwdriver = False  #Tracks if the lockbox was opened

#======================================================================

#Final door mechanics

#door ending appearance
final_door_appeared = False  #Tracks if the final ending door has spawned

#Has the player passed the point of no return?
final_sequence_started = False

#======================================================================

#End

#======================================================================

