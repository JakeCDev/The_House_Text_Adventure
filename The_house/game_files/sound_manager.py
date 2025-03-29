#======================================================================
# Sound Manager
# sound_manager.py
#======================================================================

#Imports
import os
import pygame
from color_scheme import RED, RESET

#======================================================================

#Initialize mixer and set total channels (e.g. 16 channels for flexibility)
pygame.mixer.init()
pygame.mixer.set_num_channels(16)

#======================================================================

#Paths and helpers
SOUND_DIR = os.path.join(os.path.dirname(__file__), "sounds")

#======================================================================

#Tracks looping ambient sounds by name
looping_channels = {}

#======================================================================

#Load a sound file safely
def load_sound(filename):
    path = os.path.join(SOUND_DIR, filename)
    if not os.path.exists(path):
        print(f"{RED}Sound file not found: {filename}{RESET}")
        return None
    return pygame.mixer.Sound(path)

#======================================================================

#Music (single track, uses mixer.music)
def play_music(filename, volume=0.5, fade_in=1000):
    path = os.path.join(SOUND_DIR, filename)
    if os.path.exists(path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1, fade_ms=fade_in)  #Loop w/ fade in
    else:
        print(f"{RED}Music file not found: {filename}{RESET}")

#======================================================================

#force stop music with fade out
def stop_music(fade_out=1000):
    pygame.mixer.music.fadeout(fade_out)  #Fade out music over X ms

#======================================================================

#One time Sound Effects
def play_sound_effect(filename, volume=1.0):
    sound = load_sound(filename)
    if sound:
        sound.set_volume(volume)
        sound.play()

#======================================================================

#Ambient Loops (ex - rain / wind)
def play_ambient_loop(name, filename, volume=0.6):
    #If the sound is already playing on a valid channel, don't restart it
    if name in looping_channels:
        channel = looping_channels[name]
        if channel.get_busy():  # It's still playing
            return  #Don't restart, avoid harsh stop/restart

    #Otherwise, load and start the sound
    sound = load_sound(filename)
    if sound:
        channel = pygame.mixer.find_channel()
        if channel:
            channel.set_volume(volume)
            channel.play(sound, loops=-1)
            looping_channels[name] = channel
        else:
            print(f"{RED}No free channel available for ambient loop: {name}{RESET}")

#======================================================================

#change ambient volumes
def set_ambient_volume(name, volume):
    if name in looping_channels:
        looping_channels[name].set_volume(volume)
    else:
        print(f"{RED}Cannot set volume — ambient loop not found: {name}{RESET}")

#======================================================================

#force stop a loop
def stop_ambient_loop(name, fade_out=1000):
    if name in looping_channels:
        looping_channels[name].fadeout(fade_out)
        del looping_channels[name]

#======================================================================

#Stop all currently playing ambient loops
def stop_all_ambient():
    for name in list(looping_channels.keys()):
        stop_ambient_loop(name)

#======================================================================

#sound fix for debug teleporting
def sync_ambient_to_room(room_name, sound_map):
    import pygame
    from game_states import room_sound_map  #Local import to avoid circular import

    #Stop current music
    pygame.mixer.music.stop()

    #Stop all ambient loops using the helper
    stop_all_ambient()

    #Get sound config for the target room
    room_sounds = room_sound_map.get(room_name, {})

    #Start new music if defined
    music_data = room_sounds.get("music")
    if music_data:
        music_file, music_volume = music_data
        play_music(music_file, volume=music_volume)

    #Start defined ambient loops
    ambient_loops = room_sounds.get("ambience", {})
    for name, (file, volume) in ambient_loops.items():
        play_ambient_loop(name, file, volume)

#======================================================================

#End

#======================================================================