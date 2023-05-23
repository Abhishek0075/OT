costs = [
    [4, 2, 5],
    [3, 2, 6],
    [5, 8, 1]
]
supply = [20, 30, 10]
demand = [10, 20, 20]

def calculateCost(plan, costs):
    return sum([sum([plan[i][j] * costs[i][j] for j in range(len(plan[i]))]) for i in range(len(plan))])

plan = [[0 for j in range(len(costs[i]))] for i in range(len(costs))]
count = 1
for i in range(len(plan)):
    print("Plan", count, " : \n", end="")
    for row in plan:
        print(row)
    print()
    count += 1
    for j in range(len(plan[i])):
        if supply[i] <= demand[j]:
            plan[i][j] = supply[i]
            demand[j] -= supply[i]
            supply[i] = 0
        else:
            plan[i][j] = demand[j]
            supply[i] -= demand[j]
            demand[j] = 0
    

totalCost = calculateCost(plan, costs)

print("Final Transportation plan:")
for row in plan:
    print(row)
print("Total cost: ",totalCost)
