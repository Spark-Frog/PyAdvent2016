#from math import factorial
#from copy import deepcopy
#numList = ['1','2','3', '4']
##def exploreBranch(branch : list):
##    limb = []
##    for possibility in branch:
##        newBranch = deepcopy(branch)
##        newBranch.remove(possibility)
##        if bool(newBranch):
##            limb.append(exploreBranch(newBranch))
##    return branch[0]

##print(exploreBranch(numList))
#def exploreBranch(branch : list):
#    limb = []
#    for possibility in branch:
#        newBranch = deepcopy(branch)
#        newBranch.remove(possibility)
#        for route in range(factorial(len(branch))//len(branch)):
#            limb.append([possibility])

#    return limb

#print(exploreBranch(numList))




test = set()
sortedTest = set()
print(test)
test.add(('afds', 'casdgas', 'bfsv'))
for item in test:
    item = tuple(sorted(item))
    sortedTest.add(item)
print(test)
print(sortedTest)