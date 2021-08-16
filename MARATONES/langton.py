from sys import *

def solve(M,x,y):
    est=1
    cnt=0
    while(x!=len(M)-1 or y!=len(M)-1):
        if(M[y][x]==1): est=(est+1)%4
        else: est=(est-1)%4
        M[y][x]=(M[y][x]+1)%2
        if(est==0): x-=1
        elif(est==1): y+=1
        elif(est==2): x+=1
        elif(est==3): y-=1
        if(x>=len(M) or y>=len(M) or x<0 or y<0): print("Kaputt!");return 1
    print("Yes")

def main():
    n,c,x,y=map(int,stdin.readline().split())
    while(n!=0 or c!=0 or x!=0 or y!=0):
        M=[[None for _ in range(n)] for _ in range(n)]
        num=[int(x) for x in list(bin(c))[2:]]
        n2=n**2
        for i in range(n):
            for j in range(n):
                if((n*i)+j>=n2-len(num)):
                    M[i][j]=num[(n*i)+j-n2]
                else:
                    M[i][j]=0
        solve(M,x-1,y-1)
        n,c,x,y=map(int,stdin.readline().split())
main()