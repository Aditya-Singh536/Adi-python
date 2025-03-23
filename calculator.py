print('What do you want to do?.Add,Substract,Multiply or Divide.Give the values.\n')

def calculater():
    try:
        first_num = float(input('First number:'))
        second_num = float(input('Second number:'))
    
        taking_input = input('Press a to add,s to substract,m to multiply and d to divide:')

    #Main programing

    
        if taking_input.lower() == 'a':
            print(f'{first_num + second_num} is the sum of {first_num} + {second_num}.')
        elif taking_input.lower() == 's':
            print(f'{first_num - second_num} is the diffrence of {first_num} - {second_num}.')
        elif taking_input.lower() == 'm':
            print(f'{first_num * second_num} is the product of {first_num} x {second_num}.')
        elif taking_input.lower() == 'd':
            print(f'{(first_num / second_num).__round__(2)} is the quotient of {first_num} ÷ {second_num} and the remainder is {first_num % second_num}.')
    except:
        print(ValueError('Invalid Input!')) 

calculater()