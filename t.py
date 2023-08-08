import pulp as pl

def solve_integer_programming(c, A, b):
    problem = pl.LpProblem("Integer Programming Problem", pl.LpMinimize)
    
    n = len(c)
    x = [pl.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(n)]
    
    problem += sum(c[i] * x[i] for i in range(n))
    
    for i in range(len(A)):
        problem += sum(A[i][j] * x[j] for j in range(n)) >= b[i]
    
    problem.solve()
    
    if problem.status == pl.LpStatusOptimal:
        return [x[i].value() for i in range(n)]
    
    while True:
        fractional_vars = [i for i in range(n) if not x[i].value().is_integer()]
        chosen_var = fractional_vars[0]
        value = x[chosen_var].value()
        problem += sum(int(value) * A[i][chosen_var] * x[i] for i in range(n)) >= int(value) * b[i]
        problem.solve()
        
        if problem.status == pl.LpStatusOptimal:
            return [x[i].value() for i in range(n)]

c = [3, 2, 1]
A = [[1, 1, 1], [10, 2, 6], [7, 2, 1]]
b = [5, 30, 14]

solution = solve_integer_programming(c, A, b)
print("Solution:", solution)
