# **Analysis Framework**
## **1. Algorithm Design Choices**
### **1.1 Language Selection**
- For both the bottom up & top down approach python was used
- Easier to visualize
- Dynamic typing
- Readable
### **1.2 Knapsack Problem Approaches**
- Top-Down Approach: Memoization
- Bottom-Up Approach: Tabulation
- Memoization stores the results of functions calls so they do not have to be repeated and only the subproblems needed
- Tabulation finds and stores all of the results in a table until the problem is solved
## **2. Implementation Comparison**
### **2.1 Top-Down Approach**
- Recursive solving approach
- Increased overhead
- Only fills entries when requires
### **2.2 Bottom-Up Approach**
- Iterative solving approach
- Entries are filled from smallest size until the final size
- Adds redundancy
## **3. Performance Analysis**
### **3.1 Top-Down Memoization**
- Time Complexity: O(n * W)
- Space Complexity: 0(n * W)
### **3.2 Bottom-Up Tabulation**
- Time Complexity: O(n * W)
- Space Complexity: 0(n * W)


