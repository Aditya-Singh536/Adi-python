import time
import pygame as pyme

pyme.init()
pyme.mixer.init()

def play_sound():
    try:
        pyme.mixer.music.load(
            "/home/user/Adi-python/Timer/timer_end.mp3"
        )  # Your choice of BEEP. Give the path. I've provided some.

        pyme.mixer.music.set_volume(1.0)
        pyme.mixer.music.play(3)

        while pyme.mixer.music.get_busy():
            pyme.time.Clock().tick(5)  # Keep the program running while the sound plays

    except pyme.error as error:
        print(f"Error playing sound: {error}")

get_time = print("What time to set the alarm at?")