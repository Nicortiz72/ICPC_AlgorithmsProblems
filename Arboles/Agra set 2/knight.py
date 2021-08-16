from sys import stdin
from collections import deque

change=[(1,1),(1,-1),(-1,1),(-1,-1)]
def next(R,C,M,N,x,y,visited):
	ans=set()
	for c1,c2 in change:
		if(0<=x+(c1*M)<R and 0<=y+(c2*N)<C):
			if(visited[x+(c1*M)][y+(c2*N)]!=-1):
				ans.add((x+(c1*M),y+(c2*N)))
		if(0<=x+(c1*N)<R and 0<=y+(c2*M)<C):
			if(visited[x+(c1*N)][y+(c2*M)]!=-1):
				ans.add((x+(c1*N),y+(c2*M)))
	return ans

def solve(R,C,M,N,visited):
	que=deque()
	que.append((0,0))
	visited[0][0]=1
	Ans=[[0 for e in range(C)] for t in range(R)]
	while(len(que)!=0):
		x,y=que.popleft()
		for x1,y1 in next(R,C,M,N,x,y,visited):
			Ans[x1][y1]+=1
			if(visited[x1][y1]==0):
				que.append((x1,y1))
				visited[x1][y1]=1
	even=0
	odd=0
	for i in Ans:
		for j in i:
			if(j!=0):
				if(j%2==0): even+=1
				else: odd+=1
	if(even+odd==0): even=1
	return even,odd 



def main():
	n=int(stdin.readline())
	for i in range(n):
		R,C,M,N=[int(x) for x in stdin.readline().split()]
		visited=[[0 for e in range(C)] for t in range(R)]
		n1=int(stdin.readline())
		for j in range(n1):
			x,y=stdin.readline().split()
			visited[int(x)][int(y)]=-1
		even, odd=solve(R,C,M,N,visited)

		print('Case {0}: {1} {2}'.format(i+1,even,odd))
main()
