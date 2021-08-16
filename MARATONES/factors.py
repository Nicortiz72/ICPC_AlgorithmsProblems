from sys import *
N=100001

C=[0 for i in range(N)]

for i in range(2,N):
    if(C[i]==0):
        for j in range(i,N,i):
            if(C[j]==0 and j%i==0):
                C[j]=i

def factors(x):
    ans=[]
    while x!=1:
        ans.append(C[x])
        x=x//C[x]
    return ans

Mem=[None for _ in range(N)]
Mem[1]=(0,0)
S=set()
cont=0
for i in range(2,N):
    f=factors(i)
    cont+=len(f)
    for j in f: S.add(j)
    Mem[i]=(len(S),cont)
        
def main():
    T=int(stdin.readline())
    for i in range(T):
        n=int(stdin.readline())
        print(Mem[n][0],Mem[n][1])
main()
