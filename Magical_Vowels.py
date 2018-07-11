We define a magical subsequence to be a sequence of letters within a string that contains all five vowels in order: a, e, i, o, u. There can be any number of occurrences of each vowel, but they must be in that order. For instance, aeeiou is a magical subsequence, but aeaioua is not. The magical subsequences of each string (red) would be aeeiou and aeaioua with lengths of 6 and 5 respectively.

 

Julia has a string, s, consisting of one or more of the following letters: a, e, i, o, and u. She wants to determine the longest magical subsequence in her string.

 

Function Description 

Complete the function longestSubsequence in the editor below. The function must return the length of the longest magical subsequence within the input string. If one does not occur in the string, return 0

 

longestSubsequence has the following parameter(s):

    s:  the string to analyze

 

Constraints

5 < |s| < 5 × 105
String s is composed of English vowels (i.e., a, e, i, o, and u).
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

There is one line containing s.

Sample Case 0
Sample Input 0

aeiaaioooaauuaeiou
 

Sample Output 0

10
 

Explanation 0

In the table below, the component characters of the longest magical subsequence are red:

a	e	i	a	a	i	o	o	o	a	a	u	u	a	e	i	o	u
 

Sample Case 1
Sample Input 1

aeiaaioooaa
 

Sample Output 1

0
 

Explanation 1

String s does not contain the letter u, so it is not possible to construct a magical subsequence.
