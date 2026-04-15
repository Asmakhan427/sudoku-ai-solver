import os
import json
puzzles = {
    "easy.txt": [
        "004030050", "609400000", "005100489",
        "000060930", "300807002", "026040000",
        "453009600", "000004705", "090050200",
    ],
    "medium.txt": [
        "530070000", "600195000", "098000060",
        "800060003", "400803001", "700020006",
        "060000280", "000419005", "000080079",
    ],
    "hard.txt": [
        "400000805", "030000000", "000700000",
        "020000060", "000080400", "000010000",
        "000603070", "500200000", "104000000",
    ],
    "veryhard.txt": [
        "100007090", "030020008", "009600500",
        "005300900", "010080002", "600004000",
        "300000010", "040000007", "007000300",
    ],
}

for filename, lines in puzzles.items():
    with open(filename, "w") as f:
        f.write("\n".join(lines))

class SudokuSolver:
    def __init__(self, filename: str):
        self.board = []
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line:
                    self.board.append([int(ch) for ch in line])

        self.backtrack_calls = 0
        self.backtrack_failures = 0
        self.neighbors = {
            (r, c): self._compute_neighbors(r, c)
            for r in range(9) for c in range(9)
        }
        self.domains = self._initialize_domains()

    def _compute_neighbors(self, r: int, c: int) -> set:
        peers = set()
        for i in range(9):
            peers.add((r, i))
            peers.add((i, c))
        box_r, box_c = (r // 3) * 3, (c // 3) * 3
        for dr in range(3):
            for dc in range(3):
                peers.add((box_r + dr, box_c + dc))
        peers.discard((r, c))
        return peers

    def _initialize_domains(self) -> dict:
        domains = {}
        for r in range(9):
            for c in range(9):
                if self.board[r][c] != 0:
                    domains[(r, c)] = [self.board[r][c]]
                else:
                    domains[(r, c)] = [
                        v for v in range(1, 10)
                        if self._is_consistent((r, c), v)
                    ]
        return domains

    def ac3(self, queue: list | None = None) -> bool:
        if queue is None:
            queue = [
                (xi, xj)
                for xi in self.domains
                for xj in self.neighbors[xi]
            ]

        while queue:
            xi, xj = queue.pop(0)
            if self._revise(xi, xj):
                if not self.domains[xi]:
                    return False
                for xk in self.neighbors[xi]:
                    if xk != xj:
                        queue.append((xk, xi))
        return True

    def _revise(self, xi: tuple, xj: tuple) -> bool:
        revised = False
        for x in self.domains[xi][:]:
            if not any(y != x for y in self.domains[xj]):
                self.domains[xi].remove(x)
                revised = True
        return revised

    def _is_consistent(self, var: tuple, val: int) -> bool:
        r, c = var
        for nr, nc in self.neighbors[var]:
            if self.board[nr][nc] == val:
                return False
        return True

    def solve(self) -> bool:
        self.ac3()
        return self._backtrack()

    def _backtrack(self) -> bool:
        self.backtrack_calls += 1
        unassigned = [
            (r, c)
            for r in range(9) for c in range(9)
            if self.board[r][c] == 0
        ]
        if not unassigned:
            return True

        var = min(unassigned, key=lambda v: len(self.domains[v]))
        r, c = var

        for val in list(self.domains[var]):
            if self._is_consistent(var, val):
                self.board[r][c] = val
                saved_domains = {k: list(v) for k, v in self.domains.items()}
                self.domains[var] = [val]

                arcs = [(xk, var) for xk in self.neighbors[var]]
                if self.ac3(arcs):
                    if self._backtrack():
                        return True

                self.board[r][c] = 0
                self.domains = saved_domains

        self.backtrack_failures += 1
        return False

    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                print(self.board[i][j], end=" ")
            print()

for filename in ["easy.txt", "medium.txt", "hard.txt", "veryhard.txt"]:
    print(f"\nSolving: {filename}")
    solver = SudokuSolver(filename)
    if solver.solve():
        solver.print_board()
        print(f"\nBacktrack Calls: {solver.backtrack_calls}")
        print(f"Backtrack Failures: {solver.backtrack_failures}")
    else:
        print("No solution found.")











