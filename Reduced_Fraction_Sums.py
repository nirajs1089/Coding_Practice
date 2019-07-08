Consider two fractions in the form a/b and c/d, where a, b, c, and d are integers. Given a string describing an arithmetic expression that sums these two fractions in the form a/b+c/d, compute the sum and  fully reduce the resultant fraction to its simplest form.

 For example:

The expression 1/2+1/6 evaluates to 4/6, which we reduce to the string 2/3.
The expression 7/10+13/10 evaluates to 20/10, which we reduce to the string 2/1.
 

Function Description 

Complete the function reducedFractionSums in the editor below. The function must return an array of strings representing the fully reduced fractions.

 

reducedFractionSums has the following parameter(s):

    expressions[expressions[0],...expressions[n-1]]:  an array of strings in the form a/b+c/d.

Constraints

1 ≤ n ≤ 500
1 ≤ a, b, c, d ≤ 2000
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array expressions.

The next n lines each contain an element expressions[i].

Sample Case 0
Sample Input 0

5
722/148+360/176
978/1212+183/183
358/472+301/417
780/309+684/988
258/840+854/686
Sample Output 0

2818/407
365/202
145679/98412
4307/1339
1521/980
Explanation 0

We perform the following n = 5 calculations:

722/148+360/176 = 127072/26048+53280/26048 = 180352/26048 = 2818/407.
978/1212+183/183 = 978/1212 + 1212/1212 = 2190/1212 = 365/202.
358/472+301/417 evaluates to the reduced fraction 145679/98412.

780/309+684/988 → 4307/1339.
258/840+854/686 → 1521/980.
Return the array ["2818/407", "365/202", "145679/98412", "4307/1339", "1521/980"] .

Sample Case 1
Sample Input1

10
241/26+612/398
278/348+246/157
156/53+952/760
263/418+560/304
540/28+44/295
636/78+354/868
68/415+1041/807
147/269+224/844
759/120+370/72
654/162+476/307
Sample Output 1

55915/5174
64627/27318
21127/5035
1033/418
40133/2065
48305/5642
162297/111635
46081/56759
4127/360
46315/8289
Explanation 1

We perform the following n = 10 calculations:

241/26+612/398 → 55915/5174.
278/348+246/157 → 64627/27318.
156/53+952/760 → 21127/5035.
263/418+560/304 → 1033/418.
540/28+44/295 → 40133/2065.
636/78+354/868 → 48305/5642.
68/415+1041/807 → 162297/111635.
147/269+224/844 → 46081/56759.
759/120+370/72 → 4127/360.
654/162+476/307 → 46315/8289.
Return the array ["55915/5174", "64627/27318", "21127/5035", "1033/418", "40133/2065", "48305/5642", "162297/111635", "46081/56759", "4127/360", "46315/8289"] .
