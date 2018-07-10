An array of integers arr, of size n is defined as [a[0], a[1], ..., a[n-1]. You will be given an array of integers to sort. Sorting must first be by frequency of occurrence, then by value. For instance, given an array [4, 5, 6, 5, 4, 3], there is one each of 6's and 3's, and there are two 4's, two 5's. The sorted list is [3, 6, 4, 4, 5, 5].

 

Function Description 

Complete the function customSort in the editor below. The function must return an array sorted ascending first by frequency of occurrence, then by value within frequency.

 

customSort has the following parameter(s):

    arr[arr0,...arrn-1]:  an array of integers to sort

 

Constraints

1 ≤ n ≤ 2 × 105
1 ≤ arr[i] ≤ 106
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the integer array arr.

The next n lines each contain an element arr[i].

Sample Case 0
Sample Input 0

5
3
1
2
2
4
 

Sample Output 0

1
3
4
2
2
 

Explanation

n = 5, arr = [3, 1, 2, 2, 4]

First, we separate our numbers by frequency.

The subset of numbers having frequency 1 is [3, 1, 4].

The subset of numbers having frequency 2 is [2, 2].

Our partially sorted data (with respect to and in ascending order of frequency) can be expressed as [[3, 1, 4], [2, 2]].

Then we sort each subset of elements having the same frequency in non-decreasing order, resulting in [[1, 3, 4], [2, 2]].

Sample Case 1
Sample Input 1

10
8
5
5
5
5
1
1
1
4
4
 

Sample Output 1

8
4
4
1
1
1
5
5
5
5
 

Explanation

n = 10, arr = [8, 5, 5, 5, 5, 1, 1, 1, 4, 4]

First, we separate our numbers by frequency.

The subset of numbers having frequency 1 is [8]

The subset of numbers having frequency 2 is [4]

The subset of numbers having frequency 3 is [1].

The subset of numbers having frequency 4 is [5].

Our partially sorted data (with respect to and in ascending order of frequency) can be expressed as [[8],[4, 4],[1, 1, 1],[5, 5, 5, 5]].

No more sorting is required.
