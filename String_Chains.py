Given an array of words representing your dictionary, you test each word to see if it can be made into another word in the dictionary. This will be done by removing successive characters. Each word represents its own first element of its string chain, so start with a length of 1. Each time you remove a character, increment your string chain by 1. In order to remove a character, the resulting word must be in your original dictionary. Your goal is to determine the longest string chain achievable for a given dictionary.

 

For example, given a dictionary [a, and, an, bear], the word and could be reduced to an and then to a. The single character a cannot be reduced any further as the null string is not in the dictionary. This would be the longest string chain, having a length 3. The word bear cannot be reduced at all.

 

Function Description 

Complete the function longestChain in the editor below. The function must return a single integer representing the length of the longest string chain.

 

longestChain has the following parameter(s):

    words[words[0],...words[n-1]]:  an array of strings to test

 

Constraints

1 ≤ n ≤ 50000
1 ≤ |words[i]| ≤ 60, where 0 ≤ i < n
Each words[i] is composed of lowercase letters in ascii[a-z].
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the words array.

The next n lines each contain a value words[i] where 0 ≤ i < n.

 

 

Sample Case 0
Sample Input 0

6
a
b
ba
bca
bda
bdca
 

Sample Output 0

4
 

Explanation 0

Sample Case 1: words = {"a", "b", "ba", "bca", "bda", "bdca"}

Because "a" and "b" are single-character words, we cannot remove any characters from them as that would result in the empty string, so the length for both of these string chains is 1.

 

The word "ba" can create two different string chains each with a length of 2:  ("ba" → "a" and "ba" → "b"). This means our current longest string chain is 2.

 

The word "bca" can create two different string chains of length 3:  ("bca" → "ba" → "a" and "bca" → "ba" → "b"). This means our current longest string chain is now 3.

 

The word "bda" can create two different string chains of length 3:  ("bda" → "ba" → "a" and "bda" → "ba" → "b"). At this point, our current longest string chain is still 3.

 

The word "bdca" can create four different string chains of length: 4 ("bdca" → "bda" → "ba" → "a", "bdca" → "bda" → "ba" → "b", "bdca" → "bca" → "ba" → "a", and "bdca" → "bca" → "ba" → "b"). This means our current longest string chain is now 4.

 

The longest string chain is 4.
