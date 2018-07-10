The complement of a number is defined here as the number's bitwise inversion from its highest-order 1-bit through its lowest-order bit. For example, the number n = 5 is represented as 00000101 in 8 bit binary. The highest order bit is in the 4's position. The binary complement of n is 010, which is 2 in decimal notation.

 

Function Description 

Complete the function getIntegerComplement in the editor below. The function must return the complement of n as a base 10 integer.

 

getIntegerComplement has the following parameter(s):

    n:  an ineteger in base 10

 

Constraints

0 ≤ n ≤ 105
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The single integer n
Sample Case 0
Sample Input

50
 

Sample Output 0

13
Explanation 0

(50)10 converts to (110010)2. When we invert each bit in the sequence we get (001101)2, which equals (13)10.

Sample Case 1
Sample Input

100
 

Sample Output 1

27
 

Explanation 1

(100)10 converts to (1100100)2. When we invert each bit in the sequence we get (0011011)2, which equals (27)10.
