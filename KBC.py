q = {'Q1':'Slowest animal in the world',
     'Q2':'Fastest car'}
a = {'A1':'a.Sloth  b.Turtle',
     'A2':'a.Chiron b.Jesko'}

c = q[input('Which question Q1 or Q2 :')]

if c == q['Q1']:
    print(q['Q1'])
    print(a['A1'])
    x = input('Ans:')
    if x == 'Sloth':
        print('Correct')
    elif x == 'Turtle':
        print('Incorrect')
elif c == q['Q2']:
    print(q['Q2'])
    print(a['A2'])
    y = input('Ans:')
    if y == 'Chiron':
        print('Incorrect')
    elif y == 'Jesko':
        print('Correct')
