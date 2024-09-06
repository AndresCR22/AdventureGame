def start_game():
    # Introduction to the game's story and setting
    print("The year is 2281. You've lived your entire life in Vault 25, a massive underground shelter built to protect you from the nuclear devastation above.")
    print("But now, resources are dwindling, and the Vault Overseer has given you a choice: venture into the dangerous world above or remain in the vault, risking starvation.")
    
    # Prompt the player to enter their name
    name = input('Enter your name, vault dweller: ')
    print(f'Greetings, {name}. Your fate is in your hands.')

    # Ask the player whether they want to leave the vault or stay
    leave = input('Will you leave the vault to search for supplies or stay and face the consequences? (leave/stay) ').lower()
    
    if leave == 'leave':
        # If the player chooses to leave the vault
        print("You gather your gear, knowing there's no turning back. The heavy vault door groans as it opens, revealing the harsh world outside.")
        print("As you step into the blinding sunlight, you see a barren desert stretching endlessly before you, and in the distance, the ruins of a city loom on the horizon.")
        # Ask the player where they want to go first: the city or the desert
        setting = input('Where will you go first? The city or the desert? (city/desert) ').lower()
        
        if setting == 'city':
            city_adventure(first=True)
        elif setting == 'desert':
            desert_adventure(first=True)
        else:
            # Handle invalid input
            print('Invalid response. The journey ends here.')
            quit()
            
    elif leave == 'stay':
        # If the player chooses to stay in the vault
        print("You decide to stay in the vault, hoping the Overseer finds another way to secure the dwindling resources.")
        print("Days turn into weeks, and the supplies continue to dwindle. Eventually, the vault is forced to close its doors forever, sealing your fate.")
        quit()
        
    else:
        # Handle invalid input
        print('Invalid response. The vault’s doors remain shut, and your fate is sealed.')
        quit()
        
def city_adventure(first=False):
    # Description of the player's journey to the city
    print("You decide to head towards the city. The closer you get, the more desolate and decayed the environment becomes. Towering, crumbling skyscrapers loom overhead, casting long shadows over the cracked asphalt.")
    print("The streets are littered with debris and the remnants of a once-thriving metropolis. The silence is almost deafening, save for the occasional gust of wind that sends dust swirling through the air.")
    
    # Ask the player whether they want to venture deeper into the city or make camp
    response = input("There are towering structures all around. Do you want to venture deeper or make camp here? (venture/camp) ").lower()
    
    if response == 'venture':
        # If the player chooses to venture deeper into the city
        print("You gather your courage and walk deeper into the dark and damp city, navigating through narrow alleyways and deserted streets.")
        print("After hours of cautious exploration, you spot a camp of raiders nearby. The flickering light of their fire illuminates their makeshift encampment among the ruins.")
        
        # Ask the player whether they want to sneak around the raiders or ambush their camp
        encounter = input("Do you sneak around them or ambush their camp? (sneak/ambush) ").lower()
        
        if encounter == 'sneak':
            # If the player chooses to sneak around the raiders
            print("You move quietly, slipping past the raiders while they argue over the spoils of their latest raid.")
            print("Your heart pounds in your chest, but your stealth pays off as you successfully avoid danger and continue your journey deeper into the city.")
            next_area()
        
        elif encounter == 'ambush':
            # If the player chooses to ambush the raiders
            print("With stealth and precision, you prepare your weapons and toss grenades into their camp. The explosion echoes through the empty streets.")
            print("The raiders never stood a chance. You gather valuable loot from their remains, including supplies and weapons.")
            print("The city is a little safer now, but the dangers are far from over.")
            next_area()
        
        else:
            # Handle invalid input
            print("Invalid response. You hesitate, and the raiders awaken, catching you off guard...")
            print("The last thing you hear is the sound of gunfire echoing through the empty streets. You didn't make it out alive.")
            quit()
    
    elif response == 'camp':
        # If the player chooses to make camp in the city
        print("You decide to set up camp in a relatively sheltered spot, a small alcove tucked between two ruined buildings. The remnants of an old sign creak in the wind above you.")
        print("You light a small fire, hoping to remain unnoticed in the sprawling darkness of the city. The night is quiet, but the city never truly sleeps.")
        print("You gain some much-needed rest, but you know you can't stay here forever. Tomorrow, you'll have to keep moving.")
        if first:
            next_area(destination='desert')
    else:
        # Handle invalid input
        print("Invalid response. The city's dangers overwhelm you as the shadows close in...")
        quit()

