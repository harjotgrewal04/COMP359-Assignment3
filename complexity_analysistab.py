import time
import random
from ks_bottom_up import knapsack_bottom_up

def average_knapsack_time(num_trials, n_items, max_weight, max_value, max_capacity):
    total_time = 0

    for i in range(num_trials):

        weights = [random.randint(1, max_weight) for j in range(n_items)]
        values = [random.randint(1, max_value) for k in range(n_items)]

        capacity = random.randint(1, max_capacity)
        memo = {}

        start_time = time.time()
        knapsack_bottom_up(n_items, capacity, weights, values)
        end_time = time.time()

        total_time += (end_time - start_time)

    average_time = total_time / num_trials
    return average_time

if __name__ == "__main__":

    avg_time = average_knapsack_time(100, 30, 200, 400, 100)
    print(f"Average runtime over 100 trials: {avg_time:.6f} seconds")