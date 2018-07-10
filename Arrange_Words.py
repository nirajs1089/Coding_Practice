
We define a We define  sentence to be a string of space-separated words that starts with a capital letter followed by lowercase letters and spaces, and ends with a period, i.e., it satisfies the regular expression ^[A-Z][a-z ]*\.$. We want to rearrange the words in a sentence such that the following conditions are satisfied:

 

Each word is ordered by length, ascending.
Words of equal length must appear in the same order as in the original sentence.
The rearranged sentence must be formatted to satisfy the regular expression ^[A-Z][a-z ]*\.$
 

For example, consider the sentence Cats and hats. First the words are ordered by length, maintaining original order for ties: [and, cats, hats]. Now reassemble the sentence, applying formatting: And cats hats.

 

Function Description 

Complete the function arrange in the editor below. The function must return a properly formed sentence arranged as described.

 

arrange has the following parameter(s):

    sentence:  a well formed sentence string

 

Constraints

2 ≤ | sentence | < 105
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

A single line of space-separated words denoting sentence.

Sample Case 0
Sample Input 0

The lines are printed in reverse order.
Sample Output 0

In the are lines order printed reverse.
Explanation 0

We organize the strings of each respective length in sentence = The lines are printed in reverse order. as:

Length 2: {in}
Length 3: {the, are}
Length 5: {lines, order}
Length 7: {printed, reverse}
We then reassemble our sequences of words as a sentence string, ensuring that the first letter is uppercase, the intermediate letters are lowercase, and the string terminates with a period. We return In the are lines order printed reverse. as our answer.

Sample Case 1
Sample Input 1

Here i come.
Sample Output 1

I here come.
Explanation 1

We organize the strings of each respective length in sentence = Here i come. as:

Length 1: {i}
Length 4: {here, come}
We then reassemble and format our sentence as: I here come..

Sample Case 2
Sample Input 2

I love to code.
Sample Output 2

I to love code.
Explanation 2

We organize the strings of each respective length in sentence = I love to code. as:

Length 1: {i}
Length 2: {to}
Length 4: {love, code}
We then reassemble and format our string as I to love code..
