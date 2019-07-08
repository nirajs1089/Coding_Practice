IPv4 was the first publicly used Internet Protocol. It used 4-byte addresses and permitted 232 distinct values. The typical format for an IPv4 address is A.B.C.D where A, B, C, and D are integers in the inclusive range between 0 and 255.

 

IPv6, with 128 bits, was developed to permit the expansion of the address space. These addresses are represented by eight colon-separated sixteen-bit groups, where each sixteen-bit group is written using 1 to 4 hexadecimal digits. Leading zeroes in a section are often omitted from an address, meaning that the group 0 is identical to 0000 and group 5 is identical to 0005. Additionally, contiguous zero groups within the address can be replaced with :: but that may only occur once in an address. Some examples of valid IPv6 addresses are 2001:0db8:0000:0000:0000:ff00:0042:8329 and 3:0db8:0:01:F:ff0:0042:8329.  The first address could be shortened to 2001:db8::ff00:42:8329.  

 

Given n strings of text, we want to determine whether each string of text is:

An IPv4 address.
An IPv6 address.
Neither an IPv6 address nor an IPv4 address.
 

Function Description 

Complete the function checkIPs in the editor below. The function must return an array of strings where each element is the result of a query and is ∈ {"IPv4", "IPv6", "Neither"}.

 

checkIPs has the following parameter(s):

    ip_array:  an array of strings to categorize

 

Constraints

1 ≤ n ≤ 50
1 ≤ ip_array[i] ≤ 500
Any string containing a valid IPv4 or IPv6 address has no leading or trailing whitespace.
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array ip_array.

Each of the next n lines contains a string ip_array[i].

Sample Case 0
Sample Input 0

2
This line has junk text.
121.18.19.20
 

Sample Output 0

Neither    
IPv4 
 

Explanation 0

We must check the following n = 2 strings:

ip_array[0] = "This line has junk text." is not a valid IPv4 or IPv6 address, so we return Neither in index 0 of our return array.
ip_array[1] = "121.18.19.20" is a valid IPv4 address, so we return IPv4 in index 1 of our return array.
 

Sample Case 1
Sample Input 1

1
2001:0db8:0000:0000:0000:ff00:0042:8329
 

Sample Output 1

IPv6
 

Explanation 1

We only have n = 1 value to check. Because ip_array[0] = "2001:0db8:0000:0000:0000:ff00:0042:8329" is a valid IPv6 address, we return IPv6 in index 0 of our return array.
