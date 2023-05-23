import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_assignment(cost_matrix):
    cost_matrix = np.array(cost_matrix)
    row_indices, col_indices = linear_sum_assignment(cost_matrix)
    print("Soultion :\nRow indices, Column indices : ",row_indices," ",col_indices)
    assignments = [(row_indices[i], col_indices[i]) for i in range(len(row_indices))]
    print("Assignments : ",assignments)
    return assignments


cost_matrix = [ [4, 6, 8],
                [2, 5, 7],
                [3, 9, 3] ]

assignments = solve_assignment(cost_matrix)
for row, col in assignments:
    print(f"Task {row + 1} : Worker {col + 1}")
