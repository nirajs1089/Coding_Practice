Two numbers, without leading zeros, are similar if rearranging the digits gives matching numbers, i.e., numbers with the equal frequency of each digit. For example, the numbers 1100 and 1001 are similar, but 1100 and 0110 are not similar because 0110 has a leading zero.

 

Given 2 strings representing long integers a and b, check their similarity. Based on your finding, determine one of the following:

 

If a and b are similar, find the total number of similar numbers to a.
If a and b are not similar, find the total number of similar numbers to b.
 

For example, if a = 112 and b = 121, they are similar. We count the 3 numbers similar to a: {112, 121, 211}.

If a = 11 and b = 223, they are not similar so we count the 3 numbers similar to b: {223, 232, 322}. 

 

Function Description 

Complete the function findSimilar in the editor below. The function must return a long integer, the number of integers similar to a or b as required.

 

findSimilar has the following parameter(s):

    a:  a string representing a long integer

    b:  a string representing a long integer

 

Constraints

1 ≤ numeric values of a and b ≤ 1015
The inputs do not contain ambiguous values. Specifically, there will be no leading zeros such as a = 002, b = 200. 
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains a string representing a long integer a.

The first line contains a string representing a long integer b.

 

Sample Case 0
Sample Input 0

1234
2341
 

Sample Output 0

24
 

Explanation 0

Given a = 1234 and b = 2341, they are similar (equal frequency of all digits). We count the similar numbers to a:

{1234, 1243, 1324, 1342, 1423, 1432, 2134, 2143, 2314, 2341, 2413, 2431, 3124, 3142, 3214, 3241, 3412, 3421, 4123, 4132, 4213, 4231, 4312, 4321}

The total number of similar numbers is 24.

 

Sample Case 1
Sample Input 1

1100
1001
 

Sample Output 1

3
 

Explanation 1

Given a = 1100 and b = 1001, they are similar numbers. We count the similar numbers we can form by rearranging the digits of a:

{1100, 1010, 1001}

The total number of similar numbers is 3.

 

Sample Case 2
Sample Input 2

1234
1213
 

Sample Output 2

12
 

Explanation 2

Given a = 1234 and b = 1213, they are not similar numbers. We count the similar numbers we can form by rearranging the digits of b:

{1123, 1132, 1213, 1231, 1312, 1321, 2113, 2131, 2311, 3112, 3121, 3211}

The total number of similar numbers is 12.
