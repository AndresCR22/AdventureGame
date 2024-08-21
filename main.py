def start_game():
    # Introduction
    print("The year is 2281. You've lived your entire life in Vault 25, a massive underground shelter built to protect you from the nuclear devastation above.")
    print("But now, resources are dwindling, and the Vault Overseer has given you a choice: venture into the dangerous world above or remain in the vault, risking starvation.")
    
    # Player Name Input
    name = input('Enter your name, vault dweller: ')
    print(f'Greetings, {name}. Your fate is in your hands.')

    # Decision to Leave the Vault or Stay
    leave = input('Will you leave the vault to search for supplies or stay and face the consequences? (leave/stay) ').lower()
    
    if leave == 'leave':
        print("You gather your gear, knowing there's no turning back. The heavy vault door groans as it opens, revealing the harsh world outside.")
        print("As you step into the blinding sunlight, you see a barren desert stretching endlessly before you, and in the distance, the ruins of a city loom on the horizon.")
        setting = input('Where will you go? The city or the desert? (city/desert) ').lower()
    elif leave == 'stay':
        print("You decide to stay in the vault, hoping the Overseer finds another way to secure the dwindling resources.")
        print("Days turn into weeks, and the supplies continue to dwindle. Eventually, the vault is forced to close its doors forever, sealing your fate.")
        quit()
    else:
        print('Invalid response. The vault’s doors remain shut, and your fate is sealed.')
        quit()

    if setting == 'city':
        city_adventure()
    elif setting == 'desert':
        desert_adventure()
    else:
        print('Invalid response. The journey ends here.')
        quit()

def city_adventure():
    print('Welcome to the mighty city!')
    response = input('There are towering structures all around. Do you want to venture deeper or make camp here? (venture/camp) ').lower()
    if response == 'venture':
        print('You walk deeper into the dark and damp city...')
        encounter = input('You spot a camp of raiders nearby. Do you sneak around them or ambush their camp? (sneak/ambush) ').lower()
        if encounter == 'sneak':
            print('You move quietly, slipping past the raiders while they sleep...')
            print('You successfully avoid danger and continue your journey.')
        elif encounter == 'ambush':
            print('With stealth and precision, you toss grenades into their camp, wiping them out...')
            print('The city is a little safer now, and you gain valuable loot.')
        else:
            print('Invalid response. You hesitate, and the raiders awaken, catching you off guard...')
            print('You didn\'t make it out alive.')
            quit()
    elif response == 'camp':
        print('You set up camp and light a small fire, hoping to remain unnoticed...')
        print('The night is quiet, but the city never truly sleeps. You gain some much-needed rest.')
    else:
        print('Invalid response. The city\'s dangers overwhelm you...')
        quit()

def desert_adventure():
    print('Welcome to the barren desert wastes!')
    response = input('The desert stretches endlessly. Do you venture onward or make camp? (venture/camp) ').lower()
    if response == 'venture':
        print('You walk for miles under the scorching sun until you see a faint structure in the distance...')
        approach = input('The structure looks abandoned, but could be shelter. Do you approach it or stay away? (approach/stay) ').lower()
        if approach == 'approach':
            print('You cautiously approach the structure. It\'s an old, crumbling bunker...')
            print('Inside, you find some supplies and a place to rest. This could be a temporary base of operations.')
        elif approach == 'stay':
            print('You decide it\'s safer to avoid the structure and continue on...')
            print('But the desert is unforgiving, and you find yourself lost and dehydrated...')
            print('Without shelter, the odds are against you.')
            quit()
        else:
            print('Invalid response. The desert\'s harshness claims another victim...')
            quit()
    elif response == 'camp':
        print('You set up camp in the sand, creating a small fire to keep warm as the temperature drops...')
        print('The desert night is eerily silent, and you manage to get some rest before continuing your journey.')
    else:
        print('Invalid response. The desert swallows you whole...')
        quit()

# Start the game
start_game()
