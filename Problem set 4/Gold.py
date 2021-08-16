from sys import *

AYx=[0,0,1,-1]
AYy=[1,-1,0,0]

def next(M,x,y):
	ans=[]
	flat=True
	i=0
	while(i<len(AYx) and flat):
		z1=x+AYx[i];z2=y+AYy[i]
		if(0<=z1<len(M) and 0<=z2<len(M[0]) and (M[z1][z2]=='.' or M[z1][z2]=='G' or M[z1][z2]=='T')):
			if(M[z1][z2]=='T'): ans=[];flat=False
			else:
				ans.append([z1,z2])
		i+=1
	return ans

def DFS(M,src):
	ans=0
	stack=[src]
	visited=[[0 for i in range(len(M[0]))] for j in range(len(M))]
	visited[src[0]][src[1]]=1
	while len(stack)!=0:
		u,v=stack.pop()
		for i,j in next(M,u,v):
			if(visited[i][j]==0):
				if(M[i][j]=='G'): ans+=1
				stack.append([i,j])
				visited[i][j]=1
	return ans

def main():
	line=stdin.readline().strip()
	while line!="":
		W,H=[int(x) for x in line.split()]
		M=[]
		for i in range(H):
			tmp=stdin.readline().strip()
			M.append(tmp)
			for j in range(len(tmp)):
				if(tmp[j]=='P'): src=[i,j]
		print(DFS(M,src))
		line=stdin.readline().strip()
main()