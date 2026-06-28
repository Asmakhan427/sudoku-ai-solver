# Sudoku CSP Solver


The **Sudoku CSP Solver** is an Artificial Intelligence project developed in **Python** that solves Sudoku puzzles using **Constraint Satisfaction Problem (CSP)** techniques. The solver combines **AC-3 (Arc Consistency)**, **Backtracking Search**, **Minimum Remaining Values (MRV)**, and **Forward Checking** to efficiently solve puzzles ranging from easy to very hard.

---

## Features

- Solves Easy, Medium, Hard, and Very Hard Sudoku puzzles
- Constraint propagation using the AC-3 algorithm
- MRV heuristic for efficient variable selection
- Backtracking search with forward checking
---

## Algorithms Implemented

### Constraint Satisfaction Problem (CSP)

The Sudoku puzzle is modeled as a Constraint Satisfaction Problem where each empty cell represents a variable with a domain of possible values. Constraints ensure that every row, column, and 3×3 subgrid contains unique numbers.

<img width="963" height="847" alt="image" src="https://github.com/user-attachments/assets/f22018e0-11d9-4550-be0a-9b4bb4ed4a70" />

---

### AC-3 Algorithm

The AC-3 algorithm establishes arc consistency by removing inconsistent values from variable domains before and during the search process, significantly reducing the search space.

<img width="958" height="840" alt="image" src="https://github.com/user-attachments/assets/c5c7b69d-5db8-486a-940c-c76874ab5293" />


---

### Minimum Remaining Values (MRV)

The MRV heuristic selects the unassigned variable with the fewest remaining legal values, improving search efficiency by reducing unnecessary branching.

<img width="959" height="837" alt="image" src="https://github.com/user-attachments/assets/30986d3e-7b9b-4726-a2ba-b26b35a2257e" />


---

### Backtracking Search

Backtracking recursively assigns values to variables while verifying all Sudoku constraints. If a conflict occurs, the algorithm backtracks and explores alternative assignments.

<img width="962" height="838" alt="image" src="https://github.com/user-attachments/assets/c6c42407-e21a-4feb-96b6-871c9f2fd547" />


---

### Forward Checking

Forward Checking updates neighboring domains after every assignment, preventing future conflicts and improving overall solver performance.

<img width="950" height="838" alt="image" src="https://github.com/user-attachments/assets/8625ee3a-2e70-4d00-8ab7-07d29d711359" />


---


## Sample Output

The solver displays the completed Sudoku grid along with the number of backtracking calls and failures.

<img width="948" height="834" alt="image" src="https://github.com/user-attachments/assets/ea83d5a3-b530-4f4a-ad05-59644b179b79" />


---

## Technologies Used

- Python
- Constraint Satisfaction Problems (CSP)
- AC-3 Algorithm
- Backtracking Search
- Minimum Remaining Values (MRV)
- Forward Checking

---

## Project Structure

```text
Sudoku-CSP-Solver/
│
├── easy.txt
├── medium.txt
├── hard.txt
├── veryhard.txt
├── sudoku_solver.py
├── screenshots/
└── README.md
```

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/Asmakhan427/Sudoku-CSP-Solver.git
```

2. Navigate to the project directory.

```bash
cd Sudoku-CSP-Solver
```

3. Run the solver.

```bash
python sudoku_solver.py
```

---

## Learning Outcomes

This project strengthened my understanding of:

- Constraint Satisfaction Problems (CSP)
- Arc Consistency (AC-3)
- Heuristic Search (MRV)
- Backtracking Algorithms
- Constraint Propagation
- Artificial Intelligence Search Techniques
