# 🧩 Sudoku Solver using CSP (Python)

This project implements a **Sudoku Solver** using **Constraint Satisfaction Problem (CSP)** techniques in Python.

It solves Sudoku puzzles of varying difficulty levels (`easy`, `medium`, `hard`, `veryhard`) using:

* **AC-3 Algorithm (Arc Consistency)**
* **Backtracking Search**
* **MRV Heuristic (Minimum Remaining Values)**
* **Forward Checking**

---

## 📌 Features

* Solves 9×9 Sudoku boards
* Uses **AI-based constraint solving techniques**
* Efficient solving with:

  * AC-3 preprocessing
  * MRV variable selection
  * Forward checking for pruning
* Tracks:

  * Number of backtracking calls
  * Number of failures

---

## 📂 Project Structure

```
.
├── sudoku.py
├── easy.txt
├── medium.txt
├── hard.txt
├── veryhard.txt
└── README.md
```

---

## 🧠 Concepts Used

### 1. CSP (Constraint Satisfaction Problem)

Each Sudoku cell is treated as a variable with a domain (1–9). Constraints ensure:

* No duplicate in row
* No duplicate in column
* No duplicate in 3×3 grid

---

### 2. AC-3 Algorithm

Reduces domains before search by enforcing **arc consistency**, removing invalid values early.

---

### 3. Backtracking Search

Recursively assigns values to cells and backtracks if a conflict occurs.

---

### 4. MRV Heuristic

Selects the variable with the **smallest domain first**, improving efficiency.

---

### 5. Forward Checking

After assigning a value, it removes that value from neighboring domains to prevent conflicts.

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed.

### Step 2: Run the program

```bash
python sudoku.py
```

---

## 📄 Input Format

Each Sudoku board is stored in a `.txt` file:

* 9 lines
* Each line contains 9 digits
* Use `0` for empty cells


## 👩‍💻 Author

**Faryal Jafferi**

---
