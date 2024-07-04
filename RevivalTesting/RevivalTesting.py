from functools import cache, lru_cache
from re import findall, search
from itertools import combinations
from cProfile import Profile
import pstats

@cache
def isValid(floors : tuple) -> bool:
    for floor in floors:
        if len(floor)>1:
            genList = set()
            chipList = set()
            for item in floor:
                if 'g' in item:
                    genList.add(item[:2])
                else:
                    chipList.add(item[:2])
            if bool(genList):
                for chip in chipList:
                    if chip not in genList:
                        return False
    return True

@lru_cache(maxsize = 5_000_000)
def compareTo(pattern : tuple, depth : int) -> bool:
    global pastPatterns
  #  print(len(pastPatterns))
    for length in reversed(range(depth)):
        if pattern in pastPatterns[length]:    
            return False
            
    return True



@lru_cache(maxsize = 2_000_000)
def followBranch(floors : tuple, currentFloor : int, depth : int):
    global solutionLength, pastPatterns, counter, comboList
    
    counter += 1
    if counter % 1000 == 0:
        print(counter)


    
    newdepth = depth + 1 #Depth is equivalent to the step counnt
    #if not str(depth) in pastPatterns.keys():
    #    pastPatterns[depth] = set()
    #for level in pastPatterns.keys():
    #    if not((floors,currentFloor)) in pastPatterns[level]:
    #        pastPatterns[level].add((floors, currentFloor))
    if str(depth) in pastPatterns.keys():
        pastPatterns[depth].add((floors, currentFloor))
    else:
        pastPatterns[depth] = {(floors, currentFloor)}
    if newdepth < solutionLength:    
        if 0 < currentFloor < 3: #Controls how the elevator can move
            possibleMoves = (1,-1)
        else:
            possibleMoves = (-1,) if currentFloor == 3 else (1,)
        
        combos = comboList[len(floors[currentFloor])].copy()
        #print(combos)
        for item in floors[currentFloor]:
            combos[combos.index(0)] = (item,)
        for item in combinations(tuple(floors[currentFloor]), 2):
            combos[combos.index(0)] = (item)

        for possibleMove in possibleMoves:  #Controls up/down
            for itemCombo in combos: #Controls what item
                #print(depth)
                proposedFloors = []
                for floor in floors:
                    proposedFloors.append(list(floor))
                floorToMoveTo = currentFloor + possibleMove
                #Move the elevator up or down, floorToMoveTo will represent the level of the elevator

                #Move items around
                for item in itemCombo:
                    proposedFloors[currentFloor].remove(item)
                    proposedFloors[floorToMoveTo].append(item)

                #Sort the floor so it's accurate in pastPatterns and convert to tuple
                for index, floor in enumerate(proposedFloors):
                    floor.sort()
                    proposedFloors[index] = tuple(floor)
                proposedFloors = tuple(proposedFloors)
                
                #floorRatios = [0,0,0,0]
                #for index, floor in enumerate(proposedFloors):
                #    floorRatios[index] = (len([item for item in floor if item[-1] == 'c']), len([item for item in floor if item[-1] == 'g']))
                #floorRatios = tuple(floorRatios)
                #pastPatterns uses a combination of the current state(the floor layout plus where the elevator is) and the depth to avoid infinite loops
                
                #First checks if the proposed floor fries any chips, if it doesn't check if the proposed floor is a layout that has occured at an earlier point in terms of steps
                
                if isValid(proposedFloors):
                   if compareTo((proposedFloors, floorToMoveTo), newdepth):
                        #Checks if the goal has been reached
                        for index in range(3):
                            if bool(proposedFloors[index]):
                                break
                        else:
                            solutionLength = newdepth
                            for key in [key for key in pastPatterns.keys()]:
                                if key >= solutionLength:
                                    pastPatterns.pop(key)
                            print('#',solutionLength)

                
                
                        followBranch(proposedFloors, floorToMoveTo, newdepth)
                   
    #This might be a thing to change, it's fairly useless since solution length is global anyways
    return solutionLength


if __name__ == '__main__':
    floors = ()
    cutFloor = []
    sortedFloors = ()
    floorRatios = ()
    currentFloor = 0
    counter = 0
    pastPatterns = {}
    comboList = {}
    solutionLength = 100 #Controls the maximum depth it can go at first
    numberOfItems = 0
    with open('code.txt') as file:
        floor = file.readline()
        while floor:
            floors = (*floors, (tuple(findall('\S+\sgenerator|\S+-\S+', floor))))
            floor = file.readline()
    for index, floor in enumerate(floors):
        cutFloor.append([])
        for item in floor:
            if '-' in item:
                cutFloor[index].append(item[:2]+'c')
            else:
                cutFloor[index].append(item[:2]+'g')
            numberOfItems+=1
    print(numberOfItems)
    sortedFloors = tuple(tuple(sorted(floor)) for floor in cutFloor)
    for quantity in range(numberOfItems+1):
        comboList[quantity]= [0 for _ in range(quantity+quantity*(quantity-1)//2)]
    #for floor in sortedFloors:
    #    floorRatios = (*floorRatios, (len([item for item in floor if item[-1] == 'c']), len([item for item in floor if item[-1] == 'g'])))
    #print(floorRatios)
    with Profile() as pr:
        followBranch(sortedFloors, currentFloor, 0)
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    print(solutionLength)










