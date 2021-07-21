import random

def rollDie(): 
    return random.choice([1,2,3,4,5,6])
def testRoll(n=10):
    result=''
    for i in range(n):
        result = result + ' ' + str(rollDie())
    print(result)
def testRoll2(n=10):
    list=[]
    for i in range(n):
        list.append(rollDie())
    print(list)    

def runSim(goal, numTrials, txt):
    total = 0
    for i in range(numTrials):
        result=''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal: 
            total += 1
    print('Actual probability of ',txt,'=',round(1/6**len(goal),8)) # to 8th digit
    estProbability = round(total/numTrials, 8)
    print('Estimated probability of', txt, '=', estProbability)

    
rollDie()
tsetRoll()
testRoll2(100)
runSim('11111', 10000, '11111')
runSim('121', 100000, '121')
    
    
