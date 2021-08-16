from sys import *

def solve(G,s):
	visited=[0 for i in range(len(G))]
	stack=[s]
	while len(stack)!=0:
		u=stack.pop()
		for i in G[u]:
			if(visited[i]==0):
				visited[i]=1
				stack.append(i)
	ans=[]
	for i in range(len(visited)):
		if(visited[i]==0): ans.append(i)
	return ans

def main():
	n=int(stdin.readline())
	while n!=0:
		G=[[] for i in range(n)]
		line=stdin.readline().strip()
		while line!="0":
			line=line.split()
			for i in range(1,len(line)-1): G[int(line[0])-1].append(int(line[i])-1)
			line=stdin.readline().strip()
		line=[int(x) for x in stdin.readline().split()]
		for i in line[1:]:
			ans=solve(G,i-1)
			print(len(ans),end="")
			for j in ans: print("",j+1,end="")
			print()
		n=int(stdin.readline())
main()