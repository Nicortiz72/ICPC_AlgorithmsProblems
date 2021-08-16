from sys import stdin
visited=None
vis=1

def dfs(G,n,v,rec):
	global visited,vis
	ans=1
	stack=[v]
	visited[v]=vis
	while(len(stack)!=0):
		u=stack.pop()
		for i in G[u]:
			if(visited[i]!=vis):
				stack.append(i)
				visited[u]=1
			else:
				if(rec[i]): ans=0
	return ans

def solve(G,n):
	global visited,vis
	rec=[0 for i in range(n)]
	cont=0
	for i in range(n):
		if(visited[i]!=vis):
			rec[i]=1
			cont+=dfs(G,n,i,rec)
	return cont

def main():
	global visited,vis
	n=int(stdin.readline())
	visited=[0 for i in range(100000)]
	for i in range(n):
		n,m=[int(x) for x in stdin.readline().split()]
		G=[[] for u in range(n)]
		for j in range(m):
			x,y=[int(o) for o in stdin.readline().split()]
			G[x-1].append(y-1)
		print(solve(G,n))
		vis+=1
main()