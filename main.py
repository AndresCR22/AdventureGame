name = input('Enter your name vault dweller: ')
print(f'Greetings {name}, and welcome to Vault 25!')

start = input('Would you rather play the game or die? ')
if start == 'play':
    print('Great! Let\'s play the game! ')
    setting = input('Want to go to the city or desert? ')
else:
    print('End...')
    quit()
    
if setting == 'city':
    print('Welcome to the mighty city!')
    response = input('There are great structures all around, should you venture or make camp? ')
    if response == 'venture':
        print('You walk deeper into the dark and damp city...')
        transport = input('You see a camp of raiders nearby, sneak around or ambush them?')
        if transport == 'sneak':
            print('With them sleeping, you easily sneak around...')
        elif transport == 'ambush':
            print('With them sleeping, you throw grandes in their camp and whipe them out...')
        else:
            print('invalid response')
            quit()
    elif response == 'make camp':
        print('You create a fire and ready your bed roll...')
    else:
        print('invalid response')
        quit()
        
elif setting == 'desert':
    print('Welcome to the baren desert wastes!')
    response = input('There is nothing but sand, should you venture or make camp? ')
    if response == 'venture':
        print('You walk for a few miles until you see a faint structure in the distance...')
    elif response == 'make camp':
        print('You create a fire and ready your bed roll...')
    else:
        print('invalid response')
        quit()
        
else:
    quit()