
def knapsack(n, remaining_weights, wts, vals, memo_table):

    #print(f"Checking n={n}, remaining_weights={remaining_weights}")


    # return zero if n (number of items remaining) or remaining weights is zero:
    if n == 0 or remaining_weights == 0:
       # print("Base case reached. Returning 0.")
        return 0
    
    # check the table if the (n, remaining_weights) pair already exists:
    if (n, remaining_weights) in memo_table:
        #print(f"Using memoized value for n={n}, remaining_weights={remaining_weights}: {memo_table[(n, remaining_weights)]}")
        return memo_table[(n, remaining_weights)]
    
    pick = 0
    # check if the remaining weight is less than current weight. If yes then pick the item
    if wts[n - 1] <= remaining_weights:
        #print(f"Including item {n} (weight={wts[n - 1]}, value={vals[n - 1]})")
        pick = vals[n - 1] + knapsack(n - 1, (remaining_weights - wts[n - 1]), wts, vals, memo_table)

    # don't pick the item
    #print(f"Excluding item {n}")
    not_pick = knapsack(n - 1, remaining_weights, wts, vals, memo_table)

    result = max(pick, not_pick)
    # store the max in memo table and return it
    memo_table [(n, remaining_weights)] = result
    #print(f"Best for n={n}, remaining_weights={remaining_weights} is {result}")

    return result

def test():
    # Test 1: smaller capacity
    w = [1, 3, 4]
    v = [1, 4, 5]
    capacity = 3
    m = {}
    expected1 = 4
    result1 = knapsack(len(w), capacity, w, v, m)
    assert result1 == expected1, f"Test 1 Failed: got {result1}"

    # Test 2: zero capacity
    w2 = [1, 2, 3]
    v2 = [10, 15, 40]
    capacity2 = 0
    m2 = {}
    expected2 = 0
    result2 = knapsack(len(w2), capacity2, w2, v2, m2)
    assert result2 == expected2, f"Test 2 Failed: got {result2}"

    # Test 3: all items fit
    w3 = [1, 2, 3]
    v3 = [10, 20, 30]
    capacity3 = 6
    m3 = {}
    expected3 = 60
    result3 = knapsack(len(w3), capacity3, w3, v3, m3)
    assert result3 == expected3, f"Test 3 Failed: got {result3}"

    # Test 4: choose best combination (not all fit)
    w4 = [4, 2, 3]
    v4 = [10, 4, 7]
    capacity4 = 5
    m4 = {}
    expected4 = 11   # items with weight 2 and 3
    result4 = knapsack(len(w4), capacity4, w4, v4, m4)
    assert result4 == expected4, f"Test 4 Failed: got {result4}"

    # Test 5: heavy item doesn’t fit
    w5 = [10]
    v5 = [100]
    capacity5 = 5
    m5 = {}
    expected5 = 0
    result5 = knapsack(len(w5), capacity5, w5, v5, m5)
    assert result5 == expected5, f"Test 5 Failed: got {result5}"

    print("✅ All test cases passed!")

        
    
#if __name__ == "__main__":
    #test()