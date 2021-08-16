from sys import *
def main():
    n,m=map(int,stdin.readline().split())
    while n!=0 or m!=0:
        G=[True for _ in range(n)]
        for i in range(m):
            x=int(stdin.readline().split()[1])
            if(G[abs(x)-1] and x<0): G[abs(x)-1]=False;n-=1
        print(n)
        n,m=map(int,stdin.readline().split())
main()