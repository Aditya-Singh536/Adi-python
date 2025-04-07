import time

ask = input("Timer for hours, minutes or seconds:")

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

    print("\nBEEP BEEP!")

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

    for i in range(1,ask_user_time):
        ask_user_time -= 1
        print(f"Countdown to {ask_user_time2} minutes/minute is on:{ask_user_time} or {ask_user_time/60:.2f} minutes.")
        time.sleep(1)

    print("\nBEEP BEEP!")

def sec():
    ask_user_time2 = input("Enter for how many seconds do you wanna run the timer:")
    print('')
    if ask_user_time2.isdigit():
        ask_user_time = int(ask_user_time2) +1
    else:
        print(ValueError("Invalid Input!"))
        print(f"Running timer for 30 seconds.")
        ask_user_time = 30 +1

    for i in range(1,ask_user_time):
        ask_user_time -= 1
        print(f"Countdown to {ask_user_time2} seconds/second is on:{ask_user_time}.")
        time.sleep(1)

    print("\nBEEP BEEP!")

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