Digits within an integer go from least significant to most significant from right to left. For instance, in a decimal number, the ones digit is less significant than the tens digit. Given a decimal number, convert it to binary and then determine the value, 1 or 0, at the 4th least significant digit.

 

For example, 2310 = (10111)2. The value of the 4th index from the right in the binary representation is 0.

 

Function Description 

Complete the function fourthBit in the editor below. The function must return a 0 or 1 matching the 4th least significant digit in the binary representation of num.

 

fourthBit has the following parameter(s):

    num:  a decimal integer

 

Constraints

num is a 32 bit integer
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The only line contains an integer num.

Sample Case 0
Sample Input 0

32
Sample Output 0

0
Explanation 0

The integer (32)10 converts to (100000)2. If we 1-index each bit from least to most significant, they are indexed as 654321. The bit at index 4 is 0.

Sample Case 1
Sample Input 1

77
Sample Output 1

1
Explanation 1

The integer (77)10 converts to (1001101)2. If we 1-index each bit from least to most significant, they are indexed as 7654321. The bit at index 4 is 1.
