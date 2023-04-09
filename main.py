import node, selection, random, reproduction

def getCityList():
    cityList = []
    with open('cities1000', 'r') as file:
        for line in file:
            obj = line.split()
            cityList.append(node.Node(int(obj[0]), int(obj[1]), int(obj[2])))
    return cityList

def createRoute(clist):
    return random.sample(clist, len(clist))

def initPopulation(size, clist):
    population = []
    for _ in range(0, size):
        population.append((createRoute(clist)))
    return population

def nextGeneration(currentGen, eliteSize, mutationRate):
    ranked = selection.rankPop(currentGen)
    print("distance: ", ranked[0][1], currentGen[ranked[0][0]])
    print("distance: ", ranked[1][1], currentGen[ranked[2][0]])
    print("distance: ", ranked[3][1], currentGen[ranked[3][0]])
    selectionResults = selection.rouletteSelection(ranked, eliteSize)
    pool = reproduction.matingPool(currentGen, selectionResults)
    children = reproduction.breedPopulation(pool, eliteSize)
    nextGeneration = reproduction.mutatePopulation(children, mutationRate)
    return nextGeneration

populationSize = 100
generations = 100
eliteSize = 5
mutationRate = 0.01

cityList = getCityList()
population = initPopulation(populationSize, cityList)

# for route in population:
#     print(route)

for i in range(0, generations):
    print(f"=== Gen :{i} ===")
    population = nextGeneration(population, eliteSize, mutationRate)

print("Final distance: " + str(selection.rankRoutes(population)[0][1]))



