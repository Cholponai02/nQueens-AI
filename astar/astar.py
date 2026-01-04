import heapq

class AStarSolver:
    def __init__(self, n, heuristic):
        self.n = n
        self.heuristic = heuristic

    def is_goal(self, state):
        return len(state) == self.n

    def get_successors(self, state):
        successors = []
        col = len(state)
        if col >= self.n:
            return []

        for row in range(self.n):
            is_safe = True
            for prev_col, prev_row in enumerate(state):
                if prev_row == row or \
                        abs(prev_row - row) == abs(prev_col - col):
                    is_safe = False
                    break

            if is_safe:
                successors.append(state + (row,))
        return successors

    def solve(self):
        start = ()
        initial_h = self.heuristic(start, self.n)
        frontier = [(initial_h, start)]
        explored = set()

        nodes_expanded = 0

        while frontier:
            f, state = heapq.heappop(frontier)

            if state in explored:
                continue

            explored.add(state)
            nodes_expanded += 1

            if self.is_goal(state):
                return state, nodes_expanded

            for succ in self.get_successors(state):
                if succ not in explored:
                    g = len(succ)
                    h = self.heuristic(succ, self.n)
                    heapq.heappush(frontier, (g + h, succ))

        return None, nodes_expanded
