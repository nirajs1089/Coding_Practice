In this challenge, you will consider a range of positive integers from 1 to a limit.  For each value, you will return a string or the value based on whether the number is a multiple of 3, 5 or both.  Determine the string to return based on the following rules for an integer i:

 

If i is a multiple of both 3 and 5, print FizzBuzz.
If i is a multiple of 3 (but not 5), print Fizz.
If i is a multiple of 5 (but not 3), print Buzz.
For all other is not satisfying the above rules, print the value of i.
 

Function Description 

Complete the function fizzBuzz in the editor below. The function must print FizzBuzz, Fizz, Buzz or the value if it's not a multiple, for each value i ∈ {1, 2, ... n} in ascending order, each on a separate line.  There is no return value expected.

 

fizzBuzz has the following parameter(s):

    n:  upper limit of values to test (inclusive)

 

Constraints

0 < n < 2 × 105
Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The single integer n, the limit of the range to test: [1, 2, ...n].

Sample Case 0
Sample Input 0

15
 

Sample Output 0

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
 

Explanation 0

The numbers 3, 6, 9, and 12 are multiples of three (but not five), so we print Fizz on those lines.

The numbers 5 and 10 are multiples of five (but not three), so we print Buzz on those lines.

The number 15 is a multiple of both three and five, so we print FizzBuzz on that line.

None of the other lines is a multiple of either three or five, so we print the value of i on those lines.
