We define a palindrome to be a word that reads the same forward as it does backward. For example, the word "tacocat" is a palindrome, but the words "taco" and "cat" are not. You must determine the minimum number of characters that must be inserted into a string to make it a palindrome.

 

For example, given the string s = "abcda", we can turn s into a palindrome by performing the following sequence of two character insertions: "abcda" → "abdcda" → "abdcdba".

 

Function Description 

Complete the function shortestPalindrome in the editor below. The function must return an integer denoting the minimum number of characters that must be inserted into the string to make it a palindrome.

 

shortestPalindrome has the following parameter(s):

    s:  a string

 

Constraints

1 ≤ |s| ≤ 103
String s consists of lowercase English alphabetic letters only, ascii[a-z].
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The line contains the string s.

 

Sample Case 0
Sample Input 0

abab
 

Sample Output 0

1
 

Explanation 0

We can turn s = "abab" into a palindrome in either of the following ways:

Prepend the letter "b" to the beginning of the string, resulting in the palindrome "babab".
Append the letter "a" to the end of the string, resulting in the palindrome "ababa".
In both the cases, we only need to insert 1 character to make s a palindrome.

 

Sample Case 1
Sample Input 1

abacaba
 

Sample Output 1

0
 

Explanation 1

The string s = "abacaba" is already a palindrome, so the function returns 0.

 
