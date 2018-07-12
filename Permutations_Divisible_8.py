Given an integer string, create all integer permutations of its digits. Determine if there is a permutation whose integer value is evenly divisible by 8, i.e. (permutation value) % 8 = 0.

 

For example, the possible permutations of 123 are p = {123, 132, 213, 231, 312, 321}. Of these values, p[4] = 312 is divisible by 8 because 312 % 8 = 0.

 

Function Description 

Complete the function checkDivisibility in the editor below. The function must return an array of strings, either YES or NO, where each result[i] denotes whether or not arr[i] is divisible by 8.

 

checkDivisibility has the following parameter(s):

    arr[arr[0],...arr[n-1]]:  an array of integer strings

 

Constraints

1 ≤ n ≤ 45
0 ≤ arr[i] ≤ 10110
All characters of arr[i] ∈ {0-9}
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array arr.

Each of the next n lines contains an integer as a string arr[i] where 0 ≤ i < n.

 

Sample Case 0
Sample Input 0

2
61
75
 

Sample Output 0

YES
NO
 

Explanation 0

We must check the following n = 2 values:

arr[0] = 61. The permutation p = 16 is divisible by 8 so we store YES in index 0 of our return array.
arr[1] = 75. Our only possible permutations are p = 75 and p = 57, but neither of them is divisible by 8. We store NO in index 1 of our return array.
 
