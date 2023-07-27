from functools import cache
from time import perf_counter
from re import findall
from copy import deepcopy
from itertools import combinations


@cache
def isValid(floors : tuple) -> bool:
    for floor in floors:
        for item in floor:
            if 'compatible' in item:
                if not item.split('-')[0] in set(gen.split(' ')[0] for gen in floor if 'generator' in gen) and bool(set(gen for gen in floor if 'generator' in gen)):
                    return False
    return True

@cache
def followBranch(floors : tuple, currentFloor : int, depth : int):
    global pastPatterns, solutionLength
    #pastPatterns uses a combination of the current state(the floor layout plus where the elevator is) and the depth to avoid infinite loops
    pastPatterns.add((tuple(floor for floor in floors), currentFloor, depth)) 
    newdepth = depth + 1 #Depth is equivalent to the step counnt
    if newdepth < solutionLength:    
        if 0 < currentFloor < 3: #Controls how the elevator can move
            possibleMoves = (1,-1)
        else:
            possibleMoves = (-1,) if currentFloor == 3 else (1,)
        items = tuple((item,) for item in floors[currentFloor]) #Individual devices
        combos = tuple(combo for combo in combinations(tuple(item for item in floors[currentFloor]), 2)) #Unique combinations of 2
   
        combos = (*combos, *items) #Combine the two into a tuple containing all possible combinations of move
        for possibleMove in possibleMoves:  #Controls up/down
            for itemCombo in combos: #Controls what item
                
                proposedFloors = deepcopy(list(floors))

                #Replaces  the current floor with a floor excluding any devices being moved
                proposedFloors[currentFloor] = tuple(device for device in proposedFloors[currentFloor] if device not in itemCombo)
                #Move the elevator up or down, floorToMoveTo will represent the level of the elevator
                floorToMoveTo = currentFloor + possibleMove

                proposedFloors[floorToMoveTo] = (*(proposedFloors[floorToMoveTo]), *itemCombo)

                for floor in proposedFloors:
                    proposedFloors[proposedFloors.index(floor)] = tuple(sorted(floor)) #Sort the floor so it's accurate in pastPatterns
                
                #Turn back to a tuple so it's hashable
                proposedFloors = tuple(proposedFloors)
                
                #Checks if the goal has been reached
                if sum([bool(floor) for index,floor in enumerate(proposedFloors) if index != 3]) == 0:
                     if depth < solutionLength:
                         solutionLength = newdepth
                         print('###################') #Hastags are used so that if I'm printing other data I can easily find it by searching for hastags
                         print(solutionLength)
                
                         #First checks if the proposed floor fries any chips, if it doesn't check if the proposed floor is a layout that has occured at an earlier point in terms of steps
                if isValid(proposedFloors) and not (tuple(floor for floor in proposedFloors), floorToMoveTo) in [(pattern[0], pattern[1]) for pattern in pastPatterns if pattern[2] < depth]:
                    followBranch(proposedFloors, floorToMoveTo, newdepth)
    #This might be a thing to change, it's farily useless since solution length is global anyways
    return solutionLength
            
            

if __name__ == '__main__':
    floors = ()
    sortedFloors = ()
    currentFloor = 0
    pastPatterns = set()
    solutionLength = 250 #Controls the maximum depth it can go at first

    with open('code.txt') as file:
        floor = file.readline()
        while floor:
            floors = (*floors,(tuple(findall('\S+\sgenerator|\S+-\S+',floor))))
            floor = file.readline()
    for floor in floors:
        sortedFloors = (*sortedFloors, (tuple(sorted(floor))))
 

    t1 = perf_counter()
    print(followBranch(sortedFloors, currentFloor, 0))
    print(perf_counter() - t1)
    



