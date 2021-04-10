''' Repeated String
Lilah has a string, , of lowercase English letters that she repeated infinitely many times.
Given an integer, , find and print the number of letter a 's in the first letters of Lilah's infinite string.
Input Format
The first line contains a single string, .
The second line contains an integer, .
Constraints
For of the test cases, .
Output Format
Print a single integer denoting the number of letter a 's in the first letters of the infinite string created by
repeating infinitely many times.
Sample Input 0
aba
10
Sample Output 0
7
Explanation 0
The first letters of the infinite string are abaabaabaa . Because there are a 's, we print on a
new line.
Sample Input 1
a
1000000000000
Sample Output 1
1000000000000
Explanation 1
Because all of the first letters of the infinite string are a , we print
on a new line. '''

                                                            '''----->>>>> SOLUTION <<<<<----- '''
def repeatedString(s, n):
    ls=list(s)
    l=len(ls)
    if n <= len(ls):
        return ls[:n].count("a")
    if ls.count("a") == l:
        return n
    mt=n//l
    rt=n%l
    print("-->>",mt,rt)
    ca=ls.count("a")
    print("->>>",ca)
    ca = (ca*mt) + ls[:rt].count("a")
    return ca
s = input()
n = int(input())
result = repeatedString(s, n)
