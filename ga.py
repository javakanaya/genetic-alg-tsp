import node, selection, random

def getCityList():
    cityList = []
    with open('cities1000', 'r') as file:
        for line in file:
            obj = line.split()
            cityList.append(node.Node(int(obj[0]), int(obj[1]), int(obj[2])))
    return cityList

def createRoute(list):
    return random.sample(list, len(list))

def initPopulation(size, list):
    population = []
    for _ in range(0, size):
        population.append(createRoute(list))
    return population


populationSize = 1000

cityList = getCityList()
population = initPopulation(populationSize, cityList)
print(population)
ranked = selection.rankPop(population)
print(ranked)

