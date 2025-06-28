import time
import pygame as pyme

pyme.init()
pyme.mixer.init()

ask = input("\nTimer for hours, minutes or seconds:")


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


def hour():
    ask_user_time2 = input("Enter for how many hours do you wanna run the timer:")
    print("")

    if ask_user_time2.isdigit():
        ask_user_time = int(ask_user_time2)
        ask_user_time = ask_user_time * 60 * 60
    else:
        print(ValueError("Invalid Input!"))
        print(f"Running timer for 1 hour.")
        ask_user_time = 1
        ask_user_time = ask_user_time * 60 * 60

    for i in range(1, ask_user_time):
        ask_user_time -= 1
        print(
            f"Countdown to {ask_user_time2} hours/hour is on:{ask_user_time/60:.2f} minutes."
        )
        time.sleep(1)

    print("\nTimer Ended!")
    play_sound()


def min():
    ask_user_time2 = input("Enter for how many minutes do you wanna run the timer:")
    print("")

    if ask_user_time2.isdigit():
        ask_user_time = int(ask_user_time2)
        ask_user_time = ask_user_time * 60
    else:
        print(ValueError("Invalid Input!"))
        print(f"Running timer for 5 minutes.")
        ask_user_time = 5
        ask_user_time = ask_user_time * 60

    for i in range(1, ask_user_time):
        ask_user_time -= 1
        print(
            f"Countdown to {ask_user_time2} minutes/minute is on:{ask_user_time} seconds or {ask_user_time/60:.2f} minutes."
        )
        time.sleep(1)

    print("\nTimer Ended!")
    play_sound()


def sec():
    ask_user_time2 = input("Enter for how many seconds do you wanna run the timer:")
    print("")

    if ask_user_time2.isdigit():
        ask_user_time = int(ask_user_time2)
    else:
        print(ValueError("Invalid Input!"))
        print(f"Running timer for 30 seconds.")
        ask_user_time = 30

    for i in range(1, ask_user_time):
        ask_user_time -= 1
        print(f"Countdown to {ask_user_time2} seconds/second is on:{ask_user_time}.")
        time.sleep(1)

    print("\nTimer Ended!")
    play_sound()


if ask.lower() in ["hour", "h", "hours"]:
    hour()
elif ask.lower() in ["minutes", "m", "min", "minute"]:
    min()
elif ask.lower() in ["seconds", "s", "sec", "second"]:
    sec()
else:
    print(ValueError("\nInvalid Input!\n"))
    print("Running for seconds.")
    sec()