def desert_adventure(first=False):
    # Description of the player's journey into the desert
    print("You decide to venture into the barren desert wastes. The sun beats down relentlessly as you leave the ruins of the city behind.")
    print("The desert stretches endlessly, a sea of shifting sands and rocky outcrops. The heat is oppressive, and every step feels like a struggle.")
    
    # Ask the player whether they want to venture onward or make camp in the desert
    response = input("The desert stretches endlessly. Do you venture onward or make camp? (venture/camp) ").lower()
    
    if response == 'venture':
        # If the player chooses to venture onward in the desert
        print("You walk for hours under the scorching sun, your throat dry and your skin blistered. Just when you think you can't go any further, you notice a faint shimmer in the distance.")
        print("As you draw closer, you realize it's not a mirage but an oasis, hidden among towering dunes. However, something feels off about this place.")
        
        # Ask the player whether they want to explore the oasis or continue through the desert
        explore_oasis = input("Do you explore the oasis or continue through the desert? (explore/continue) ").lower()
        
        if explore_oasis == 'explore':
            # If the player chooses to explore the oasis
            print("You cautiously approach the oasis, the cool shade of palm trees a welcome relief. But as you bend down to drink from the crystal-clear pool, you hear a low growl.")
            print("A massive, mutated creature, part scorpion and part lizard, emerges from the shadows, its many eyes glinting in the sunlight.")
            
            # Ask the player whether they want to fight the creature or flee
            fight_or_flee = input("Do you fight the creature or flee? (fight/flee) ").lower()
            
            if fight_or_flee == 'fight':
                # If the player chooses to fight the creature
                print("You draw your weapon and engage in a fierce battle with the mutant beast. Its pincers snap dangerously close, but with skill and determination, you manage to land a fatal blow.")
                print("As the creature collapses, you notice a small, hidden entrance behind where it was guarding. Perhaps there’s more to this oasis than meets the eye...")
                print("You discover an underground cave, filled with ancient technology and forgotten treasures from before the war.")
                next_area()
            
            elif fight_or_flee == 'flee':
                # If the player chooses to flee from the creature
                print("Realizing you're outmatched, you sprint away from the oasis as the creature gives chase. The adrenaline pumps through your veins, but you manage to lose it among the dunes.")
                print("You survive, but the encounter has left you shaken and exhausted. The desert's dangers are ever-present, and you must stay alert.")
                next_area()
            
            else:
                # Handle invalid input
                print("Invalid response. The creature's attack catches you off guard, and you fall to the ground, its venomous sting delivering a swift end to your journey.")
                quit()
        
        elif explore_oasis == 'continue':
            # If the player chooses to continue through the desert
            print("You decide to play it safe and continue your journey through the desert. The heat is relentless, and the landscape unforgiving, but you press on.")
            print("Eventually, you stumble upon the remnants of an old caravan, half-buried in the sand. You find some supplies, but the question remains: what happened to the travelers?")
            print("As night falls, you make camp nearby, keeping a wary eye on the surrounding darkness.")
            next_area()
        
        else:
            # Handle invalid input
            print("Invalid response. The desert's mysteries remain unsolved, and you are lost to the sands...")
            quit()
    
    elif response == 'camp':
        # If the player chooses to make camp in the desert
        print("You decide to set up camp in the sand, creating a small fire to keep warm as the temperature drops. The desert night is eerily silent, with only the occasional howl of a distant creature breaking the stillness.")
        print("You sleep fitfully, aware of the countless dangers lurking in the shadows. But by dawn, you're ready to continue your journey.")
        if first:
            next_area(destination='city')
    else:
        # Handle invalid input
        print("Invalid response. The desert swallows you whole as you struggle to find your way...")
        quit()

def next_area(destination=None):
    if destination:
        if destination == 'desert':
            desert_adventure()
        elif destination == 'city':
            city_adventure()
        else:
            print("Your path is uncertain, and you wander aimlessly, eventually succumbing to the harsh realities of the wasteland.")
            quit()
    else:
        # Ask the player where they want to go next after completing an area
        setting = input('Where will you go next? The city or the desert? (city/desert) ').lower()
        
        if setting == 'city':
            city_adventure()
        elif setting == 'desert':
            desert_adventure()
        else:
            # Handle invalid input
            print("Invalid response. You lose your way in the wasteland, and your journey ends here.")
            quit()

start_game()
