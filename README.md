#  Sudoku CSP Solver
##  Project Overview
This project implements a **Sudoku Solver** using **Constraint Satisfaction Problem (CSP)** techniques from Artificial Intelligence.
The solver efficiently solves Sudoku puzzles of varying difficulty levels using:
* **AC-3 Algorithm (Arc Consistency)**
* **Backtracking Search**
* **MRV Heuristic (Minimum Remaining Values)**
* **Forward Checking**
##  Problem Formulation (CSP)
* **Variables:**
  81 cells of a 9×9 Sudoku board, each represented as `(row, column)`
* **Domains:**
  Values from **1 to 9** for empty cells
  Single value for pre-filled cells
* **Constraints:**
  * All values in each **row** must be different
  * All values in each **column** must be different
  * All values in each **3×3 box** must be different
##  Algorithms Used
### 1. AC-3 (Arc Consistency Algorithm)
* Applied before search and after each assignment
* Removes invalid values from domains
* Reduces search space significantly
### 2. MRV (Minimum Remaining Values)
* Selects the variable with the **fewest legal values**
* Helps detect failure early (fail-first strategy)
### 3. Backtracking Search
* Recursively assigns values to variables
* Reverts (backtracks) when constraints are violated
### 4. Forward Checking
* Uses AC-3 after each assignment
* Prevents future conflicts by updating domains
  
##  Project Structure
sudoku-csp-solver/
│
├── easy.txt
├── medium.txt
├── hard.txt
├── veryhard.txt
├── sudoku_solver.py
└── README.md
## ▶️ How to Run
1. Clone the repository:
git clone https://github.com/your-username/sudoku-csp-solver.git
2. Navigate to the folder:
cd sudoku-csp-solver
3. Run the program:
python sudoku_solver.py

##  Sample Output
The program solves puzzles and prints:
* Completed Sudoku board
* Number of backtracking calls
* Number of failures
  
## Features
* Solves **Easy, Medium, Hard, and Very Hard** puzzles
* Efficient constraint propagation using **AC-3**
* Smart variable selection using **MRV**
* Performance tracking (calls & failures)

##  Concepts Covered

* Constraint Satisfaction Problems (CSP)
* Arc Consistency (AC-3)
* Heuristics (MRV)
* Backtracking Algorithms
* Artificial Intelligence Search Techniques


---

## 📌 Note

This project is developed for academic purposes as part of an Artificial Intelligence assignment.
