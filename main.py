from astar.astar import AStarSolver
from astar.heuristics import nqueens_heuristic
from csp.nqueens_csp import solve_nqueens_csp
import time
from utils.visualize_nqueens import NQueensVisualizer

N = 8

print("=== A* ===")
astar = AStarSolver(N, nqueens_heuristic)
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

visualizer = NQueensVisualizer(N)

def show_step(state):
    visualizer.draw_state(state)

solver = AStarSolver(N, nqueens_heuristic)
solution, _ = solver.solve(callback=show_step)

print("Solution:", solution)