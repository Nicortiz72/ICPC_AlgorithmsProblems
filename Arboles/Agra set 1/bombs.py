from sys import stdin
from sys import setrecursionlimit

COMPS = None
DEEP = None
LOW = None


def dfs(G,v, u):
	global COMPS, DEEP, LOW
	DEEP[v] = LOW[v] = u
	for t in G[v]:
		if DEEP[t] == -1:
			dfs(G,t, u + 1)
			if LOW[t] >= DEEP[v]:
				COMPS[v] += 1
			LOW[v] = min(LOW[v], LOW[t])
		else:
			LOW[v] = min(DEEP[t], LOW[v])
	return G


def solve(G,n):
	global COMPS, DEEP, LOW
	COMPS = [1 for i in range(n)]
	DEEP = [-1 for i in range(n)]
	LOW = [0 for i in range(n)]
	for i in range(n):
		if DEEP[i] == -1:
			dfs(G,i, 0)
			COMPS[i] -= 1
	ans = []
	for i in range(n):
		ans.append([i, COMPS[i]])
	return ans


def main():
	setrecursionlimit(10000)
	n,m=[int(i) for i in stdin.readline().split()]
	first=False
	while(n+m!=0):
		G=[[] for i in range(n)]
		x,y=[int(i) for i in stdin.readline().split()]
		while(x!=-1 or y!=-1):
			G[x].append(y)
			G[y].append(x)
			x,y=[int(i) for i in stdin.readline().split()]
		if(first): print()
		ans=solve(G,n)
		ans = sorted(sorted(ans, key = lambda x : x[0]), key = lambda x : x[1], reverse = True)
		for i in range(m):
			print(ans[i][0],ans[i][1])
		first=True
		n,m=[int(i) for i in stdin.readline().split()]
main()
