import random

print('Welcome to guessing game!')

v = random.randint(1, 100)
playing = True
guesses = []

while(playing):
        
        player_choice = int(input('Enter a number: '))
        
        if player_choice < 1 or player_choice > 100:
            print('OUT OF BOUNDS!')
            continue
            
        # Winning Scenario    
        if player_choice == v:
            print('CORRECT GUESS!')
            guesses.append(player_choice)
            playing = False
            
        else:
            # First Time Playing
            if len(guesses) == 0:
                if abs(player_choice - v) in range(1,11):
                    print('WARM!')
                else:
                    print('COLD!')
                guesses.append(player_choice)
            else:
                if abs(guesses[-1]-v) < abs(player_choice-v) :
                    print('COLDER!')
                else:
                    print('WARMER!')
                guesses.append(player_choice)
                
print('Number of Guesses: %d' %(len(guesses)))
