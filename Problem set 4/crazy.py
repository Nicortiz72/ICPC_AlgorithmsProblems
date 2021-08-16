from sys import *
from collections import deque

AYx=[-2,-1,1,2,-2,-1,1,2]
AYy=[1,2,2,1,-1,-2,-2,-1]

ARx=[-1,0,1,-1,1,-1,0,1]
ARy=[1,1,1,0,0,-1,-1,-1]

def next(M,x,y,f):
	ans=[]
	i=0
	if(f):
		while(i<len(AYx)):
			z1=x+AYx[i];z2=y+AYy[i]
			if(0<=z1<len(M) and 0<=z2<len(M[0])):
				ans.append([z1,z2])
			i+=1
	else:
		while(i<len(AYx)):
			z1=x+ARx[i];z2=y+ARy[i]
			if(0<=z1<len(M) and 0<=z2<len(M[0])):
				ans.append([z1,z2])
			i+=1
	return ans

def solve(T,src,end,H):
	visited=[[0 for i in range(len(T[0]))] for j in range(len(T))]
	visited[src[0]][src[1]]=2
	king=float('inf')
	ans=float('inf')
	que=deque()
	for i in H: que.append([i[0],i[1],0]);visited[i[0]][i[1]]=1
	que.append([src[0],src[1],0])
	while(len(que)!=0):
		x,y,d=que.popleft()
		for x1,y1 in next(T,x,y,visited[x][y]==1):
			if(visited[x1][y1]==0):
				que.append((x1,y1,d+1))
				visited[x1][y1]=1
				if(visited[x][y]==2): 
					visited[x1][y1]=2
					if(T[x1][y1]=='B' and king): ans=min(ans,d+1)
				else:
					if(T[x1][y1]=='B'): king=min(d,king)
			elif(visited[x][y]==2 and T[x1][y1]=='B' and d<=king):
				ans=min(ans,d+1)
	return ans

def main():
	n=int(stdin.readline())
	for i in range(n):
		M,N=[int(x) for x in stdin.readline().split()]
		T=[];H=[]
		for j in range(M):
			tmp=[l for l in stdin.readline().strip()]
			T.append(tmp)
			for u in range(len(tmp)):
				if(tmp[u]=='A'): src=[j,u]
				elif(tmp[u]=='B'): end=[j,u]
				elif(tmp[u]=='Z'): H.append([j,u])
		ans=solve(T,src,end,H)
		if(ans==float('inf')): print("King Peter, you can't go now!")
		else: print("Minimal possible length of a trip is",ans)

main()

