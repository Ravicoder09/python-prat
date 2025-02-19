weight=int(input('what is your weight'))
unit=input("is your weight is in lbs or kgs ")
if unit == 'kg' or unit == 'KG' or unit == 'Kg':
    weight1=weight*2.2
    print(f'{weight1} is your weight in lbs')
elif unit == 'lbs' or unit == 'LBS' or unit == 'LBs' or unit == 'Lbs':
    weight2=weight/2.2
    print(f'{weight2} is nyour weight in kgs')
else:
    print('your input is not corect')


command=""
while command != 'quit':
    command=input(">")
    if command == 'start':
        print('game is start')
    elif command == 'stop':
        print('game is paused')
    elif command == 'help':
        print('''start -  to start the game
              stop - to pause the game 
              quit - to end the game''')
    elif command == 'quit':
        print('game ends here')
        break
    else:
        print('your input is wrong type help to know the available inputs')              