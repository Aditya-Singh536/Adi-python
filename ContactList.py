def gain_details():
    sim1 = {"A":845845, "B":34983}
    ask_name = input('\nPlase enter the name of the peron whose number has to be stored:') 
    ask_phone_num = input('Give the phone number of the person to save:')    
    def contact_list():

        #Add details:  
            
        sim1[ask_name] = ask_phone_num #type:ignore
        ask_user = input('\nDo you want to store one more number? (Yes/No):')
        if ask_user.lower() == 'yes':
            gain_details()
        else:
            print('Your details have been stored!\n')


        #Search details:

        ask_user_searching = input('Do you want to search? (Yes/No):')
        if ask_user_searching.lower() == 'yes':
            ask_user_search_name = input('\nPlease provide the name of the number to search:')
            if ask_user_search_name in sim1:
                print(sim1.__getitem__(ask_user_search_name),f'Is the number of {ask_user_search_name}.')
                print('The search has been given!')
            else:
                print('The person doesn\'t exist in your contact list.')
        elif ask_user_searching.lower() == 'no':
            print('Okay!')  
        else:
            print('Invalid Input!')    


        #Delete details:

        ask_user_delete = input('\nDo you want to delete? (Yes/No):')
        if ask_user_delete.lower() == 'yes':
            ask_user_delete_name = input('\nPlease provide the name of the number to delete:')
            print(sim1, "before deletion")
            if ask_user_delete_name in sim1:
                #del sim1[ask_user_delete_name]
                sim1.pop(ask_user_delete_name)
                print(sim1)
                print('Your deletion has been done.')
                ask_user_continuation = input('Do you want to continue? (Yes/No):')
                if ask_user_continuation.lower() == 'yes':
                    gain_details()
                elif ask_user_continuation.lower() == 'no':
                    print('Okay!')
                else:
                    print('Invalid Input!')   
            else:
                print('There is no such person in your contact list!') 
                ask_user_continuation = input('Do you want to continue? (Yes/No):')
                if ask_user_continuation.lower() == 'yes':
                    gain_details()
                elif ask_user_continuation.lower() == 'no':
                    print('Okay!')
                else:
                    print('Invalid Input!')     
        elif ask_user_delete.lower() == 'no':
            print('Okay!')
            ask_user_continuation = input('Do you want to continue? (Yes/No):')
            if ask_user_continuation.lower() == 'yes':
                gain_details()
            elif ask_user_continuation.lower() == 'no':
                print('Okay!')
            else:
                print('Invalid Input!')   
        else:
            print('Invalid Input!')         

    if len(ask_phone_num) ==  10:
        contact_list()
    elif len(ask_phone_num) > 10 or len(ask_phone_num) < 10:
        print('Invalid INDIAN Phone Number!')
    else:
        print('Invalid Input!')

    if ask_phone_num.isnumeric():
        contact_list()
    else:
        print('Invalid Input!')    

gain_details()