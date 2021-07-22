from matplotlib import pylab
import random

import Lecture5_RandomWalk.py 

## How do i graph it? 
#xVals = [1, 2, 3, 4]
#yVals1 = [1, 2, 3, 4]
#pylab.plot(xVals, yVals1, 'b-', label = 'first')
#yVals2 = [1, 7, 3, 5]
#pylab.plot(xVals, yVals2, 'r--', label = 'second')
#pylab.legend()

class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result
    
def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of',
              numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances
