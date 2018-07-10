You have a boutique that specializes in words that don't have adjacent matching characters. Bobby, a competitor, has decided to get out of the word business altogether and you have bought his inventory. Your idea is to modify his inventory of words so they are suitable for sale in your store. To do this, you find all adjacent pairs of matching characters and replace one of the characters with a different one. Determine the minimum number of characters that must be replaced to make a salable word.

 

For example, you purchased words = [add, boook, break]. You will create an array with your results from the tests. Change d in add, change o in boook and no change is necessary in break. The return array result = [1,1,0].

 

Function Description 

Complete the function minimalOperations in the editor below. The function must return an array of integers, each result[i] being the minimum operations needed to fix word[i].

 

Constraints

1 ≤ n ≤ 100
2 ≤ |words[i]| ≤ 105
Each character of words[i] ∈ ascii[a-z].
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array words.

Each of the next n lines contains a string words[i].

 

Sample Case 0
Sample Input 0

5
ab
aab
abb
abab
abaaaba
 

Sample Output 0

0
1
1
0
1
 

Explanation 0

 

word = "ab" is already salable so result[0] = 0.
word = "aab" is not salable. We can replace word[0] = 'a' with 'g' to get the string "gab", so result[1] = 1.
word = "abb" is not salable. We can replace word[2] = 'b' with 'c' to get the string "abc", so result[2] = 1.
word = "abab" is already salable so result[3] = 0.
word = "abaaaba" is not salable. We can replace word[3] = 'a' with 'b' to get the string "abababa" and result[4] = 1.
 

We then return result = [0, 1, 1, 0, 1].
