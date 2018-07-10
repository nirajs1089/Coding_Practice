You will be given an array of the lengths of a number of sticks.  When a turn begins, you must count the number of sticks you have.  Determine the length of a stick with the shortest length and discard any sticks of that length.  Remove that length from each of the longer sticks and discard the offcuts.  Repeat until there are no sticks left.  Return an array where the elements are the numbers of sticks you had at the beginning of each turn.

 

For example, consider an array representing the lengths of four sticks: [1, 1, 2, 3].  The shortest sticks are 1 unit long.  Discard them.  Remove 1 unit from the other two sticks and discard the scrap.  Now you have two sticks lengths [1, 2].  Do the same and you'll have one stick of length [1].  Discard it and return an array with the number of sticks you had at the start of each turn: [4, 2, 1].

lengths     cut length      sticks
1 1 2 3          1            4
_ _ 1 2          1            2
_ _ _ 1          1            1
_ _ _ _        DONE        DONE
 

Function Description 

Complete the function cutSticks in the editor below. The function must return an array of integers representing the number of sticks at the start of each turn.

 

cutSticks has the following parameter(s):

    lengths[lengths[0],...lengths[n-1]]:  an array of integers representing the starting stick lengths

 

Constraints

1 ≤ n ≤ 103
1 ≤ lengths[i] ≤ 103, where 0 ≤ i < n
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the number elements in lengths.

The next n lines each represents lengths[i] where 0 ≤ i < n.

 

Sample Case 0
Sample Input 0

6
5
4
4
2
2
8
 

Sample Output 0

6
4
2
1
 

Explanation 0

  lengths     cut length      sticks
5 4 4 2 2 8          2           6
3 2 2 _ _ 6          2           4
1 _ _ _ _ 4          1           2
_ _ _ _ _ 3          3           1
_ _ _ _ _ _        DONE        DONE
Sample Case 1
Sample Input 1

8
1
2
3
4
3
3
2
1
 

Sample Output 1

8
6
4
1
 

Explanation 1

    lengths       cut length   sticks
1 2 3 4 3 3 2 1       1           8
_ 1 2 3 2 2 1 _       1           6
_ _ 1 2 1 1 _ _       1           4
_ _ _ 1 _ _ _ _       1           1
_ _ _ _ _ _ _ _     DONE        DONE
