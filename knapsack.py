def knapsack(B,W,M):
	N=len(B)
	tab=[[0 for i in range(M+1)] for j in range(N+1)]
	n,m=1,0
	while n!=N+1:
		if m==M+1: n,m=n+1,0
		else:
			tab[n][m]=tab[n-1][m]
			if(W[n-1]<=m):
				tab[n][m]=max(tap[n][m],B[n-1]+tap[n-1][m-W[n-1]])
			m+=1
	return tab[N][M]

def knapsack_opt(B,W,M):
	N=len(B)
	tab=[0 for i in range(M+1)]
	n,m=1,M
	while n!=N+1:
		if m==-1: n,m =n+1,m
		else:
			if(m>=W[n-1]):
				tab[m]=max(tab[m],B[n-1]+tab[m-W[n-1]])
			m-=1
	return tab[N][M]
INF=float('inf')
def CChange(D,X):
	N=len(D)
	tab=[[INF for i in range(X+1)] for j in range(N+1)]
	tab[0][0]=0
	n,x=1,0
	while n!=N+1:
		if(x==X+1): n,x=n+1,0
		else:
			tab[n][x]=tab[n-1][x]
			if(D[n-1]<=x):
				tab[n][x]=min(tab[n][x],1+tab[n][x-D[n-1]])
		x+=1
	return tab

