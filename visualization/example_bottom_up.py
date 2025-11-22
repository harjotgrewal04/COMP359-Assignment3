"""
Example: Using the visualizer with bottom-up approach
"""

import sys
sys.path.append('..')

from ks_bottom_up import solve_knapsack
from visualizer import KnapsackVisualizer


def demo_bottom_up():
    """Demonstrate bottom-up approach with visualization."""
    
    # Example problem
    weights = [2, 3, 4, 5, 6]
    values = [3, 4, 8, 8, 10]
    capacity = 10
    
    print("\n" + "="*60)
    print("  BOTTOM-UP APPROACH WITH VISUALIZATION")
    print("="*60)
    print(f"\nWeights: {weights}")
    print(f"Values:  {values}")
    print(f"Capacity: {capacity}")
    
    # Solve using bottom-up approach
    max_value, selected_items, dp_table = solve_knapsack(weights, values, capacity)
    
    print(f"\nMaximum Value: {max_value}")
    print(f"Selected Items: {selected_items}")
    
    # Create visualizer
    viz = KnapsackVisualizer(weights, values, capacity)
    
    # Generate visualizations
    print("\nGenerating visualizations...")
    viz.visualize_dp_table(dp_table, 
                          save_path='output/bottom_up_table.png',
                          title='Bottom-Up DP Table (Tabulation)')
    
    viz.visualize_solution(selected_items, max_value,
                          save_path='output/bottom_up_solution.png')
    
    viz.visualize_backtrack(dp_table, selected_items,
                           save_path='output/bottom_up_backtrack.png')
    
    print("\n✓ All visualizations saved in output/ folder!")


if __name__ == "__main__":
    import os
    os.makedirs('output', exist_ok=True)
    demo_bottom_up()