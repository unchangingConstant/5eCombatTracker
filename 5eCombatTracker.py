#Python 5e DM Combat Tracker

from time import sleep
#Initiative taker:

#nameInitiave dictionary declaration:
creatures = {}

print("Enter 'Name : Initiativecount'\nEnter 'START' to start combat:")

#This section takes the creature name and initiative order
while True:

    #Assigns input to a tuple and checks if user wants to stop
    #I assigned it to a tuple so it could serve as a dicionary key
    #I will store the name and initiative count in the key, and a list of status effects and their lengths in the values
    'Remember to add something that checks that the tuple elements are in the right order'
    nameInitiative = input().split()
    if nameInitiative[0].upper() == 'START':
        break
    nameInitiative[1] = int(nameInitiative[1])
    creatures.update({tuple(nameInitiative):[]})
    print(f'{nameInitiative[0]} added')

#creates the tracker list. Which will keep track of turn order.
#This block sorts the key tuples in the dictionary by their 2nd element, the initiative count
tracker = list(creatures.keys())
tracker.sort(reverse = True, key = lambda x : x[1])

#This block lets the user handle initiative ties
for i in range(len(tracker)):
    try:
        if tracker[i][1] == tracker[i+1][1]:
            print(f'Does {tracker[i][0]}(1) or {tracker[i+1][0]}(2) have a higher initiative bonus? (Input respective #)')
            uInput = input()

            if uInput == '2':
                tracker[i], tracker[i+1] = [tracker[i+1], tracker[i]]
    except IndexError:
        break

Round = 1

#This will be the main combat loop
while True:

    #Displays current round 
    print(f'START OF ROUND {Round}\n')

    #Iterates through the turns in combat
    for i in tracker:
        print(f'{i[0]}: {i[1]}')
        input()

    Round += 1
