Consider a string consisting of the characters < and > only. We consider the string to be balanced if each < always appears before (i.e., to the left of) a corresponding > character (they do not need to be adjacent). Moreover, each < and > act as a unique pair of symbols and neither symbol can be considered as part of any other pair of symbols.

 

To balance a string, we can replace any > character with <>. Given an expression and a maximum number of replacements, can you turn an unbalanced string into a balanced one?

 

For example, the strings <<>>, <>, and <><> are all balanced, but the strings >>, <<>, and ><>< are unbalanced. The string >> can be balanced in two moves by replacing each > with a <> to make <><>.

 

Function Description 

Complete the function balancedOrNot in the editor below. The function must return an array of integers where element[i] contains a 1 if expressions[i] is balanced or a 0 if it is not.

 

balancedOrNot has the following parameter(s):

expressions[expressions[0],...expressions[n-1]]:  an array of strings to check

maxReplacements[maxReplacements[0],...maxReplacements[n-1]]:  an array of integers representing the maximum number of replacements available for each expressions[i]

 

Constraints

1 ≤ n ≤ 102
1 ≤ length of expressions[i] ≤ 105
0 ≤ maxReplacements[i] ≤ 105
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array expressions.

The next n lines each contain an element expressions[i].

The next line contains an integer n, the size of the array maxReplacements.

The next n lines each contain an element maxReplacements[i].

Sample Case 0
Sample Input 0

2
<>>>
<>>>>
2
2
2
 

Sample Output 0

1
0
 

Explanation 0

We process expressions = ["<>>>", "<>>>>"] and maxReplacements = [2, 2] like so:

 

For string <>>> with maxReplacements[0] = 2, it becomes balanced after two replacements: <>>> → <><>> → <><><>.  The string was converted in ≤ maxReplacements[0] replacements.  Store a 1 in index 0 of our return array.
For string <>>>> with maxReplacements[1] = 2, becomes balanced after three replacements: <>>>> → <><>>> → <><><>> → <><><><>.   There were not enough replacements available, so store a 0 in index 1 of the return array.
 

We then return the array [1, 0] as our answer.

 

Sample Case 1
Sample Input 1

2
<>
<>><
2
1
0
 

Sample Output 1

1
0
 

Explanation 1

We process expressions = ["<>", "<>><"] and maxReplacements = [1, 0] like so:

 

For string <> with maxReplacements[0] = 1, it is already balanced and needs no replacements. Store a 1 in index 0 of the return array.
For string <>>< with maxReplacements[1] = 0, the string is not balanced. It's impossible to balance the string because it ends in < and because there are 0 replacements available. Store a 0 in index 1 of the return array.
 

We then return the array [1, 0] as our answer.
