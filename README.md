# **Group 6: Knapsack Problem & Visualization**

This project implements two dynamic programming approaches to solve the 0/1 Knapsack Problem: top-down (memoization) and bottom-up (tabulation). We analyze time and space complexity, performance, and provide visualizations of both implementations.

## **Members:**
- Tanisha Ahuja
- Diana Emel
- Harjot Grewal

---

## **Planning & Logging of Work**

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

## **Link to our GitHub repo**:
https://github.com/harjotgrewal04/COMP359-Assignment3

## **References / Citations**

- GeeksforGeeks. (2012, March 19). 0/1 Knapsack Problem. Retrieved from GeeksforGeeks website: https://www.geeksforgeeks.org/dsa/0-1-knapsack-problem-dp-10/
- GeeksforGeeks. (2022, June 24). What is Memoization? A Complete Tutorial. Retrieved December 2, 2025, from GeeksforGeeks website: https://www.geeksforgeeks.org/dsa/what-is-memoization-a-complete-tutorial/#what-is-memoization
- GeeksforGeeks. (2017, April 13). Tabulation vs Memoization. Retrieved from GeeksforGeeks website: https://www.geeksforgeeks.org/dsa/tabulation-vs-memoization/-
- Gautam, S. (2023, September 4). Top-down vs Bottom-up Approach in Dynamic Programming. Retrieved from EnjoyAlgorithms website: https://medium.com/enjoy-algorithm/top-down-vs-bottom-up-approach-in-dynamic-programming-53b917bfbe0
- Mastering the 0/1 Knapsack Problem: A Comprehensive Guide – AlgoCademy Blog. (2025). Retrieved December 2, 2025, from Algocademy.com website: https://algocademy.com/blog/mastering-the-0-1-knapsack-problem-a-comprehensive-guide/#space-optimization
