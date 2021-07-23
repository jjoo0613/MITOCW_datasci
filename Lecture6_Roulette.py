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
    
    
