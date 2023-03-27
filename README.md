# UMT-Software-Problem
In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.) Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.

Sample input:
[1,2,3,4,5,6,7,8]
Sample output:
True

Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average
of 4.5.
Note:
The length of A will be in the range [1, 30].
A[i] will be in the range of [0, 10000].

Personal Tests:
testCases = [[2, 2, 33],[2, 4, 4], [], [1], [75, 2], [11, 23, 37, 45, 54, 86, 90], [1, 2, 3, 4, 5, 6,7,8],[2, 4, 6, 8, 10, 12, 14, 16],[11, 23, 37, 45, 54, 86, 94], [10, 20, 30, 40, 50, 60, 70, 120], [2, 2, 2]]

False,False,False,False,False,False,True,True,True,True,True

Implementation:

For this problem, I realized that in the case of numbers ordered by increasing multiples of n, the average of the first and last number is equal to the average of the other numbers.
Based on this fact, we created an algorithm that sorts the list of numbers and initially checks this fact, then checks all possibilities for subsequences that contain the first and last number plus the other numbers starting from the second to the penultimate.
The algorithm uses the total sum of the numbers to calculate the average of list B and the average of list C without actually putting numbers in the lists.
