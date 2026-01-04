from astar.astar import AStarSolver
from astar.heuristics import conflicts_heuristic
from csp.nqueens_csp import solve_nqueens_csp
import time

N = 8

print("=== A* ===")
astar = AStarSolver(N, conflicts_heuristic)
start = time.time()
solution, expanded = astar.solve()
elapsed = time.time() - start
print("Solution:", solution)
print("Nodes expanded:", expanded)
print("Time:", elapsed)

print("\n=== CSP ===")
solution, elapsed = solve_nqueens_csp(N)
print("Solution:", solution)
print("Time:", elapsed)
