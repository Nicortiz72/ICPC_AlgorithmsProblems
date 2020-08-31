from sys import stdin
from sys import stdout
import math
import operator as op
from functools import reduce

#Nicolas Ortiz
#Uva problem Binomial coefficient
#final project algorithm design

import time
inTime=time.time()

H=[0, 0, 44721361, 181714, 12449, 2608, 950, 473, 286, 197, 148, 119, 
   100, 87, 78, 72, 67, 63, 61, 59, 57, 56, 55, 54, 54, 54, 54, 54, 54, 
   54, 54, 54, 55, 55, 56, 56, 57, 57, 58, 59, 59, 60, 
   61, 61, 62, 63, 63, 64, 65, 66, 67, 67, 68, 69, 70, 71, 72, 72, 73, 74]

M3={}
def Choose(n, r):
    global M2,M3
    if(r==2): ans=(n*(n-1))>>1
    else:
        ans=M3.get((r,n))
        if(ans==None):
            r = min(r, n-r)
            numer = reduce(op.mul, range(n, n-r, -1), 1)
            denom = reduce(op.mul, range(1, r+1), 1)
            ans=(numer // denom)
            M3[(r,n)]=ans
    return ans

def binary(x,k):
    ans=-1
    fact=int((math.factorial(k)*x)**(1/k))
    for n in range(fact,fact+k+2):
        if(Choose(n,k)==x): ans=n
    return ans


def find(x):
    ans=set()
    lim=-1
    for k in range(2,IK):
        n=binary(x,k)
        if(n!=-1 and Choose(n,k)==x):
            ans.add((n, k))
            ans.add((n, n - k))
    return ans


D={}
IK=4
NM=H[IK]#12449#2700 #NM=2500
KM=30 #1250

def tab():
    global D,M2,M3
    for i in range(IK+1,NM): 
        ans=Choose(i,IK)
        M3[(IK,i)]=ans
        tmp2=D.get(ans)
        if(tmp2!=None):
            D[ans].add((i,IK))
            D[ans].add((i,i-IK))
    for k in range(IK+1,KM):
        for n in range(k+1,H[k]):
            ans=M3.get((k-1,n-1),1)+M3.get((k,n-1),1)
            tmp=D.get(ans)
            M3[(k,n)]=ans
            if(tmp!=None):
                D[ans].add((n,k))
                D[ans].add((n,n-k))

def main():
    global D
    n=int(stdin.readline())
    A=[]
    for i in range(n):
        a=int(stdin.readline())
        A.append(a)
        D[a]=set()
    tab()
    for a in A:
        ans=D.get(a)
        ans.add((a,1));ans.add((a,a-1))
        ans=ans.union(find(a))
        ans=list(ans)
        ans.sort()
        stdout.write(str(len(ans))+"\n")
        stdout.write("({0},{1})".format(ans[0][0],ans[0][1]))
        for (n,k) in ans[1:]:
            stdout.write(" ({0},{1})".format(n,k))
        stdout.write("\n")
    
main()

#stdout.write(str(time.time()-inTime)+"\n")
stdout.close()