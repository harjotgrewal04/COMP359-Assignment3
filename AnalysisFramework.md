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
## **6. Test Cases**
## **5. Design Choices**
## **6. Future improvements**
## **7. Conclusion**


