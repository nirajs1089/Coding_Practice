Given an array of integers, your task is to count the number of duplicate array elements. Duplicate is defined as two or more identical elements. For example, in the array [1, 2, 2, 3, 3, 3], the two twos are one duplicate and so are the three threes.

 

Function Description 

Complete the function countDuplicates in the editor below. The function must return an integer denoting the number of non-unique (duplicate) values in the numbers array.

 

countDuplicates has the following parameter(s):

    numbers[numbers[0],...numbers[n-1]]:  an array of integers to process

 

Constraints

1 ≤ n ≤ 1000
1 ≤ numbers[i] ≤ 1000, 0 ≤ i < n
 

Input Format Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the numbers array.

The next n lines contain an integer describing the value of numbers[i] where 0 ≤ i < n.

Sample Case 0
Sample Input 0

8 
1 
3
1
4
5
6
3
2 
Sample Output 0

2
Explanation 0

n = 8 and numbers = [1, 3, 1, 4, 5, 6, 3, 2]. The integers 1 and 3 both occur more than once, so we return 2 as our answer.

Sample Case 1
Sample Input 1

6
1
1
2
2
2
3
Sample Output 1

2
Explanation 1

n = 6 and numbers = [1, 1, 2, 2, 2, 3]. The integers 1 and 2 both occur more than once, so we return 2 as our answer.
