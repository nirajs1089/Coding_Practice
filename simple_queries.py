Given two arrays of positive integers, for each element in the second array, find the total number of elements in the first array which are less than or equal to that element.  Store the values determined in an array.

 

For example, if the first array is [1, 2, 3] and the second array is [2, 4], then there are 2 elements in the first array less than or equal to 2. There are 3 elements in the first array which are less than or equal to 4. We can store these answers in an array, answer = [2, 3].

 

Function Description 

Complete the function counts in the editor below. The function must return an array of m positive integers, one for each maxes[i] representing the total number of elements nums[j] satisfying nums[j] ≤ maxes[i]where 0 ≤ j < n and 0 ≤ i < m, in the given order.

 

counts has the following parameter(s):

    nums[nums[0],...nums[n-1]]:  first array of positive integers

    maxes[maxes[0],...maxes[n-1]]:  second array of positive integers

 

Constraints

2 ≤ n, m ≤ 105
1 ≤ nums[j] ≤ 109, where 0 ≤ j < n.
1 ≤ maxes[i] ≤ 109, where 0 ≤ i < m.
 

Input Format For Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the number of elements in nums.

The next n lines each contain an integer describing nums[j] where 0 ≤ j < n.

The next line contains an integer m, the number of elements in maxes.

The next m lines each contain an integer describing maxes[i] where 0 ≤ i < m.

 

Sample Case 0
Sample Input 0

4
1
4
2
4
2
3
5
Sample Output 0

2
4
Explanation 0

We are given n = 4, nums = [1, 4, 2, 4], m = 2, and maxes = [3, 5].

For maxes[0] = 3, we have 2 elements in nums (nums[0] = 1 and nums[2] = 2) that are ≤ maxes[0].
For maxes[1] = 5, we have 4 elements in nums (nums[0] = 1, nums[1] = 4, nums[2] = 2, and nums[3] = 4) that are ≤ maxes[1].
Thus, the function returns the array [2, 4] as the answer.

Sample Case 1
Sample Input 1

5
2
10
5
4
8
4
3
1
7
8
Sample Output 1

1
0
3
4
Explanation 1

We are given, n = 5, nums = [2, 10, 5, 4, 8], m = 4, and maxes = [3, 1, 7, 8].

For maxes[0] = 3, we have 1 element in nums (nums[0] = 2) that is ≤ maxes[0].
For maxes[1] = 1, there are 0 elements in nums that are ≤ maxes[1].
For maxes[2] = 7, we have 3 elements in nums (nums[0] = 2, nums[2] = 5, and nums[3] = 4) that are ≤ maxes[2].
For maxes[3] = 8, we have 4 elements in nums (nums[0] = 2, nums[2] = 5, nums[3] = 4, and nums[4] = 8) that are ≤ maxes[3].
Thus, the function returns the array [1, 0, 3, 4] as the answer
