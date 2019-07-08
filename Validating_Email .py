We consider an email address in the form user@domain.extension to be valid if its domain and extension are hackerrank.com and the value of user satisfies the following constraints:

It starts with between 1 and 6 lowercase English letters denoted by the character class [a-z].
The lowercase letter(s) are followed by an optional underscore, i.e. zero or one occurrence of  the _ character.
The optional underscore is followed by 0 to 4 optional digits denoted by the character class [0-9]. 
Complete the code in the editor below by replacing the blank ("________") with a regular expression that matches valid email addresses according to the criteria above. Locked code in the editor prints True for each correct match and False for each incorrect match.

An example of a valid email is abcdef_1234@hackerrank.com.  It has as many of each class of character as possible.  The address a1_1@baddomain.com fails for two reasons.  First, digits cannot precede the underscore.  Second, the domain fails because it is not hackerrank.

Constraints

1 ≤ query ≤ 103
1 ≤ string length ≤ 103.
Input Format
Locked stub code reads strings from stdin and processes them with your regex.

The first line contains an integer, query, describing the total number of target strings to match against the regular expression.
Each line i of the query subsequent lines contains a string describing the ith email address to validate.
Sample Case 0
Sample Input 0

5
julia@hackerrank.com
julia_@hackerrank.com
julia_0@hackerrank.com
julia0_@hackerrank.com
julia@gmail.com
Sample Output 0

True
True
True
False
False
Explanation 0

We perform the following query = 5 validations:

julia@hackerrank.com starts with between 1 and 6 lowercase letters and contains zero of the optional characters, so it's valid.
julia_@hackerrank.com starts with between 1 and 6 lowercase letters, is followed by a single underscore, and contains none of the optional digits, so it's valid.
julia_0@hackerrank.com starts with between 1 and 6 lowercase letters, is followed by a single underscore, and is followed by between 0 and 4 digits, so it's valid.
julia0_@hackerrank.com has valid lowercase letters followed by a valid digit, but the digit must not precede the underscore.
julia@gmail.com has a valid user name, but its domain and extension do not match hackerrank.com.
