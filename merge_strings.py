You are merging data from two sources connected to a network access point to create a new data packet.

 

You must merge strings a and b, and then return a single merged string. A merge operation on two strings is described as follows:

Append alternating characters from a and b, respectively, to some new string, mergedString.
Once all of the characters in one of the strings have been merged, append the remaining characters in the other string to mergedString.
 

As an example, assume you have two strings to merge: 'abc' and 'stuvwx'. Alternate between the first and second strings as long as you can:

'a' + 's' + 'b' + 't' + 'c' + 'u'. At this point you have traversed the first string and have generated 'asbtcu'. The remainder of the second string, 'vwx' is now added to the end of the string, creating 'asbtcuvwx'.

 

Function Description 

Complete the function mergeStrings in the editor below. The function must return the merged string.

 

mergeStrings has the following parameter(s):

    a:  first string

    b:  second string

 

Constraints

1 ≤ |a|, |b| ≤ 25000
Input Format For Custom Testing
Input from stdin will be processed as follows and passed to the function:

 

The first line contains string a.

The second line contains string b.

Sample Case 0
 

Sample Input 0

abc
def
 

Sample Output 0

adbecf
 

Explanation 0

a = abc

b = def

Taking alternate characters from both the strings, we get adbecf

Sample Case 1
 

Sample Input 1

ab
zsd
 

Sample Output 1

azbsd
 

Explanation 1

a = ab

b = zsd 

Taking alternate characters from both the strings, we get azbsd. After string a is exhausted, the remainder of string b is concatenated.
