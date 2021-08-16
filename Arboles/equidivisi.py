from sys import stdin
vis=None
change=[(0,1),(1,0),(-1,0),(0,-1)]
def dfs(r,c,n,M):
	global vis
	vis[r][c]=1
	for i in change:
		if(0<=r+i[0]<n and 0<=c+i[1]<n and vis[r+i[0]][c+i[1]]==0 and M[r][c]==M[r+i[0]][c+i[1]]):
			dfs(r+i[0],c+i[1],n,M)

	
def solve(M):
	global vis
	n=len(M)
	vis=[[0 for i in range(n)]for j in range(n)]
	res=[False for i in range(n)]
	for r in range(n):
		for c in range(n):
			if(vis[r][c]==0 and not(res[M[r][c]])):
				res[M[r][c]]=True
				dfs(r,c,n,M)
	return all([all(i) for i in vis]) and all(res)

def main():
	global vis
	n=int(stdin.readline())
	while(n!=0):
		visited=[[0 for i in range(n)]for j in range(n)]
		M=[[n-1 for i in range(n)] for j in range(n)]
		ok=False
		for u in range(n-1):
			A=[int(i) for i in stdin.readline().split()]
			if(len(A)<n+n): ok=True
			for i,j in zip(A[::2],A[1::2]):
				M[i-1][j-1]=u
		print("good" if solve(M) else "wrong")
		n=int(stdin.readline())
main()

