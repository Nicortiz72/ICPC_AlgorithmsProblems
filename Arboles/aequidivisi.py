from sys import stdin
from collections import deque
visited=None
change=[[1,0],[-1,0],[0,1],[0,-1]]
def next(M,n,x,y):
	ans=[]
	for i in change:
		if(0<=x+i[0]<n and 0<=y+i[1]<n and visited[x+i[0]][y+i[1]]==0 and M[x][y]==M[x+i[0]][y+i[1]]):
			ans.append([x+i[0],y+i[1]])
	return ans


def Dfs(M,n,x,y):
	global visited
	stack=[[x,y]]
	cont=0
	while(len(stack)!=0):
		i,j=stack.pop()
		visited[i][j]=1
		cont+=1
		for u in next(M,n,i,j):
			stack.append(u)
	return cont
def Bfs(M,n,x,y):
	global visited
	qqe=deque();qqe.append([x,y])
	cont=0
	while(len(qqe)!=0):
		i,j=qqe.popleft()
		visited[i][j]=1
		cont+=1
		for u in next(M,n,i,j):
			qqe.append(u)
	return cont


def solve(M,n):
	i=0; ok=True
	while(i<n and ok):
		j=0
		while(j<n and ok):
			if(visited[i][j]!=1):
				cont=Dfs(M,n,i,j)
				if(cont!=n): ok=False
			j+=1
		i+=1
	if(ok and all([all(i) for i in visited])): return "good"
	else: return "wrong"
	

def main():
	global visited
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
		print("wrong" if ok else solve(M,n))
		n=int(stdin.readline())
main()