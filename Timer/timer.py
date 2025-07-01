import time
import pygame as pyme

pyme.init()
pyme.mixer.init()

ask = input("Enter how long should the timer run:")
if ask.isdigit():
    ask = int(ask)
else:
    raise Exception("Invalid Input!")

print("")

for i in range(ask, 0, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    time.sleep(1)

print("\nCountdown is over!!")


def play_sound():
    try:
        pyme.mixer.music.load(
            "/home/user/Adi-python/Timer/timer_end.mp3"
        )  #! IMPORTANT: Replace this with the actual path to your MP3 file.
        pyme.mixer.music.set_volume(1.0)
        pyme.mixer.music.play(3)

        while pyme.mixer.music.get_busy():
            pyme.time.Clock().tick(5)  # Keep the program running while the sound plays

    except pyme.error as error:
        print(f"Error playing sound: {error}")


play_sound()
