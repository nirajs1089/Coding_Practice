Given two usernames, the degree of similarity is defined as the length of the longest prefix common to both strings. In this challenge, you will be given a string. You must break the string to create ever shorter suffixes, then determine the similarity of the suffix to the original string. Do this for each suffix length from the length of the string to 0, and cumulate the results.

 

As an example, consider the string 'ababa'. Compare all suffixes to the original string.

Discard	Suffix	Similarity	Length
''	'ababa'	'ababa'	5
'a'	'baba'	''	0
'ab'	'aba'	'aba'	3
'aba'	'ba'	''	0
'abab'	'a'	'a'	1
'ababa'	''	''	0
 

 

 

 

 

 

 

 

 

 

 

 

So our sum is 5 + 0 + 3 + 0 + 1 + 0 = 9

 

Function Description 

Complete the function usernameDisparity in the editor below. The function must return an integer array of the sums of the similarities for each test case.

 

usernameDisparity has the following parameter(s):

    inputs[inputs[0],...inputs[n-1]]:  an array of username strings to process

 

Constraints

1 ≤ T ≤ 10

1 ≤ |s| ≤ 105

The string contains only letters in the range ascii[a-z].

 

Input Format For Custom Testing
Input from stdin will be processed as follows and passed to the function usernameDisparity:

 

The first line contains the number of test cases T.

The next T lines each contain a string representing the value of string S for each test case.

Sample Case 0
Sample Input 0

1
ababaa 
Sample Output 0

11

Explanation 0

 

T = 1

S = ababaa

The suffixes of the string are ababaa, babaa, abaa, baa, aa and a. The similarities of each of these strings with the string ababaa are 6,0,3,0,1,1 respectively.

The sum is calculated 6 + 0 + 3 + 0 + 1 + 1 = 11.

Sample Case 1
Sample Input 1

1
aa
Sample Output 1

3
Explanation 1

 

T = 1

S = aa

The Suffixes of the string are aa, a.The similarities of each of these strings with the string aa is 2, 1 .

The sum is calculated 2 + 1 = 3.
