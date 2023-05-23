def calculateDistance(cityDistances,permutation):
    distance = 0
    numCities = len(permutation)
    for i in range(numCities):
        currentCity = permutation[i]
        nextCity = permutation[(i + 1) % numCities]
        distance += cityDistances[currentCity][nextCity]
    return distance

def travellingSalesmanProblem(cityDistances):
    numCities = len(cityDistances)
    allCities = list(range(numCities))
    shortestDistance = float('inf')
    shortestPath = None

    def permute(cities,start,end):
        nonlocal shortestPath,shortestDistance
        if start == end:
            distance = calculateDistance(cityDistances,cities) 
            if distance < shortestDistance:
                shortestDistance = distance
                shortestPath = cities[:]
        else:
            for i in range(start,end + 1):
                cities[start],cities[i] = cities[i],cities[start]
                permute(cities,start + 1,end)
                cities[start],cities[i] = cities[i],cities[start]

    permute(allCities,0,numCities-1)
    return shortestPath,shortestDistance

cities = [
    [0,14,24,20],
    [14,0,50,25],
    [24,50,0,30],
    [20,25,30,0]
]

print("The initial graph : ")
for row in cities :
    print(row)
shortestPath,shortestDistance = travellingSalesmanProblem(cities)
print("Shortest path:",shortestPath)
print("Shortest distance:",shortestDistance)
