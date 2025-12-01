# Knapsack Problem Visualization Module

This module provides visualization tools for the 0/1 Knapsack problem using dynamic programming.

## Team Members
- Tanisha Ahuja (Bottom-up approach + Visualization)
- Diana Emel (Top-down approach implementation + complexity analysis)
- Harjot Grewal (Top-down visualization + Bottom-up complexity analysis)

## Current Implementation

**Bottom-Up (Tabulation) Approach** - Implemented by Tanisha Ahuja
- Complete 2D DP table visualization
- Solution visualization with selected items
- Backtracking path visualization

**Top-down (Memorization) Approach** - Implemented by Diana Emal and Harjot Grewal
- Complete 2D memorization table visualization
- Solution visualization with selected items

## Files

- `visualizer.py` - Main visualization class with all plotting methods
- `example_bottom_up.py` - Demo for bottom-up approach visualization
- `example_top_down.py` - Demo for top-down approach visualization
- `README.md` - This file

## Features

### 1. DP Table Visualization
- Shows the complete 2D DP table with all states computed
- Heatmap showing maximum values at each state
- Item information panel

### 2. Solution Visualization
- Bar chart showing selected vs non-selected items
- Summary panel with solution details
- Value/weight ratios for each item
- Capacity utilization statistics

### 3. Backtracking Visualization
- Shows the path taken through the DP table to find selected items
- Arrows indicating the backtracking direction
- Highlighted path cells

## Usage

### For Bottom-Up Approach:

```python
from ks_bottom_up import solve_knapsack
from visualizer import KnapsackVisualizer

# Solve the problem
max_value, selected_items, dp_table = solve_knapsack(weights, values, capacity)

# Create visualizer
viz = KnapsackVisualizer(weights, values, capacity)

# Generate visualizations
viz.visualize_dp_table(dp_table, save_path='dp_table.png')
viz.visualize_solution(selected_items, max_value, save_path='solution.png')
viz.visualize_backtrack(dp_table, selected_items, save_path='backtrack.png')
```
### For Top-Down Approach:
```python
from ks_top_down import knapsack
from visualizer import KnapsackVisualizer

# Solve the problem
max_value = knapsack(n, capacity, weights, values, memo)
selected_items = backtrack_solution_top_down(n, capacity, weights, values, memo)

# Create visualizer
viz = KnapsackVisualizer(weights, values, capacity)

# Generate visualizations
viz.visualize_memo_table(memo, save_path='output/top_down_memo.png',title='Top-Down Memoization Table')
viz.visualize_solution(selected_items, max_value, save_path='output/top_down_solution.png')
```



## Example Output

Run the example to see the visualizations for bottom-up:

```bash
cd visualization
python example_bottom_up.py
```

This will save visualizations to the `output/` folder:
- `bottom_up_table.png` - Full DP table heatmap
- `bottom_up_solution.png` - Solution summary with selected items
- `bottom_up_backtrack.png` - Backtracking path through the table

Run the example to see the visualizations for top-down:
```bash
cd visualization
python example_top_down.py
```
This will save visualizations to the `output/` folder:
- `top_down_memo.png` - Full DP memorization table heatmap
- `top_down_solution.png` - Solution summary with selected items

## Dependencies

- `numpy` >= 1.21.0
- `matplotlib` >= 3.4.0

