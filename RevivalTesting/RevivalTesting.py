from functools import wraps
from time import perf_counter
from types import FunctionType, GeneratorType

def timer(func : FunctionType):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        result = func(*args, **kwargs)
        t2 = perf_counter() - t1
        print(f'{func.__name__} ran in {t2}')
        return result
    return wrapper
#from hashlib import md5

#doorID = 'reyedfim'
#password = ['-','-','-','-','-','-','-','-']
#increasingInteger = 0
#while '-' in password:
#    guess = md5((f'{doorID}{increasingInteger}').encode()).hexdigest()
#    if guess.startswith('00000'):
#        if guess[5].isdigit():
#            if int(guess[5]) < 8:
#                if password[int(guess[5])] == '-':
#                    password[int(guess[5])] = guess[6]
#    increasingInteger += 1
#print(''.join(password))
#Day 6
#decodedWord = ''
#with open('code.txt', 'r') as file:
#    word = tuple(file.readline().removesuffix('\n'))
#    letterCounter = {
#            '0' : {},
#            '1' : {},
#            '2' : {},
#            '3' : {},
#            '4' : {},
#            '5' : {},
#            '6' : {},
#            '7' : {}
#            }
#    while word:
#        for index,letter in enumerate(word):
#            if letter in letterCounter[str(index)]: 
#                letterCounter[str(index)][letter] += 1
#            else:
#                letterCounter[str(index)][letter] = 1
#        word = tuple(file.readline().removesuffix('\n'))
#    for index, dictionary in enumerate(letterCounter.values()):
#        decodedWord += min(dictionary, key = dictionary.get)
#    print(decodedWord)
#Day 7
#import re
##Part 1
#listOfTLSIPs = []
#with open('code.txt', 'r') as file:
#    IP = file.readline().removesuffix('\n')
#    while IP:
#        centerTLS = True
#        outerTLS = False
#        parts = re.split('[[]|[]]', IP)
#        for index, part in enumerate(parts):
#            for pos in range(len(part)-3):
#                if part[pos] == part[pos+3] and part[pos+1] == part[pos+2] and part[pos] != part[pos+1]:
#                    if index % 2 == 0:
#                        outerTLS = True
#                    elif index % 2 == 1:
#                        centerTLS = False
#        if outerTLS and centerTLS:
#            listOfTLSIPs.append(IP)
#        IP = file.readline().removesuffix('\n')
#print(len(listOfTLSIPs))
##Part 2
#listOfTLSIPs = []
#with open('code.txt', 'r') as file:
#    IP = file.readline().removesuffix('\n')
#    while IP:
#        checks = []
#        match = False
#        parts = re.split('[[]|[]]', IP)
#        for part in [part for index, part in enumerate(parts) if index % 2 == 0]:
#            for pos in range(len(part)-2):
#                if part[pos] == part[pos+2] and part[pos] != part[pos+1]:
#                    checks.append(part[pos+1]+part[pos]+part[pos+1])

#        for part in [part for index, part in enumerate(parts) if index % 2 == 1]:
#            for pos in range(len(part)-2):
#                if part[pos] == part[pos+2] and part[pos] != part[pos+1]:
#                    if part[pos]+part[pos+1]+part[pos] in checks:
#                       match = True
#        if match:
#            listOfTLSIPs.append(IP)
#        IP = file.readline().removesuffix('\n')
#print(len(listOfTLSIPs))
#from collections import deque
#import re
#count = 0 
#display = list(deque('0'*50) for x in range(6))
#with open('code.txt', 'r') as instructions:
#    line = instructions.readline().removesuffix('\n')
#    instruction = re.split(' by | x=|x| y=|\s',line)
#    while line:
#        match instruction[0]:
#            case 'rect':
#                for row in range(int(instruction[2])):
#                    for col in range(int(instruction[1])):
#                        display[row][col] = '1'
#            case 'rotate':
#                match instruction[1]:
#                    case 'row':
#                        display[int(instruction[2])].rotate(int(instruction[3]))
#                    case 'column': 
#                        col = deque()
#                        for row in display:
#                            col.append(row[int(instruction[2])])
#                        col.rotate(int(instruction[3]))
#                        for index,row in enumerate(display):
#                            row[int(instruction[2])] = col[index]
#        line = instructions.readline().removesuffix('\n')
#        instruction = re.split(' by | x=|x| y=|\s',line)
                        

                        
#    for row in display:
#        for index,col in enumerate(row):
#            count += int(col)
#            if col == '0': #For part 2
#                row[index] = ' '
#        print(''.join(row)) #Part 2 answer
#    print(count) #Part 1 answer
 
#with open('code.txt', 'r') as file:
#    marker = [0,0]
#    compressed = file.read(1)
#    decompressedString = ''
#    while compressed:
#        if marker[0] == 0:
#            if compressed != '(':
#                decompressedString += compressed
#                compressed = file.read(1)
#            else:
#                marker = ''
#                while compressed != ')':
#                    compressed = file.read(1)
#                    marker += compressed if compressed != ')' else ''
#                marker = [int(i) for i in marker.split('x')]
#        else:
#            duplicateString = ''
#            while marker[0] != 0:
#                 compressed = file.read(1)
#                 duplicateString += compressed
#                 marker[0] -= 1
#            decompressedString += duplicateString * marker[1]
#            compressed = file.read(1)
#    print(len(decompressedString))
#from io import TextIOWrapper

