from sys import *

def solve(N,K,M):
	tab=[[0 for i in range(N+1)] for j in range(K+1)]
	tab[0][0]=1
	for k in range(1,K+1):
		for n in range(1,N+1):
			for m in range(1,M+1):
				if(n-m>=0): tab[k][n]+=tab[k-1][n-m]
	return tab[K][N]

def main():
	line=stdin.readline().strip()
	while line != "":
		N,K,M=[int(x) for x in line.split()]
		print(solve(N,K,M))
		line=stdin.readline().strip()
main()