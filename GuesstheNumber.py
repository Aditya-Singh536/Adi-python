import random as roam

def guess_num():

    ask = input('Do you wanna play this game? (Yes/No):')
    if ask.lower() == 'yes':

        guess = roam.choice(range(1,1001))
        ask_user = input('\nEnter the number you geussed (The range is from 1 to 1000):')

        if ask_user.isnumeric():
            ask_user = int(ask_user)

            if ask_user > 1000:
                print(ValueError('\nInvalid Input! The input can\'t go beond 1000'))
            else:    
                if ask_user == guess:
                    print('\nYou geussed the number right!')

                elif ask_user !=  guess:
                    print(f'\nThe number was {guess}.\nThe number changed!')
                    guess_num()
        else:
            print(ValueError('\nInvalid Input!'))

    elif ask.lower() == 'no':
        print('Just try once')
        ask2 = input('Do you want to play? (Yes/No):')
        if ask2.lower() == 'yes':
            print('\nYou are the pro who doen\'t want to show your levels.')
            guess_num()
        elif ask2.lower() == 'no':
            print('\nYou are the person who will become the greatest noob of the world.')
        else:
            print(ValueError('\nInvalid Input!'))    

guess_num()        
