from ortools.sat.python import cp_model
import time

def solve_nqueens_csp(n):
    model = cp_model.CpModel()

    queens = [model.NewIntVar(0, n - 1, f"Q{i}") for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            model.Add(queens[i] != queens[j])
            model.AddAbsEquality(
                model.NewIntVar(0, n, ""),
                queens[i] - queens[j]
            )
            model.Add(queens[i] - queens[j] != i - j)
            model.Add(queens[i] - queens[j] != j - i)

    solver = cp_model.CpSolver()
    start = time.time()
    status = solver.Solve(model)
    elapsed = time.time() - start

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        solution = [solver.Value(q) for q in queens]
        return solution, elapsed

    return None, elapsed
