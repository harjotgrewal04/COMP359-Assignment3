"""
Knapsack Problem Visualizer
Supports both top-down (memoization) and bottom-up (tabulation) approaches.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class KnapsackVisualizer:
    """
    Visualizer for knapsack problem solutions.
    Works with both dynamic programming approaches.
    """
    
    def __init__(self, weights, values, capacity):
        """
        Initialize the visualizer.
        
        Args:
            weights: List of item weights
            values: List of item values
            capacity: Maximum weight capacity
        """
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.n = len(weights)
    
    def visualize_dp_table(self, dp_table, save_path=None, title="Knapsack DP Table"):
        """
        Visualize a 2D DP table as a heatmap (for bottom-up approach).
        
        Args:
            dp_table: 2D list/array representing the DP table
            save_path: Optional path to save the figure
            title: Title for the plot
        """
        plt.figure(figsize=(14, 8))
        
        # Convert to numpy array
        dp_array = np.array(dp_table)
        
        im = plt.imshow(dp_array, cmap='YlOrRd', aspect='auto')
        plt.colorbar(im, label='Maximum Value')
        
        # Add text annotations
        for i in range(dp_array.shape[0]):
            for j in range(dp_array.shape[1]):
                plt.text(j, i, str(dp_array[i, j]), ha='center', va='center',
                        color='black' if dp_array[i, j] < dp_array.max() * 0.6 else 'white',
                        fontweight='bold')
        
        plt.xlabel('Capacity (w)', fontsize=12, fontweight='bold')
        plt.ylabel('Items (i)', fontsize=12, fontweight='bold')
        plt.title(title, fontsize=14, fontweight='bold', pad=20)
        plt.xticks(range(self.capacity + 1))
        plt.yticks(range(self.n + 1))
        
        # Add item information
        item_info = '\n'.join([f'Item {i}: W={self.weights[i]}, V={self.values[i]}' 
                               for i in range(self.n)])
        plt.text(1.15, 0.5, item_info, transform=plt.gca().transAxes,
                fontsize=10, verticalalignment='center',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved: {save_path}")
        else:
            plt.show()
        plt.close()
    
    def visualize_memo_table(self, memo_dict, save_path=None, title="Memoization Table"):
        """
        Visualize a memoization dictionary (for top-down approach).
        Shows only the states that were computed.
        
        Args:
            memo_dict: Dictionary with (n, capacity) as keys
            save_path: Optional path to save the figure
            title: Title for the plot
        """
        plt.figure(figsize=(14, 8))
        
        # Create a full table initialized with -1 (not computed)
        full_table = np.full((self.n + 1, self.capacity + 1), -1, dtype=int)
        
        # Fill in the memoized values
        for (n, w), value in memo_dict.items():
            if n <= self.n and w <= self.capacity:
                full_table[n, w] = value
        
        # Create custom colormap: gray for -1, YlOrRd for computed values
        masked_array = np.ma.masked_where(full_table == -1, full_table)
        
        plt.imshow(full_table, cmap='binary', aspect='auto', alpha=0.3)
        im = plt.imshow(masked_array, cmap='YlOrRd', aspect='auto')
        plt.colorbar(im, label='Maximum Value')
        
        # Add text annotations
        for i in range(full_table.shape[0]):
            for j in range(full_table.shape[1]):
                if full_table[i, j] >= 0:
                    color = 'black' if full_table[i, j] < masked_array.max() * 0.6 else 'white'
                    plt.text(j, i, str(full_table[i, j]), ha='center', va='center',
                            color=color, fontweight='bold')
                else:
                    plt.text(j, i, '·', ha='center', va='center',
                            color='lightgray', fontsize=20)
        
        plt.xlabel('Capacity (w)', fontsize=12, fontweight='bold')
        plt.ylabel('Items (n)', fontsize=12, fontweight='bold')
        plt.title(f'{title} - Computed States: {len(memo_dict)}', 
                  fontsize=14, fontweight='bold', pad=20)
        plt.xticks(range(self.capacity + 1))
        plt.yticks(range(self.n + 1))
        
        # Add item information
        item_info = '\n'.join([f'Item {i}: W={self.weights[i]}, V={self.values[i]}' 
                               for i in range(self.n)])
        item_info += f'\n\nStates computed:\n{len(memo_dict)}/{(self.n+1)*(self.capacity+1)}'
        plt.text(1.15, 0.5, item_info, transform=plt.gca().transAxes,
                fontsize=10, verticalalignment='center',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved: {save_path}")
        else:
            plt.show()
        plt.close()
    
    def visualize_solution(self, selected_items, max_value, save_path=None):
        """
        Visualize the selected items and solution.
        
        Args:
            selected_items: List of selected item indices
            max_value: Maximum value achieved
            save_path: Optional path to save the figure
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Left plot: Items comparison
        items = list(range(self.n))
        selected = [i in selected_items for i in items]
        colors = ['#2ecc71' if s else '#e74c3c' for s in selected]
        
        x = np.arange(len(items))
        width = 0.35
        
        bars1 = ax1.bar(x - width/2, self.weights, width, label='Weight', 
                       color=colors, alpha=0.7, edgecolor='black', linewidth=2)
        bars2 = ax1.bar(x + width/2, self.values, width, label='Value',
                       color=colors, alpha=0.9, edgecolor='black', linewidth=2)
        
        ax1.set_xlabel('Item Index', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Weight / Value', fontsize=12, fontweight='bold')
        ax1.set_title('Items: Selected vs Not Selected', fontsize=14, fontweight='bold')
        ax1.set_xticks(x)
        ax1.set_xticklabels([f'Item {i}' for i in items])
        ax1.legend()
        ax1.grid(axis='y', alpha=0.3)
        
        # Add value/weight ratio labels
        for i, (w, v) in enumerate(zip(self.weights, self.values)):
            ratio = v / w if w > 0 else 0
            ax1.text(i, max(w, v) + 0.5, f'Ratio: {ratio:.2f}',
                    ha='center', fontsize=9, fontweight='bold')
        
        # Right plot: Solution summary
        ax2.axis('off')
        
        total_weight = sum(self.weights[i] for i in selected_items)
        total_value = sum(self.values[i] for i in selected_items)
        
        summary_text = f"""
        ╔═══════════════════════════════════════╗
        ║      KNAPSACK SOLUTION SUMMARY       ║
        ╚═══════════════════════════════════════╝
        
        Capacity: {self.capacity}
        
        Selected Items: {len(selected_items)} out of {self.n}
        {', '.join([f'Item {i}' for i in selected_items])}
        
        ───────────────────────────────────────
        
        Total Weight Used: {total_weight} / {self.capacity}
        Remaining Capacity: {self.capacity - total_weight}
        
        Total Value: {total_value}
        
        ───────────────────────────────────────
        
        Item Details:
        """
        
        for i in selected_items:
            summary_text += f"\n  • Item {i}: Weight={self.weights[i]}, Value={self.values[i]}"
        
        summary_text += f"""
        
        ───────────────────────────────────────
        
        Efficiency: {(total_value / self.capacity):.2f} value per unit
        Utilization: {(total_weight / self.capacity * 100):.1f}% of capacity
        """
        
        ax2.text(0.1, 0.95, summary_text, transform=ax2.transAxes,
                fontsize=11, verticalalignment='top', family='monospace',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
        
        # Add legend for colors
        green_patch = mpatches.Patch(color='#2ecc71', label='Selected')
        red_patch = mpatches.Patch(color='#e74c3c', label='Not Selected')
        ax2.legend(handles=[green_patch, red_patch], loc='lower right',
                  fontsize=12, framealpha=0.9)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved: {save_path}")
        else:
            plt.show()
        plt.close()
    
    def visualize_backtrack(self, dp_table, selected_items, save_path=None):
        """
        Visualize the backtracking path through the DP table (bottom-up).
        
        Args:
            dp_table: 2D DP table
            selected_items: List of selected item indices
            save_path: Optional path to save the figure
        """
        # Reconstruct the backtracking path
        path = []
        i = self.n
        w = self.capacity
        
        while i > 0 and w > 0:
            path.append((i, w))
            if dp_table[i][w] != dp_table[i-1][w]:
                w -= self.weights[i-1]
            i -= 1
        path.append((i, w))
        
        # Create visualization
        fig, ax = plt.subplots(figsize=(14, 8))
        
        dp_array = np.array(dp_table)
        
        # Create mask for backtracking path
        mask = np.zeros_like(dp_array, dtype=bool)
        for (i, w) in path:
            mask[i, w] = True
        
        # Plot heatmap with path highlighted
        im = ax.imshow(dp_array, cmap='YlOrRd', aspect='auto', alpha=0.3)
        
        # Highlight the path
        path_array = np.copy(dp_array).astype(float)
        path_array[~mask] = np.nan
        im2 = ax.imshow(path_array, cmap='Greens', aspect='auto', alpha=1.0)
        
        plt.colorbar(im2, ax=ax, label='Maximum Value')
        
        # Add text annotations
        for i in range(dp_array.shape[0]):
            for j in range(dp_array.shape[1]):
                color = 'darkgreen' if mask[i, j] else 'gray'
                weight = 'bold' if mask[i, j] else 'normal'
                ax.text(j, i, str(dp_array[i, j]), ha='center', va='center',
                       color=color, fontweight=weight)
        
        # Draw arrows along the path
        for k in range(len(path) - 1):
            i1, w1 = path[k]
            i2, w2 = path[k + 1]
            ax.annotate('', xy=(w2, i2), xytext=(w1, i1),
                       arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
        
        ax.set_xlabel('Capacity (w)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Items (i)', fontsize=12, fontweight='bold')
        ax.set_title('Backtracking Path Through DP Table', 
                    fontsize=14, fontweight='bold', pad=20)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved: {save_path}")
        else:
            plt.show()
        plt.close()
    
    def compare_approaches(self, bottom_up_stats, top_down_stats, save_path=None):
        """
        Compare bottom-up vs top-down approaches.
        
        Args:
            bottom_up_stats: Dict with keys: 'time', 'space', 'states_computed'
            top_down_stats: Dict with keys: 'time', 'space', 'states_computed'
            save_path: Optional path to save the figure
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        
        approaches = ['Bottom-Up\n(Tabulation)', 'Top-Down\n(Memoization)']
        
        # Time comparison
        times = [bottom_up_stats['time'], top_down_stats['time']]
        bars1 = axes[0].bar(approaches, times, color=['#3498db', '#e74c3c'])
        axes[0].set_ylabel('Time (seconds)', fontweight='bold')
        axes[0].set_title('Execution Time', fontweight='bold', fontsize=14)
        axes[0].grid(axis='y', alpha=0.3)
        for i, v in enumerate(times):
            axes[0].text(i, v, f'{v:.6f}s', ha='center', va='bottom', fontweight='bold')
        
        # States computed
        states = [bottom_up_stats['states_computed'], top_down_stats['states_computed']]
        total_states = (self.n + 1) * (self.capacity + 1)
        bars2 = axes[1].bar(approaches, states, color=['#3498db', '#e74c3c'])
        axes[1].axhline(y=total_states, color='gray', linestyle='--', label='Total possible states')
        axes[1].set_ylabel('Number of States', fontweight='bold')
        axes[1].set_title('States Computed', fontweight='bold', fontsize=14)
        axes[1].legend()
        axes[1].grid(axis='y', alpha=0.3)
        for i, v in enumerate(states):
            axes[1].text(i, v, f'{v}\n({v/total_states*100:.1f}%)', 
                        ha='center', va='bottom', fontweight='bold')
        
        # Space comparison
        space = [bottom_up_stats['space'], top_down_stats['space']]
        bars3 = axes[2].bar(approaches, space, color=['#3498db', '#e74c3c'])
        axes[2].set_ylabel('Space (states)', fontweight='bold')
        axes[2].set_title('Space Complexity', fontweight='bold', fontsize=14)
        axes[2].grid(axis='y', alpha=0.3)
        for i, v in enumerate(space):
            axes[2].text(i, v, f'{v}', ha='center', va='bottom', fontweight='bold')
        
        plt.suptitle('Bottom-Up vs Top-Down Comparison', 
                    fontsize=16, fontweight='bold', y=1.02)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved: {save_path}")
        else:
            plt.show()
        plt.close()