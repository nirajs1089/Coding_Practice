In a merge sort, you create ever smaller arrays of items and then merge them to create a final, fully sorted array. In this challenge, you will have two sorted arrays that must be merged to form a single, sorted array. Each of the arrays will be sorted in non-decreasing order.

 

As an example, consider the arrays a = [1, 2, 3] and b = [2, 5, 5]. Merge the arrays to create array c as follows:

	a[0] < b[0] → c = [a[0]] = [1]
	a[1] = b[0] → c = [a[0], b[0]] = [1, 2]
	a[1] < b[1] → c = [a[0], b[0], a[1]] = [1, 2, 2]
	a[2] < b[1] → c = [a[0], b[0], a[1], a[2]]= [1, 2, 2, 3]
	No more elements in a → c = [a[0], b[0], a[1], a[2], b[1], b[2]] = [1, 2, 2, 3, 5, 5]
Elements were alternately taken from the arrays in the order given, maintaining precedence.

 

Function Description 

Complete the function mergeArrays in the editor below. The function must return an array of all the elements from both input arrays in non-decreasing order.

 

mergeArrays has the following parameter(s):

    a[a[0],...a[n-1]]:  a sorted array of integers

    b[b[0],...b[n-1]]:  a sorted array of integers

 

Constraints

1 < n < 5 × 105
0 ≤ a[i], b[i] ≤ 109, where 0 ≤ i < n
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array a.

The next n lines each contain an element a[i] where 0 ≤ i < n.

The next line contains an integer n, the size of the array b.

The next n lines each contain an element b[i] where 0 ≤ i < n.

Sample Case 0
Sample Input 0

4
1
5
7
7
4
0
1
2
3
 

Sample Output 0

0
1
1
2
3
5
7
7
 

Explanation

The following arrays are passed to mergeArrays as arguments:

a = [ 1, 5, 7, 7]

b = [ 0, 1, 2, 3]

 

The mergedArray function returns the following merged, non-decreasing array: [ 0, 1, 1, 2, 3, 5, 7, 7 ]

Sample Case 1
Sample Input 1

5
2
4
5
9
9
5
0
1
2
3
4
 

Sample Output 1

0
1
2
2
3
4
4
5
9
9
 

Explanation

The following arrays are passed to mergeArrays as arguments:

a = [ 2, 4, 5, 9, 9]

b = [ 0, 1, 2, 3, 4]

 

The mergedArray function returns the following merged, non-decreasing array: [0, 1, 2, 2, 3, 4, 4, 5, 9, 9]
