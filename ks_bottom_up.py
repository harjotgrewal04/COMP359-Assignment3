
def knapsack_bottom_up(n, capacity, weights, values):
    """
    Bottom-up dynamic programming solution for 0/1 Knapsack Problem.
    
    Time Complexity: O(n * W) where n is number of items and W is capacity
    Space Complexity: O(n * W) for the DP table
    
    Args:
        n: Number of items
        capacity: Maximum weight capacity of knapsack
        weights: List of item weights
        values: List of item values
    
    Returns:
        Maximum value that can be achieved
    """
    # Create DP table: dp[i][w] = max value using first i items with capacity w
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Option 1: Don't include item i-1
            dp_table[i][w] = dp_table[i-1][w]
            
            # Option 2: Include item i-1 (if it fits)
            if weights[i-1] <= w:
                value_with_item = dp_table[i-1][w - weights[i-1]] + values[i-1]
                dp_table[i][w] = max(dp_table[i][w], value_with_item)
    
    return dp_table[n][capacity]


def backtrack_solution(n, capacity, weights, values, dp_table):
    """
    Backtrack through the DP table to find which items were selected.
    
    Args:
        n: Number of items
        capacity: Maximum weight capacity
        weights: List of item weights
        values: List of item values
        dp_table: Completed DP table
    
    Returns:
        List of selected item indices (0-based)
    """
    selected_items = []
    i = n
    w = capacity
    
    while i > 0 and w > 0:
        # If value came from including item i-1
        if dp_table[i][w] != dp_table[i-1][w]:
            selected_items.append(i-1)  # Item index (0-based)
            w -= weights[i-1]
        i -= 1
    
    selected_items.reverse()
    return selected_items


def solve_knapsack(weights, values, capacity):
    """
    Complete solution with both max value and selected items.
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity
    
    Returns:
        tuple: (max_value, selected_items, dp_table)
    """
    n = len(weights)
    
    # Create DP table
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp_table[i][w] = dp_table[i-1][w]
            
            if weights[i-1] <= w:
                value_with_item = dp_table[i-1][w - weights[i-1]] + values[i-1]
                dp_table[i][w] = max(dp_table[i][w], value_with_item)
    
    # Backtrack to find selected items
    selected_items = backtrack_solution(n, capacity, weights, values, dp_table)
    max_value = dp_table[n][capacity]
    
    return max_value, selected_items, dp_table


def test():
    # Test 1: smaller capacity
    w = [1, 3, 4]
    v = [1, 4, 5]
    capacity = 3
    expected1 = 4
    result1 = knapsack_bottom_up(len(w), capacity, w, v)
    assert result1 == expected1, f"Test 1 Failed: got {result1}"

    # Test 2: zero capacity
    w2 = [1, 2, 3]
    v2 = [10, 15, 40]
    capacity2 = 0
    expected2 = 0
    result2 = knapsack_bottom_up(len(w2), capacity2, w2, v2)
    assert result2 == expected2, f"Test 2 Failed: got {result2}"

    # Test 3: all items fit
    w3 = [1, 2, 3]
    v3 = [10, 20, 30]
    capacity3 = 6
    expected3 = 60
    result3 = knapsack_bottom_up(len(w3), capacity3, w3, v3)
    assert result3 == expected3, f"Test 3 Failed: got {result3}"

    # Test 4: choose best combination (not all fit)
    w4 = [4, 2, 3]
    v4 = [10, 4, 7]
    capacity4 = 5
    expected4 = 11    # items with weight 2 and 3
    result4 = knapsack_bottom_up(len(w4), capacity4, w4, v4)
    assert result4 == expected4, f"Test 4 Failed: got {result4}"

    # Test 5: heavy item doesn't fit
    w5 = [10]
    v5 = [100]
    capacity5 = 5
    expected5 = 0
    result5 = knapsack_bottom_up(len(w5), capacity5, w5, v5)
    assert result5 == expected5, f"Test 5 Failed: got {result5}"

    print("✅ All test cases passed!")

    
#if __name__ == "__main__":
    #test()
