                                                   ''' ----->>>>> PROBLEM STATEMENT <<<<<----- '''
''' You are given a string that is formed from only three characters ‘a’, ‘b’, ‘c’. You are allowed to change atmost ‘k’ characters in the given string while attempting to optimize the uniformity index.
Note : The uniformity index of a string is defined by the maximum length of the substring that contains same character in it.
Input
The first line of input contains two integers n (the size of string) and k. The next line contains a string of length n.
Output
A single integer denoting the maximum uniformity index that can be achieved.
Constraints
1 <= n <= 10^6
0 <= k <= n
String contains only ‘a’, ‘b’, ‘c’.
Sample Input 0
6 3
abaccc
Sample Output 0
6
Explanation
First 3 letters can be changed to ‘c’ and we can get the string ‘cccccc’ '''

                                                    ''' ----->>>>> SOLUTION: <<<<<---- '''
n,k=map(int,input("\n 6 3").split())
st=input("Enter a string:")
c1,c2,c3=st.count("a"),st.count("b"),st.count("c")
if c1 <=c2:
    if c2<=c3 and c1+c2 <=k:
        st=st.replace("a","c")
	st=st.replace("b","c")
    elif c2>c3 and c1+c3<=k:
	st=st.replace("a","b")
	st=st.replace("c","b")
    else:
        print("K is Wrong, for given input")
elif c1 <= c3:
    st=st.replace("a","c")
    st=st.replace("b","c")
else:
    st=st.replace("b","a")
    st=st.replace("c","a")
print("Finalllll String :",st)
