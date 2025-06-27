def kbc_game():
    question = {"q1": "\nSlowest animal in the world", "q2": "\nFastest car"}
    answer = {"a1": "a.Sloth  b.Turtle", "a2": "a.Chiron b.Jesko"}

    ask = input("Which question Q1 or Q2 :").lower().strip()

    while ask == "q1" or ask == "q2":
        if ask == "q1":
            print(question["q1"])
            print(answer["a1"])
            ask = input("Ans:").lower().strip()
            if ask == "sloth" or "a.sloth" or "a":
                print("\nCorrect")
            elif ask == "turtle" or "b.turtle" or "b":
                print("\nIncorrect")
        elif ask == "q2":
            print(question["q2"])
            print(answer["a2"])
            ask = input("Ans:").lower().strip()
            if ask == "chiron" or "a.chiron" or "a":
                print("\nIncorrect")
            elif ask == "Jesko" or "b.jesko" or "b":
                print("\nCorrect")
        else:
            raise Exception("**Invalid Input**")

kbc_game()

ak = input("\nDo you want to play again? (yes/no): ").lower().strip()
if ak == "yes":
    print("Restarting the game...")
    kbc_game()
elif ak == "no":
    print("Thank you for playing!")
else:
    print("**Invalid Input**")
