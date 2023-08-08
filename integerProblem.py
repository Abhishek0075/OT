import numpy as np
from simplex import simplex
from scipy.optimize import linprog

def SolveLPRelaxation(c, A, b):
    res = linprog(c, A_ub=A, b_ub=b)
    x = res.x
    return {'x': x, 'status': res.status, 'message': res.message}

def GomorysCuttingPlane(A, b, c):
    m, n = A.shape
    integer_solution_found = False

    while not integer_solution_found:
        res = SolveLPRelaxation(c, A, b)
        x = res['x']
        fractional_part = x - np.floor(x)

        if np.max(fractional_part) == 0:
            integer_solution_found = True
            integer_solution = x.astype(int)
        else:
            most_fractional_index = np.argmax(fractional_part)
            most_fractional_value = fractional_part[most_fractional_index]

            new_constraint = np.zeros(n)
            new_constraint[most_fractional_index] = 1
            A = np.vstack((A, new_constraint))
            b = np.hstack((b, np.floor(x[most_fractional_index])))

    return integer_solution

A = np.array([[1, 2, 3], [4, 5, 6]]) 
b = np.array([7, 8])
c = np.array([1, 1, 1])

integer_solution = GomorysCuttingPlane(A, b, c)
print("Integer Solution:", integer_solution)
