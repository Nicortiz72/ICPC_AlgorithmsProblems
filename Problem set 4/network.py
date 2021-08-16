from sys import *
from collections import deque

def BFS(G,src,end):
	visited=[0 for i in range(len(G))]
	visited[src]=1
	que=deque()
	que.append((src,0))
	ans=-1
	while(len(que)!=0):
		u,d=que.popleft()
		for v in G[u]:
			if(visited[v]==0):
				que.append((v,d+1))
				if(v==end): ans=d
				visited[v]=1
	return ans

def main():
	n=int(stdin.readline())
	for i in range(n):
		N=int(stdin.readline())
		G=[[] for _ in range(N)]
		for j in range(N):
			line=[int(x) for x in stdin.readline().split()]
			G[line[0]]=line[2:]
		src,end=[int(x) for x in stdin.readline().split()]
		print(src,end,BFS(G,src,end))
main()
