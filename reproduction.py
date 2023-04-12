import random

def matingPool(population, selectedResult):
    pool = []
    for i in range(0, len(selectedResult)):
        index = selectedResult[i]
        pool.append(population[index])
    return pool

def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        
    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child

def pmx(parent1, parent2):
    """
    Perform Partially Mapped Crossover (PMX) on two parent chromosomes.

    Args:
    parent1 (list): First parent chromosome
    parent2 (list): Second parent chromosome

    Returns:
    offspring (list): Offspring chromosome
    """

    # Choose two crossover points at random
    cxpoint1 = random.randint(0, len(parent1) - 1)
    cxpoint2 = random.randint(0, len(parent1) - 1)

    # Make sure crossover points are different
    while cxpoint2 == cxpoint1:
        cxpoint2 = random.randint(0, len(parent1) - 1)

    # Make sure crossover points are in increasing order
    if cxpoint1 > cxpoint2:
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

    # Create empty offspring chromosome
    offspring = [None] * len(parent1)

    # Copy genetic material between crossover points
    for i in range(cxpoint1, cxpoint2 + 1):
        offspring[i] = parent2[i]

    # Copy remaining genetic material from parent 1
    for i in range(len(parent1)):
        if i < cxpoint1 or i > cxpoint2:
            if parent1[i] not in offspring:
                offspring[i] = parent1[i]

    # Replace duplicated genetic material
    for i in range(cxpoint1, cxpoint2 + 1):
        if offspring[i] is None:
            idx = parent1.index(parent2[i])
            while offspring[idx] is not None:
                idx = parent1.index(parent2[idx])
            offspring[idx] = parent1[i]

    # Fill in remaining None values
    for i in range(len(parent1)):
        if offspring[i] is None:
            offspring[i] = parent1[i]

    return offspring

def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,eliteSize):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = pmx(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children

def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual

def mutatePopulation(population, mutationRate, eliteSize):
    mutatedPop = []
    
    for i in range(0,eliteSize):
        mutatedPop.append(population[i])
    for ind in range(eliteSize, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop