import csv
import time

from astar.astar import AStarSolver
from astar.heuristics import nqueens_heuristic
from csp.nqueens_csp import solve_nqueens_csp


def run_experiments(n_values, output_file="results.csv"):
    with open(output_file, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "n",
            "algorithm",
            "time_seconds",
            "nodes_expanded"
        ])

        for n in n_values:
            print(f"\n=== n = {n} ===")

            # ---------- A* ----------
            print("Running A*...")
            astar = AStarSolver(n, nqueens_heuristic)

            start = time.time()
            solution, nodes_expanded = astar.solve()
            elapsed = time.time() - start

            writer.writerow([
                n,
                "A*",
                elapsed,
                nodes_expanded
            ])

            print(f"A*: time={elapsed:.4f}s, nodes={nodes_expanded}")

            # ---------- CSP ----------
            print("Running CSP...")
            solution, elapsed = solve_nqueens_csp(n)

            writer.writerow([
                n,
                "CSP",
                elapsed,
                0  # not applicable
            ])

            print(f"CSP: time={elapsed:.4f}s")


if __name__ == "__main__":
    n_values = [4, 6, 8, 10, 12, 14, 16]
    run_experiments(n_values)
