from sys import *
INF=float('inf')
def solve(W,L):
	N=len(W);M=(max(L)+max(W))
	tab=[[0 for i in range(M+1)] for j in range(N+1)]
	#for i in range(M+1): tab[0][i]=INF
	n,m=1,0
	while n!=N+1:
		if(m==M+1): n,m=n+1,0
		else:
			tab[n][m]=tab[n-1][m]
			if(W[n-1]<=m):
				tab[n][m]=max(tab[n][m],tab[n-1][min(L[n-1],m-W[n-1])]+1)
			m+=1
	#print(tab)
	return max(tab[N])


def main():
	n=int(stdin.readline())
	while n!=0:
		W,L=list(),list()
		for i in range(n):
			w,l=[int(x) for x in stdin.readline().split()]
			W.append(w);L.append(l)
		W.reverse();L.reverse()
		print(solve(W,L))
		n=int(stdin.readline())
main()