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
        
        if setting == 'city':
            city_adventure()
        elif setting == 'desert':
            desert_adventure()
        else:
            print('Invalid response. The journey ends here.')
            quit()
            
    elif leave == 'stay':
        print("You decide to stay in the vault, hoping the Overseer finds another way to secure the dwindling resources.")
        print("Days turn into weeks, and the supplies continue to dwindle. Eventually, the vault is forced to close its doors forever, sealing your fate.")
        quit()
        
    else:
        print('Invalid response. The vault’s doors remain shut, and your fate is sealed.')
        quit()


def city_adventure():
    print("You decide to head towards the city. The closer you get, the more desolate and decayed the environment becomes. Towering, crumbling skyscrapers loom overhead, casting long shadows over the cracked asphalt.")
    print("The streets are littered with debris and the remnants of a once-thriving metropolis. The silence is almost deafening, save for the occasional gust of wind that sends dust swirling through the air.")
    
    response = input("There are towering structures all around. Do you want to venture deeper or make camp here? (venture/camp) ").lower()
    
    if response == 'venture':
        print("You gather your courage and walk deeper into the dark and damp city, navigating through narrow alleyways and deserted streets.")
        print("After hours of cautious exploration, you spot a camp of raiders nearby. The flickering light of their fire illuminates their makeshift encampment among the ruins.")
        
        encounter = input("Do you sneak around them or ambush their camp? (sneak/ambush) ").lower()
        
        if encounter == 'sneak':
            print("You move quietly, slipping past the raiders while they argue over the spoils of their latest raid.")
            print("Your heart pounds in your chest, but your stealth pays off as you successfully avoid danger and continue your journey deeper into the city.")
            next_area()
        
        elif encounter == 'ambush':
            print("With stealth and precision, you prepare your weapons and toss grenades into their camp. The explosion echoes through the empty streets.")
            print("The raiders never stood a chance. You gather valuable loot from their remains, including supplies and weapons.")
            print("The city is a little safer now, but the dangers are far from over.")
            next_area()
        
        else:
            print("Invalid response. You hesitate, and the raiders awaken, catching you off guard...")
            print("The last thing you hear is the sound of gunfire echoing through the empty streets. You didn't make it out alive.")
            quit()
    
    elif response == 'camp':
        print("You decide to set up camp in a relatively sheltered spot, a small alcove tucked between two ruined buildings. The remnants of an old sign creak in the wind above you.")
        print("You light a small fire, hoping to remain unnoticed in the sprawling darkness of the city. The night is quiet, but the city never truly sleeps.")
        print("You gain some much-needed rest, but you know you can't stay here forever. Tomorrow, you'll have to keep moving.")
        next_area()
    
    else:
        print("Invalid response. The city's dangers overwhelm you as the shadows close in...")
        quit()


def desert_adventure():
    print("You decide to venture into the barren desert wastes. The sun beats down relentlessly as you leave the ruins of the city behind.")
    print("The desert stretches endlessly, a sea of shifting sands and rocky outcrops. The heat is oppressive, and every step feels like a struggle.")
    
    response = input("The desert stretches endlessly. Do you venture onward or make camp? (venture/camp) ").lower()
    
    if response == 'venture':
        print("You walk for hours under the scorching sun, your throat dry and your skin blistered. Just when you think you can't go any further, you notice a faint shimmer in the distance.")
        print("As you draw closer, you realize it's not a mirage but an oasis, hidden among towering dunes. However, something feels off about this place.")
        
        explore_oasis = input("Do you explore the oasis or continue through the desert? (explore/continue) ").lower()
        
        if explore_oasis == 'explore':
            print("You cautiously approach the oasis, the cool shade of palm trees a welcome relief. But as you bend down to drink from the crystal-clear pool, you hear a low growl.")
            print("A massive, mutated creature, part scorpion and part lizard, emerges from the shadows, its many eyes glinting in the sunlight.")
            
            fight_or_flee = input("Do you fight the creature or flee? (fight/flee) ").lower()
            
            if fight_or_flee == 'fight':
                print("You draw your weapon and engage in a fierce battle with the mutant beast. Its pincers snap dangerously close, but with skill and determination, you manage to land a fatal blow.")
                print("As the creature collapses, you notice a small, hidden entrance behind where it was guarding. Perhaps there’s more to this oasis than meets the eye...")
                print("You discover an underground cave, filled with ancient technology and forgotten treasures from before the war.")
                next_area()
            
            elif fight_or_flee == 'flee':
                print("Realizing you're outmatched, you sprint away from the oasis as the creature gives chase. The adrenaline pumps through your veins, but you manage to lose it among the dunes.")
                print("You survive, but the encounter has left you shaken and exhausted. The desert's dangers are ever-present, and you must stay alert.")
                next_area()
            
            else:
                print("Invalid response. The creature's attack catches you off guard, and you fall to the ground, its venomous sting delivering a swift end to your journey.")
                quit()
        
        elif explore_oasis == 'continue':
            print("You decide to play it safe and continue your journey through the desert. The heat is relentless, and the landscape unforgiving, but you press on.")
            print("Eventually, you stumble upon the remnants of an old caravan, half-buried in the sand. You find some supplies, but the question remains: what happened to the travelers?")
            print("As night falls, you make camp nearby, keeping a wary eye on the surrounding darkness.")
            next_area()
        
        else:
            print("Invalid response. The desert's mysteries remain unsolved, and you are lost to the sands...")
            quit()
    
    elif response == 'camp':
        print("You decide to set up camp in the sand, creating a small fire to keep warm as the temperature drops. The desert night is eerily silent, with only the occasional howl of a distant creature breaking the stillness.")
        print("As you drift off to sleep, you're awakened by a strange noise. A sandstorm is approaching, and it's moving fast.")
        
        sandstorm_response = input("Do you try to find shelter or brave the storm? (shelter/brave) ").lower()
        
        if sandstorm_response == 'shelter':
            print("You quickly pack up your camp and search for shelter, finding a small cave just in time. The storm rages outside, but you're safe inside.")
            print("As you wait for the storm to pass, you notice strange markings on the cave walls. They seem to tell the story of an ancient civilization that once thrived in this desert.")
            next_area()
        
        elif sandstorm_response == 'brave':
            print("You decide to brave the storm, covering your face and marching forward into the howling wind. The sand whips at your skin, and the storm feels endless.")
            print("When it finally subsides, you're left disoriented and exhausted, but you've made it through. You notice the landscape has changed, revealing new paths and hidden secrets.")
            next_area()
        
        else:
            print("Invalid response. The sandstorm engulfs you, and you are lost to the desert...")
            quit()
    
    else:
        print("Invalid response. The desert swallows you whole...")
        quit()


def next_area():
    print("The journey continues...")

# Start the game
start_game()
