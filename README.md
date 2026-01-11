# 👑n-Queens: A* Search vs CSP

This project implements and compares two approaches for solving the **n-Queens problem**:

1.  **A* Search Algorithm**: Implemented from scratch in Python.
2.  **Constraint Satisfaction Problem (CSP)**: Implemented using the [Google OR-Tools](https://developers.google.com/optimization) CP-SAT solver.

The goal is to evaluate their performance and scalability as the board size ($n$) increases.

---

## 📝 Problem Description

The **n-Queens problem** consists of placing $n$ queens on an $n \times n$ chessboard such that no two queens attack each other.
This means that no two queens share the same row, column, or diagonal.
The problem is a classical benchmark in Artificial Intelligence for evaluating search algorithms and constraint-based approaches.

---
## 📁 Project Structure

```text
nQueens-AI/
├── astar/
│   ├── astar.py             # A* algorithm implementation
│   └── heuristics.py        # Heuristic functions
├── csp/
│   └── nqueens_csp.py       # CSP formulation using OR-Tools
├── experiments/
│   └── run_experiments.py   # Script for running performance experiments
├── visualization/
│   └── visualize_nqueens.py # Chessboard visualization (optional)
├── main.py                  # Example run with visualization
├── requirements.txt
└── README.md                # Project documentation
```
## 🛠 Features

* **Custom A* Implementation**: Uses heuristic search to find valid queen placements.
* **CSP Solver**: Leverages the industry-standard Google OR-Tools for efficient constraint solving.
* **Performance Comparison**: Analyze how each method scales from small (e.g., 4x4) to large (e.g., 50x50 or more) boards.

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.8+**
* **pip** (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Cholponai02/nQueens-AI.git
   cd n-queens-ai
   ```
2. **Create a virtual environment:**
   ```bash
   py -m venv venv
   ```
3. **Activate the environment**
   ```bash
   .\venv\Scripts\Activate.ps1
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

To run a sample comparison with visualization:
```bash
python main.py
   ```
 🏃 To RUN PERFOMANCE EXPERIMENTS (main code):
```bash
python -m experiments.run_experiments
   ```
