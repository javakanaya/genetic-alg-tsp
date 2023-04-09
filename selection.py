import operator, random
import pandas as pd
import numpy as np
import fitness as fn

def rankPop(population):
    populationsFitness = {}
    for i in range(0, len(population)):
        # get fitness value, and its index
        populationsFitness[i] = fn.Fitness(population[i]).routeFitness()
    # return sorted list of fitnes value
    # print(sorted(populationsFitness.items(), key = operator.itemgetter(1), reverse = True))
    return sorted(populationsFitness.items(), key = operator.itemgetter(1))

def rouletteSelection(populationRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(populationRanked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()

    for i in range(0, eliteSize):
        selectionResults.append(populationRanked[i][0])
    for i in range(0, len(populationRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(populationRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(populationRanked[i][0])
                break
    return selectionResults