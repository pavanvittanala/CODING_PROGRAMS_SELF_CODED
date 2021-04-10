''' ----->>>>> PALINDROME OF STRING USING RECURSION <<<<<----- '''
def pali(st):
    if len(st) == 0 or len(st) == 1:
        return True
    
    if st[0] == st[-1]:
        return pali(st[1:-1])
    return False
p=int(input())
if pali(p):
    print("Yes")
else:
    print("No")
