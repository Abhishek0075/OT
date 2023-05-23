import math
import numpy as np



def createTable(toBeMaximized,coefficents,solution):
    xb = [eq + [x] for eq,x in zip(coefficents,solution)]
    z = toBeMaximized + [0]
    return xb + [z]


def improvedDual(table):
    rhsEntries = [row[-1] for row in table[:-1]]
    return any([entry < 0 for entry in rhsEntries])


def getPivot(table):
    rhsEntries = [row[-1] for row in table[:-1]]
    minRhs = min(rhsEntries)
    row = rhsEntries.index(minRhs)
    tableCol = []
    for index, element in enumerate(table[row][:-1]):
        if element < 0:
            tableCol.append(index)
    colValues = [table[row][c] / table[-1][c] for c in tableCol]
    colMinIndex = colValues.index(min(colValues))
    finalCol = tableCol[colMinIndex]
    
    return row, finalCol


def pivotStep(table, pivotPosition):
    newTable = [[] for eq in table]
    i, j = pivotPosition
    pivotValue = table[i][j]
    newTable[i] = np.array(table[i]) / pivotValue
    for eq_i, eq in enumerate(table):
        if eq_i != i:
            multiplier = np.array(newTable[i]) * table[eq_i][j]
            newTable[eq_i] = np.array(table[eq_i]) - multiplier
    return newTable


def isBasic(col):
    return sum(col) == 1 and len([c for c in col if c == 0]) == len(col) - 1


def getSolution(table):
    tableCol = np.array(table).T
    solutions = []
    for col in tableCol:
        solution = 0
        if isBasic(col):
            oneIndex = col.tolist().index(1)
            solution = tableCol[-1][oneIndex]
        solutions.append(solution)
        
    return solutions


def dualSimplex(c, A, b):
    table = createTable(c, A, b)
    print("Initial table : ",table,"\n")
    while improvedDual(table):
        pivotPos = getPivot(table)
        table = pivotStep(table, pivotPos)
    return getSolution(table)


toBeMaximized = [12, 3, 4, 0, 0]

coefficents = [[-4, -2, -3, 1, 0],
    [-8, -1, -2, 0, 1]]

solutions = [-2, -3]

dual = dualSimplex(toBeMaximized, coefficents, solutions)
print('After dual simplex : ', dual)