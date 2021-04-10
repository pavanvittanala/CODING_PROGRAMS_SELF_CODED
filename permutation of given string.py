''' ---->>>> FIND ALL PERMUTATIONS OF A GIVEN STRING USINNG PYTHON <<<<<----- '''
def permu(ss,l,r):
    if l==r:
        print(''.join(ss))
    else:
        for i in range(l,r+1):
            ss[i],ss[l]=ss[l],ss[i]
            permu(ss,l+1,r)
            ss[i],ss[l]=ss[l],ss[i]

st=list(str(input()))
permu(st,0,len(st)-1)
