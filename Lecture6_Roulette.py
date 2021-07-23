import random 

class FairRoulette():
    def __init__(self):
        self.pockets= []
        for i in range(1, 37): #1-36
            self.pockets.append(i)
        self.ball = None
        self.pocketOdds = len(self.pockets) - 1 #35 
  
    def spin(self):
        self.ball = random.choice(self.pockets) #random from 1-36
        
    def betPocket(self, pocket, amt): 
        if str(pocket) == str(self.ball): 
            return amt*self.pocketOdds #bet and win --> win $ amount = rest of holes (35) *betamount
        else: 
            return - amt
    def __str__(self): 
        return 'fair roulette'

def playRoulette(game, numSpins, pocket, bet, toPrint):
    totalPocket = 0
    for i in range(numSpins):
        game.spin() #FairRoulette.spin , EuRoulette.spin
        totalPocket += game.betPocket(pocket, bet) #b=pocketnumber, amount
    if toPrint:
        print(numSpins, 'spins of', game)
        print('Expected return betting in hole #', pocket, '=',str(100*totalPocket/numSpins) + '%\n')
    return (totalPocket/numSpins)


random.seed(0)
game = FairRoulette()
for numSpins in (100, 1000000):
    for i in range(3):
        playRoulette(game, numSpins, 2,1, True) 

####    append gametype - Eu, Am are subclass of FairRoulette- they function the same as FairRoulette! 
class EuRoulette(FairRoulette): #Eu Roulette is a subclass of FairRoulette
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0') #European pocket
    def __str__(self):
        return "European Roulette"

class AmRoulette(EuRoulette): #American Roulette is subclass of EU roulette < FairRoulette
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00') #another pocket --> thus less likely
    def __str__(self):
        return 'American Roullete'

####Simulations.. . 
    
def findPocketReturn(game, numTrials, trialSize, toPrint):
    pocketReturns = []
    for t in range(numTrials):
        trialVals = playRoulette(game, trialSize, 2, 1, toPrint)
        pocketReturns.append(trialVals)
    return pocketReturns

random.seed(0)
numTrials = 20
resultDict = {}
games = (FairRoulette, EuRoulette, AmRoulette)
for gametype in games:
    resultDict[gametype().__str__()] = [] #since was in tuple - we hav eto extract w/ .__str__() .... 
                                   # we need to G() with this bracket for the input of class(self) 
for numSpins in (1000, 10000, 100000, 1000000):
    print('\nSimulate', numTrials, 'trials of', numSpins, 'spins each')
    for gametype in games:
        pocketReturns = findPocketReturn(gametype(), numTrials,numSpins, False)
        expReturn = 100*sum(pocketReturns)/len(pocketReturns)
        print('Exp. return for', gametype(), '=', str(round(expReturn, 3)) + '%')

        
def getMeanAndStd(data):
    mean = sum(data)/float(len(data))
    tot = 0.0
    for i in data:
        tot += (i - mean)**2
    var = tot/len(data)
    std = var**0.5
    
    return mean, std

 
numTrials = 20
resultDict = {}
games = (FairRoulette, EuRoulette, AmRoulette)
for G in games:
    resultDict[G().__str__()] = []
for numSpins in (1000, 10000, 100000, 1000000):
    print('\nSimulate', numTrials, 'trials of', numSpins, 'spins each')
    for G in games:
        pocketReturns = findPocketReturn(G(), numTrials,numSpins, False)
        mean, std = getMeanAndStd(pocketReturns)
        resultDict[G().__str__()].append((numSpins, 100*mean, 100*std))
        
        print('Exp. return for', G(), '=', str(round(100*mean, 3)) + '%,' \
              + '+/-'+str(round(100*1.96*std, 3)) + '%' \
              + 'with 95% confidence')    #"why 1.96? two tail z-score 95%I = 1.96sigma"
