import time
import pygame as pyme

pyme.init()
pyme.mixer.init()

ask = input("\nTimer for hours, minutes or seconds:")

def play_sound():
    try:
        pyme.mixer.music.load("/home/linux/Adi-Python/alarm_end.mp3")
        pyme.mixer.music.set_volume(1.0)
        pyme.mixer.music.play()
        while pyme.mixer.music.get_busy():
            pyme.time.Clock().tick(5)  # Keep the program running while the sound plays
    except pyme.error as e:
        print(f"Error playing sound: {e}")

def hour():
    ask_user_time2 = input("Enter for how many hours do you wanna run the timer:")
    print('')
    if ask_user_time2.isdigit():
        ask_user_time = int(ask_user_time2)
        ask_user_time = ask_user_time*60*60 +1
    else:
        print(ValueError("Invalid Input!"))
        print(f"Running timer for 1 hour.")
        ask_user_time = 1
        ask_user_time = ask_user_time*60*60 +1

    for i in range(1,ask_user_time):
        ask_user_time -= 1
        print(f"Countdown to {ask_user_time2} hours/hour is on:{ask_user_time} or {ask_user_time/60:.2f} minutes.")
        time.sleep(1)

    print("\nAlarm Ended!")
    play_sound()

def min():
    ask_user_time2 = input("Enter for how many minutes do you wanna run the timer:")
    print('')
    if ask_user_time2.isdigit():
        ask_user_time = int(ask_user_time2)
        ask_user_time = ask_user_time*60 +1
    else:
        print(ValueError("Invalid Input!"))
        print(f"Running timer for 5 minutes.")
        ask_user_time = 5
        ask_user_time = ask_user_time*60 +1
    
    if int(ask_user_time2) > 60:
        print("It is not in minutes running in hours.\n")
        hour()
    else:
        pass

    for i in range(1,ask_user_time):
        ask_user_time -= 1
        print(f"Countdown to {ask_user_time2} minutes/minute is on:{ask_user_time} or {ask_user_time/60:.2f} minutes.")
        time.sleep(1)

    print("\nAlarm Ended!")
    play_sound()

def sec():
    ask_user_time2 = input("Enter for how many seconds do you wanna run the timer:")
    print('')
    if ask_user_time2.isdigit():
        ask_user_time = int(ask_user_time2) +1
    else:
        print(ValueError("Invalid Input!"))
        print(f"Running timer for 30 seconds.")
        ask_user_time = 30 +1
    
    if int(ask_user_time2) > 60:
        print("It is in minutes running in minutes.\n")
        min()
    else:
        pass

    for i in range(1,ask_user_time):
        ask_user_time -= 1
        print(f"Countdown to {ask_user_time2} seconds/second is on:{ask_user_time}.")
        time.sleep(1)

    print("\nAlarm Ended!")
    play_sound()

if ask.lower() in ["hour","h","hours"]:
    hour()
elif ask.lower() in ["minutes","m","min","minute"]:
    min()
elif ask.lower() in ["seconds","s","sec","second"]:
    sec()
else:
    print(ValueError("\nInvalid Input!\n"))
    print("Running for seconds.")
    sec()
