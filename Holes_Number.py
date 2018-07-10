You are designing a poster which prints out numbers with a unique style applied to each of them.  The styling is based on the number of closed paths or holes present in a given number.  

 

The number of holes that each of the digits from 0 to 9 have are equal to the number of closed paths in the digit. Their values are:

1, 2, 3, 5, and 7 = 0 holes.
0, 4, 6, and 9 = 1 hole.
8 = 2 holes.
 

Given a number, you must determine the sum of the number of holes for all of its digits. For example, the number 819 has 3 holes.

 

Function Description 

Complete the function countHoles in the editor below. The function must return an integer denoting the total number of holes in num.

 

countHoles has the following parameter(s):

    num:  the integer to process

 

Constraints

1 ≤ num ≤ 109
Input Format For Custom Testing
Input from stdin will be processed as follows and passed to the function:

 

There is one line of text containing a single integer num, the value to process.

Sample Case 0
Sample Input

630
 

Sample Output

2
 

Explanation

Add the holes count for each digit, 6, 3 and 0. Return 1 + 0 + 1 = 2.

Sample Case 1
Sample Input

1288
 

Sample Output

4
 

Explanation

Add the holes count for each digit, 1, 2, 8, 8. Return 0 + 0 + 2 + 2 = 4.
