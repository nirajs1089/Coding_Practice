Dwight has an ordered array of sales numbers. Michael wants to know the index of the smallest index element for which the sums of all elements to the left and to the right are equal. The array may not be reordered.

 

For example, given the array sales=[1,2,3,4,6], we see that 1+2+3=6. Using zero based indexing, sales[3]=4 is the value sought. The index is 3.

 

Function Description 

Complete the function balancedSum in the editor below. The function must return the index of the smallest element for which the sum of elements to its left and its right are equal.

 

balancedSum has the following parameter(s):

    sales[sales[0],...sales[n-1]]:  an array of integers

 

Constraints

3 ≤ n ≤ 105
1 ≤ sales[i] ≤ 2 × 104, where 0 ≤ i < n
It is guaranteed that a solution always exists.
Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array sales.

Each of the next n lines contains an integer sales[i] where 0 ≤ i < n.

 

Sample Case 0
Sample Input 0

4
1
2
3
3
 

Sample Output 0

2
 

Explanation 0

sales[0] + sales[1] = 1 + 2 = 3 is equal to sales[3] = 3, so we return 2 as our index.

 

Sample Case 1
Sample Input 1

3
1
2
1
 

Sample Output 1

1
 

Explanation 1

sales[0] = 1 is equal to sales[2] = 1, so we return 1 as our index.
