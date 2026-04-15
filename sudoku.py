from collections import defaultdict, deque
def read_board(filename):
    board = []
    with open(filename, 'r') as f:
        for line in f:
            board.append([int(ch) for ch in line.strip()])
    return board

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)   

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")   

            print(board[i][j], end=" ")

        print()
    print()

# CSP

def get_domains(board):
    domains = {}
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                domains[(r, c)] = set(range(1, 10))
            else:
                domains[(r, c)] = {board[r][c]}
    return domains

def get_neighbors():
    neighbors = defaultdict(set)
    for r in range(9):
        for c in range(9):
            cell = (r, c)

            for i in range(9):
                if i != c:
                    neighbors[cell].add((r, i))
                if i != r:
                    neighbors[cell].add((i, c))

            br, bc = 3 * (r // 3), 3 * (c // 3)
            for i in range(br, br + 3):
                for j in range(bc, bc + 3):
                    if (i, j) != cell:
                        neighbors[cell].add((i, j))
    return neighbors

# AC-3

def ac3(domains, neighbors):
    queue = deque([(xi, xj) for xi in domains for xj in neighbors[xi]])

    while queue:
        xi, xj = queue.popleft()
        if revise(domains, xi, xj):
            if not domains[xi]:
                return False
            for xk in neighbors[xi] - {xj}:
                queue.append((xk, xi))
    return True

def revise(domains, xi, xj):
    revised = False
    for val in set(domains[xi]):
        if all(val == v for v in domains[xj]):
            domains[xi].remove(val)
            revised = True
    return revised

# Forward Checking

def forward_check(var, value, domains, neighbors):
    removed = []

    for n in neighbors[var]:
        if value in domains[n]:
            domains[n].remove(value)
            removed.append((n, value))

            if not domains[n]:
                restore(domains, removed)
                return None
    return removed

def restore(domains, removed):
    for var, val in removed:
        domains[var].add(val)

# Backtracking

backtrack_calls = 0
backtrack_failures = 0

def backtrack(assignment, domains, neighbors):
    global backtrack_calls, backtrack_failures
    backtrack_calls += 1

    if len(assignment) == 81:
        return assignment

    # MRV
    var = min([v for v in domains if v not in assignment],
              key=lambda v: len(domains[v]))

    for value in domains[var]:
        if is_consistent(var, value, assignment, neighbors):

            assignment[var] = value
            removed = forward_check(var, value, domains, neighbors)

            if removed is not None:
                result = backtrack(assignment, domains, neighbors)
                if result:
                    return result

            # undo
            assignment.pop(var)
            if removed:
                restore(domains, removed)

    backtrack_failures += 1
    return None

def is_consistent(var, value, assignment, neighbors):
    for n in neighbors[var]:
        if n in assignment and assignment[n] == value:
            return False
    return True

# Solver

def solve_sudoku(filename):
    global backtrack_calls, backtrack_failures
    backtrack_calls, backtrack_failures = 0, 0

    board = read_board(filename)
    print("Solving:", filename)

    domains = get_domains(board)
    neighbors = get_neighbors()

    ac3(domains, neighbors)

    assignment = {v: next(iter(domains[v])) for v in domains if len(domains[v]) == 1}

    result = backtrack(assignment, domains, neighbors)

    if result:
        solved = [[result[(r, c)] for c in range(9)] for r in range(9)]
        print_board(solved)
    else:
        print("No solution")

    print("Calls:", backtrack_calls)
    print("Failures:", backtrack_failures)
    print("-" * 40)

if __name__ == "__main__":
    for f in ["easy.txt", "medium.txt", "hard.txt", "veryhard.txt"]:
        solve_sudoku(f)
