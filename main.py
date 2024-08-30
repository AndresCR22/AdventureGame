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
        setting = input('Where will you go first? The city or the desert? (city/desert) ').lower()
        
        if setting == 'city':
            city_adventure(first=True)
        elif setting == 'desert':
            desert_adventure(first=True)
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
        
def city_adventure(first=False):
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
        if first:
            next_area(destination='desert')
    else:
        print("Invalid response. The city's dangers overwhelm you as the shadows close in...")
        quit()


def desert_adventure(first=False):
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

def next_area(destination=None):
    if destination == 'desert':
        print("After resting in the city, you know it's time to face the harsh desert. You gather your supplies and head out once more.")
        desert_adventure()
    elif destination == 'city':
        print("After enduring the desert, you find yourself drawn to the towering ruins of the city. You gather your courage and move towards the skyline.")
        city_adventure()
    else:
        print("With both the city and desert behind you, you return to your camp, your mind heavy with the experiences you've endured.")
        print("But as you rest, you realize that your journey is far from over. There's one more challenge that lies ahead.")

        # Transition to the final area
        final_area()

def final_area(name):
    print("In the quiet of your camp, a mysterious stranger approaches. His face is hidden by the shadow of his hood, and his voice is deep and haunting.")
    print("He tells you of a place called the 'Forgotten Bunker,' hidden deep beneath the earth, a relic from before the bombs fell. The bunker, he claims, holds the key to rebuilding the world.")
    print("With a sense of foreboding and hope, you decide to follow him. The journey is long and treacherous, but you finally reach the entrance to the bunker, hidden behind a waterfall deep in the mountains.")
    
    response = input("Do you trust the stranger and enter the bunker, or turn back and continue to survive on your own? (enter/turn back) ").lower()

    if response == 'enter':
        print("You follow the stranger into the dark, descending a spiral staircase that seems to go on forever. The air grows colder with each step.")
        print("When you finally reach the bottom, the bunker door creaks open, revealing a room filled with advanced technology, untouched for centuries.")
        print("The stranger steps forward, revealing his face at last—a ghoul, scarred by radiation but filled with knowledge of the old world.")
        print("He tells you that the bunker holds the remnants of a powerful AI that once controlled the world's resources. With it, you could either bring about a new era of prosperity or doom the wasteland forever.")
        
        decision = input("Do you attempt to reactivate the AI and use its power to rebuild, or destroy it to prevent anyone from misusing it? (reactivate/destroy) ").lower()
        
        if decision == 'reactivate':
            print("You connect the systems, and the AI awakens, its cold, digital voice echoing in the chamber. You issue commands, and the bunker hums to life.")
            print("Across the wasteland, old machines begin to stir. Crops begin to grow in irradiated soil, and clean water starts to flow. The wasteland is reborn.")
            print(f"As the new leader, {name}, you guide the survivors into a new age. But with great power comes great responsibility, and the future is yours to shape.")
            print("Ending: The Wasteland Reborn")
        
        elif decision == 'destroy':
            print("You look at the terminal and realize that no one should wield this much power. You set the self-destruct sequence, and the bunker begins to shake.")
            print("The stranger watches in silence as you both run for the exit. The ground trembles as the bunker collapses behind you, burying the secrets of the past forever.")
            print(f"You return to the wasteland, {name}, knowing that you've prevented a potential disaster. Life continues, but the future is uncertain.")
            print("Ending: The Past Buried")
        
        else:
            print("Invalid response. The AI remains dormant, and you are left to wonder what could have been...")
            print("The journey ends here.")
            quit()
    
    elif response == 'turn back':
        print(f"You decide that some things are better left forgotten. You turn away from the bunker and leave the stranger behind.")
        print(f"Returning to the wasteland, {name}, you continue to survive, knowing that the world will move on, with or without you.")
        print("Ending: The Lone Wanderer")
    
    else:
        print("Invalid response. The stranger disappears, and the opportunity is lost...")
        print("The journey ends here.")
        quit()

# Start the game
start_game()
