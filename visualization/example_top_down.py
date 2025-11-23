"""
Example: Using the visualizer with top-down approach
"""
import sys
import os
# Get the directory of *this* file (visualization/)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Project root is the parent of visualization/
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

# Add project root to sys.path (so we can import ks_top_down, visualizer, etc.)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from ks_top_down import knapsack
from visualizer import KnapsackVisualizer

def backtrack_solution_top_down(n, capacity, weights, values, memo):
    """
    Backtrack to find which items were selected (for top-down approach).
    """
    selected_items = []
    i = n
    w = capacity
    
    while i > 0 and w > 0:
        # Check if this state included item i-1
        not_pick = memo.get((i-1, w), 0)
        pick = 0
        if weights[i-1] <= w:
            pick = values[i-1] + memo.get((i-1, w - weights[i-1]), 0)
        
        if pick > not_pick and (i, w) in memo:
            selected_items.append(i-1)
            w -= weights[i-1]
        i -= 1
    
    selected_items.reverse()
    return selected_items


def demo_top_down():
    """Demonstrate top-down approach with visualization."""

    # Example problem
    weights = [2, 3, 4, 5, 6]
    values = [3, 4, 8, 8, 10]
    capacity = 20
    n = len(weights)
    
    print("\n" + "="*60)
    print("  TOP-DOWN APPROACH WITH VISUALIZATION")
    print("="*60)
    print(f"\nWeights: {weights}")
    print(f"Values:  {values}")
    print(f"Capacity: {capacity}")
    
    # Solve using top-down approach
    memo = {}
    max_value = knapsack(n, capacity, weights, values, memo)
    
    
    # Backtrack to find selected items
    selected_items = backtrack_solution_top_down(n, capacity, weights, values, memo)
    
    print(f"\nMaximum Value: {max_value}")
    print(f"Selected Items: {selected_items}")
    print(f"States computed: {len(memo)} out of {(n+1)*(capacity+1)}")
    
    # Create visualizer
    viz = KnapsackVisualizer(weights, values, capacity)
    
    # Generate visualizations
    print("\nGenerating visualizations...")
    viz.visualize_memo_table(memo, 
                            save_path='output/top_down_memo.png',
                            title='Top-Down Memoization Table')
    
    viz.visualize_solution(selected_items, max_value,
                          save_path='output/top_down_solution.png')
    
    print("\n✓ All visualizations saved in output/ folder!")
    print(f"Note: Top-down computed only {len(memo)}/{(n+1)*(capacity+1)} states!")


if __name__ == "__main__":
    import os
    os.makedirs('output', exist_ok=True)
    demo_top_down()