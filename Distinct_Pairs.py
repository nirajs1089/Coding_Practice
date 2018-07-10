In this challenge, you will be given an array of integers and a target value.  Determine the number of distinct pairs of elements in the array that sum to the target value. Two pairs (a, b) and (c, d) are considered to be distinct if and only if the values in sorted order do not match, i.e., (1, 9) and (9, 1) are indistinct but (1, 9) and (9, 2) are distinct.

 

For instance, given the array [1, 2, 3, 6, 7, 8, 9, 1], and a target value of 10, the seven pairs (1,9), (2,8), (3,7), (8, 2), (9, 1), (9, 1), and (1, 9) all sum to 10 and only three distinct pairs: (1, 9), (2, 8), and (3, 7).

 

Function Description 

Complete the function numberOfPairs in the editor below. The function must return an integer, the total number of distinct pairs of elements in the array that sum to the target value. 

 

numberOfPairs has the following parameter(s):

    a[a[0],...a[n-1]]: an array of integers to select pairs from

    k: target integer value to sum to

 

Constraints

1 ≤ n ≤ 5 × 105
0 ≤ a[i] ≤ 109
0 ≤ k ≤ 5 × 109
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array a.

The next n lines each contain an element a[i] where 0 ≤ i < n.

The next line contains an integer k, the target value.

 

Sample Case 0
Sample Input 0

6
1
3
46
1
3
9
47
 

Sample Output 0

1
 

Explanation 0

a = [1, 3, 46, 1, 3, 9], k = 47

There are 4 pairs of unique elements where a[i] + a[j] = k:

(a[0] = 1, a[2] = 46)
(a[2] = 46, a[0] = 1)
(a[2] = 46, a[3] = 1)
(a[3] = 1, a[2] = 46)
In the list above, all four pairs contain the same values. We only have 1 distinct pair, (1, 46).

Sample Case 1
Sample Input 1

7
6
6
3
9
3
5
1
12
 

Sample Output 1

2
 

Explanation 1

a = [6, 6, 3, 9, 3, 5, 1], k = 12

There are 5 unique pairs where a[i] + a[j] = k:

(a[0] = 6, a[1] = 6)
(a[1] = 6, a[0] = 6)
(a[2] = 3, a[3] = 9)
(a[3] = 9, a[2] = 3)
(a[3] = 9, a[4] = 3)
(a[4] = 3, a[3] = 9)
In the list, the first two pairs are indistinct as are the last 4. Both groups are made of sets sharing the same elements. We only have 2 distinct pairs, (6, 6) and (3, 9).
