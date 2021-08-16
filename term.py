from sys import *

def solve(A,N,M):
	tab=[[0 for _ in range(M+1)] for _ in range(N+1)]
	for n in range(1,N+1):
		for m in range(M,-1,-1):
			a=A[n-1][0]+tab[n-1][m]
			for j in range(1,m+1):
				if(A[n-1][j]>=5):
					a=max(a,tab[n-1][m-j]+A[n-1][j])
			if(a<5): return -1
			tab[n][m]=a
	return max(tab[N])

def solve2(A):
	s=0
	for i in range(len(A)):
		if(A[i][0]<5): return -1
		s+=A[i][0]
	return s


def main():
	t=int(stdin.readline())
	for _ in range(t):
		n,m=[int(x) for x in stdin.readline().split()]
		A=list()
		for i in range(n):
			A.append([int(x) for x in stdin.readline().split()])
		print(n,m)
		if(m==n): ans=solve2(A)
		else: ans =solve(A,n,m-n)
		if(ans==-1): print("Peter, you shouldnt have played billiard that much.")
		else: ans=float(ans)/n;print("Maximal possible average mark - %.2f."%ans)
main()
