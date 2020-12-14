from sys import *

def solve(G,p,degree):
	nodesp=[]
	nodesp2=0
	for i in range(len(G)):
		if(degree[i]>2): nodesp2+=1
		elif(degree[i]==2): nodesp.append(i)
	for i in range(len(nodesp)):
		for j in range(i+1, len(nodesp)):
			if(G[i][j]==0):
				nodesp2+=1
	return nodesp2





