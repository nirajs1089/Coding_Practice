Given a string, s, we define a substring to be a non-empty string that can be obtained by one of the following means:

Removing zero or more characters from the left side of s.
Removing zero or more characters from the right side of s.
Removing zero or more characters from the left side of s and removing zero or more characters from the right side of s.
 

For example, let s = abcde. The substrings are:


 1	abcde
 2	abcd
 3	bcde
 4	abc
 5	bcd
 6	cde
 7	ab
 8	bc
 9	cd
10	de
11	a 
12	b
13	c
14	d
15	e
 

Function Description 

Complete the function substringCalculator in the editor below. The function must return the number of distinct substrings of string s.

 

substringCalculator has the following parameter(s):

    s:  the string to analyze

 

Constraints

String s consists of characters in the range ascii[a-z].
0 ≤ |s| ≤ 105
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

A single line with string s.

Sample Case 0
Sample Input 0

kincenvizh
Sample Output 0

53
Explanation 0

String s = kincenvizh has the following distinct substrings:

 1 kincenvizh
 2 kincenviz
 3 kincenvi
 4 kincenv
 5 kincen
 6 kince
 7 kinc
 8 kin
 9 ki
10 k
11 incenvizh
12 incenviz
13 incenvi
14 incenv
15 incen
16 ince
17 inc
18 in
19 i
20 ncenvizh
21 ncenviz
22 ncenvi
23 ncenv
24 ncen
25 nce
26 nc
27 n
28 cenvizh
29 cenviz
30 cenvi
31 cenv
32 cen
33 ce
34 c
35 envizh
36 enviz
37 envi
38 env
39 en
40 e
41 nvizh
42 nviz
43 nvi
44 nv
45 vizh
46 viz
47 vi
48 v
49 izh
50 iz
51 zh
52 z
53 h

About
