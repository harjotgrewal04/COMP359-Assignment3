# **Group 6: Knapsack Problem & Visualization**

This project implements two dynamic programming approaches to solve the 0/1 Knapsack Problem: top-down (memoization) and bottom-up (tabulation). We analyze time and space complexity, performance, and provide visualizations of both implementations.

## **Members:**
- Tanisha Ahuja
- Diana Emel
- Harjot Grewal

---

## **Plan & Logging of Work**

- **Version control:** Git was used to track all contributions.

- **Task split:**

  - **Tanisha Ahuja:** Implemented bottom-up (tabulation) approach, bottom-up visualization, and backtracking functionality. See `ks_bottom_up.py` and `visualization/example_bottom_up.py`.

  - **Diana Emel:** Implemented top-down (memoization) approach and complexity analysis for top-down approach. See `ks_top_down.py`, and `complexity_analysismem.py`.

  - **Harjot Grewal:** Implemented top-down visualization and complexity analysis for bottom-up approach. See `complexity_analysistab.py`, and `visualization/example_top_down.py`.

- All members contributed coding, testing, and documentation.

---

## **Analysis Framework**

For full analysis framework explaination, see `AnalysisFramework.md`.


**Performance Results (100 trials, 30 items):**

| Approach | Average Runtime (seconds) |
|----------|--------------------------|
| Top-Down (Memoization) | ~0.000067 |
| Bottom-Up (Tabulation) | ~0.000121 |

---

## **Visualization**
Visualization is provided for both top-down and bottom-up methods. To see full details on the visualization approach, see `visualization/README.md`.

---

## **Debugging / Testing Code**

- **Methods used:** print statements, assertions, structured test cases.

- **Example test cases for top-down approach:**

  - Small capacity → correct maximum value

  - Zero capacity → `0`

  - All items fit → sum of all values

  - Best combination selection → optimal value with weight constraint

  - Heavy item doesn't fit → `0`

- **Logs:** Test outputs included in `tests/top_down.txt`.

---

## **References / Citations**

- GeeksforGeeks. (n.d.). *What is Memoization? A Complete Tutorial*. GeeksforGeeks. https://www.geeksforgeeks.org/dsa/what-is-memoization-a-complete-tutorial/#what-is-memoization

- GeeksforGeeks. (n.d.). *Tabulation vs Memoization*. GeeksforGeeks. https://www.geeksforgeeks.org/dsa/tabulation-vs-memoization/
