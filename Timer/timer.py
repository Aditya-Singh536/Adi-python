import time
import pygame as pyme

pyme.init()
pyme.mixer.init()

ask = input("Enter how log should the timer run:")
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
        )  # Your choice of BEEP. Give the path.

        pyme.mixer.music.set_volume(1.0)
        pyme.mixer.music.play(5)

        while pyme.mixer.music.get_busy():
            pyme.time.Clock().tick(5)  # Keep the program running while the sound plays

    except pyme.error as error:
        print(f"Error playing sound: {error}")


play_sound()
