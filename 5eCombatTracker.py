#Python 5e DM Combat Tracker

#This dictionary will store name, initiative, and a list of status effects and their lengths
creatures = {}

print("Enter 'Name : InitiativeCount' to add creature to combat\nEnter 'START' to start combat")

#This section takes the creatures' names and initiative counts
while True:

    #Assigns input to a list split by either a ':' or a space, either works
    #I will store the name and initiative count in the keys of the creature dictionary, with a list of effects in the values
    'Remember to add something that checks that the tuple elements are in the right order'
    nameInitiative = input()
    if ':' in nameInitiative:
        nameInitiative = nameInitiative.split(':')
    else:
        nameInitiative = nameInitiative.split()

    #Starts combat if the user wills it
    if nameInitiative[0].upper() == 'START':
        break
    
    #This will accomodate for initiative counts and names input in the wrong order
    #It also checks to make sure the user input an initiative count
    try:
        try:
            nameInitiative[1] = int(nameInitiative[1])
        except ValueError:
            nameInitiative[0], nameInitiative[1] = [nameInitiative[1], nameInitiative[0]]
            nameInitiative[1] = int(nameInitiative[1])
           
        #Puts the name and initiative into a dictionary (with an empty list to store status effects later on)
        #Stores nameInitiative as a tuple so it can server as a key
        creatures.update({tuple(nameInitiative):[]})
        print(f'{nameInitiative[0]} added')
        
    #If the user doesn't input an initiative count, it informs them
    except ValueError:
        print(f'Neither {nameInitiative[1]} or {nameInitiative[0]} is an initiative count, try again')
    except IndexError:
        print('Invalid Input, please enter valid input')

#Creates the tracker list from the creatures key list. Which will keep track of turn order.
#This block sorts the key tuples in the dictionary by their 2nd element, the initiative count
tracker = list(creatures.keys())
tracker.sort(reverse = True, key = lambda x : x[1])

#This block checks for ties and lets the user handle them
for i in range(len(tracker)):
    #I implemented error handling because the index eventually goes out of bounds
    #But by that time it's gone through all the creatures so it breaks the loop when it reaches that point
    try:
        if tracker[i][1] == tracker[i+1][1]:
            print(f'Does {tracker[i][0]}(1) or {tracker[i+1][0]}(2) have a higher initiative bonus? (Input respective #)')
            uInput = input()
            
            if uInput == '2':
                tracker[i], tracker[i+1] = [tracker[i+1], tracker[i]]      
    except IndexError:
        break

#This will count the number of rounds passed
Round = 1

#This will be the main combat loop
while True:

    #Displays current round 
    print(f'\n*****************\nSTART OF ROUND {Round}\n*****************')

    #Iterates through the turns in combat
    for i in tracker:
        #This bit decrements the values of effects at the start of the respective creature's turn
        for x in creatures[tuple(i)]:
            x[1] -= 1

        #Gives user summary of active effects and who's turn it is
        #It also checks to see which effects have run it course
        print()
        print(f"{i[0].capitalize()}'s Turn! ({i[1]})")
        print('Active Effects: ')
        for x in creatures[i]:
            if x[1] == 0:
                print(f'* The {x[0]} effect has ended!')
                creatures[i].remove(x)
            else:    
                print(f'* {x[0]}({x[1]})')  
        
        #Allows user to bark commands at the program (To continue to next turn or place an effect on current character)
        while True:            
            command = input('- ')
            if command == 'next' or command == 'n':
                break
            elif command == '':
                print('No input detected')
            else:
                command = command.split()
                creatures[i].append([command[0], int(command[1])])

    Round += 1


