#def decompressSub(file : TextIOWrapper) -> int:
#    marker = ''
#    length = 0
#    compressed = file.read(1)
#    while compressed != ')':
#        marker += compressed if compressed != ')' else ''
#        compressed = file.read(1)
#    marker = [int(i) for i in marker.split('x')]
#    currentPos = file.tell()
#    while file.tell() < currentPos + marker[0]:
#        compressed = file.read(1)
#        if compressed == '(': #Simply remove these two lines to revert to part 1
#            length += decompressSub(file)
#    length = marker[0]*marker[1] if length == 0 else length * marker[1]

#    return length


#with open('code.txt','r') as file:
#    compressed = file.read(1)
#    length = 0
#    while compressed:
#            if compressed != '(':
#                compressed = file.read(1)
#                length += 1
#            else:
#                length += decompressSub(file)
#                compressed = file.read(1)
#    print(length)

#import re

#class Bot():
#    def __init__(self, info : GeneratorType):
#        self.name = next(info)
#        self.low = (next(info), next(info))
#        self.high = (next(info), next(info))
#        self.values = []

#    def sort(self):
#        self.values.sort()

#bots = {}
#outputs = {}
#valueList = []
#target = [17,61]
#with open('code.txt', 'r') as commands:
#    line = commands.readline()
#    while line:
#        if line.startswith('bot'):
#            info = re.findall('\d+|output|bot', line)
#            bots[info[1]] = Bot(info[i] for i in range(1,6))

#        else:
#             valueList.append(re.findall('\d+', line))

#        line = commands.readline()

#    for value in valueList:
#        bots[value[1]].values.append(int(value[0]))
 
#    for bot in bots.values(): bot.sort()
 
#    while [bot.values for bot in bots.values() if bot.values]:
#        for bot in bots.values(): 
#            if len(bot.values) == 2:
#                bot.sort()
#                if 'bot' in bot.low:
#                    bots[bot.low[1]].values.append(bot.values[0]) 
#                else:
#                    outputs[bot.low[1]] = bot.values[0]
#                if 'bot' in bot.high:
#                    bots[bot.high[1]].values.append(bot.values[1])
#                else:
#                    outputs[bot.high[1]] = bot.values[1]
#                bot.values = []
        
                

#        for bot in bots.values(): bot.sort()
#        for bot in bots.values():
#            if bot.values == target: #Part 1
#                print(bot.name)


#    print(outputs['0']*outputs['1']*outputs['2']) #Part 2


from re import findall
from copy import deepcopy
from itertools import combinations
from sys import setrecursionlimit
import cProfile
import pstats
setrecursionlimit(100000)

def cache(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args)+str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@cache
def isValid(floors : list) -> bool:
    for floor in floors:
        for item in floor:
            if 'compatible' in item:
                if not item.split('-')[0] in set(gen.split(' ')[0] for gen in floor if 'generator' in gen) and bool(set(gen for gen in floor if 'generator' in gen)):
                    return False
    return True

@cache
def followBranch(floors : list, currentFloor : int, depth : int):
    global pastPatterns, solutionLength, counter
    pastPatterns.append(([floor for floor in floors], currentFloor, depth))
    newdepth = depth + 1
    if newdepth < solutionLength:    
        if 0 < currentFloor < 3:
            possibleMoves = [1,-1]
        else:
            possibleMoves = [-1] if currentFloor == 3 else [1]
        items = floors[currentFloor]
        combos = [combo for combo in combinations(items, 2)]
        for item in items:
            combos.append([item])
        for possibleMove in possibleMoves:  
            for itemCombo in combos:
                proposedFloors = deepcopy(floors)
                floorToMoveTo = currentFloor
                heldDevices = itemCombo
                for item in heldDevices:
                    proposedFloors[floorToMoveTo].pop(proposedFloors[floorToMoveTo].index(item))
                floorToMoveTo += possibleMove
                for item in heldDevices:
                    proposedFloors[floorToMoveTo].append(item)
                for floor in proposedFloors:
                    floor.sort()
            
                if sum([bool(floor) for index,floor in enumerate(proposedFloors) if index != 3]) == 0:
                     if depth < solutionLength:
                         solutionLength = newdepth
                     
                         #print('###################')
                         print(solutionLength)
                         #print('###################')
            
                if isValid(proposedFloors) and not (list(floor for floor in proposedFloors), floorToMoveTo) in [(pattern[0], pattern[1]) for pattern in pastPatterns if pattern[2] < depth] :
                    followBranch(proposedFloors, floorToMoveTo, newdepth)

    return solutionLength
            
            




if __name__ == '__main__':
    floors = []
    currentFloor = 0
    heldDevices = []
    pastPatterns = []
    solutionLength = 250
    counter = 0

    with open('code.txt') as file:
        floor = file.readline()
        while floor:
            floors.append(findall('\S+\sgenerator|\S+-\S+',floor))
            floor = file.readline()
    
    for floor in floors:
            floor.sort()
    #with cProfile.Profile() as pr:
     #   followBranch(floors, currentFloor, 0)
    #stats = pstats.Stats(pr)
    #stats.sort_stats(pstats.SortKey.TIME)
    #stats.print_stats()



    t1 = perf_counter()
    print(followBranch(floors, currentFloor, 0))
    print(perf_counter() - t1)




