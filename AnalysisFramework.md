# **Analysis Framework**

## **1. Algorithm Design Choices**

### **1.1 Language Selection**
- For both the bottom up & top down approach python was used
- Easier to visualize
- Dynamic typing
- Readable
- 
### **1.2 Knapsack Problem Approaches**
- Top-Down Approach: Memoization
- Bottom-Up Approach: Tabulation
- Memoization stores the results of functions calls so they do not have to be repeated and only the subproblems needed
- Tabulation finds and stores all of the results in a table until the problem is solved
- 
## **2. Implementation Comparison**

### **2.1 Top-Down Approach**
- Recursive solving approach
- Increased overhead
- Only fills entries when requires
- 
### **2.2 Bottom-Up Approach**
- Iterative solving approach
- Entries are filled from smallest size until the final size
- Adds redundancy
- 
## **3. Performance Analysis**

### **3.1 Top-Down Memoization** 
- Time Complexity: O(n * W)
- Space Complexity: 0(n * W)
- Empirical Results: Average runtime over 100 trials: 0.000067 seconds
- Averaged over 5 times: 0.0000614 seconds
  
### **3.2 Bottom-Up Tabulation**
- Time Complexity: O(n * W)
- Space Complexity: 0(n * W)
- Empirical Results: Average runtime over 100 trials: 0.000121 seconds
- Averaged over 5 times: 0.000108 seconds
  
### **3.3 Analysis**
- Bottom-Up is slower due to computing all subproblems
- Top-Down is quicker due to only computing needed entries
- Despite the time difference share same time complexity due to worst case of all entries needing to be filled
- Top-Down only stores visited states while Bottom-Up stores a full 2D table
  
## **4. Test Cases**

### **4.1 Test Strategies**

#### **4.1.1 Top-Down & Bottom-Up Test Cases**
- Small capacity & zero capacity
- All items fit in knapsack
- Must select best combination/highest value
- Singular heavy item
  
### **4.1.2 Empirical Test Cases**
- 100 trials, 30 items, 200 max weight, 400 max value 100 max capacity**
- Uses randomly generated integers
  
## **4.2 Test Coverage**
- Both approaches tested
- Visualization for both implementations with same test case
- Execution time using randomly generated numbers for both implementations

## **5. Future improvements**
- Using a real-time DP table visualization
- Implementing the previous row to calculate current which will decrease space complexity in Bottom-Up

## **6. Conclusion**
To conclude uisng python and its available libraries we were able to effectively visualize  and implement a top-down and bottom-up approach for the knapsack problem. Using dynamic programming allows for breaking the larger problem into smaller subproblems which we applied in the memoization and tabulation. Where memoization uses a recursive approach and stores subproblem results to help avoid redundant calculations. While also only calculating the states which are needed. Tabulation uses a iterative approach and computes all reults and stores them in a table and avoids the recursive overhead. Overall, using dymanic programming to solve the knapsack problem allows for efficient and better time and space complexity especially when compared against brute force methods. 
