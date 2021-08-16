from sys import stdin

visited=None
vis=1
def toposort(G):
  ans = list()
  indeg = [ 0 for _ in range(len(G)) ]
  for u in range(len(G)):
    for v in G[u]:
      indeg[v] += 1
  pending = list()
  for u in range(len(G)):
    if indeg[u]==0:
      pending.append(u)
  while len(pending)!=0:
    u = pending.pop()
    ans.append(u)
    for v in G[u]:
      indeg[v] -= 1
      if indeg[v]==0:
        pending.append(v)
  return len(ans)

def dfs(G,n,p):
	global visited,vis
	ans=[False for i in range(len(G[p]))]
	vitmp=[0 for i in range(n)]
	for i in range(len(G[p])):
		stack=[G[p][i]]
		ans[i]=vitmp[G[p][i]]==1
		vitmp[G[p][i]]=1
		while(len(stack)!=0 and not(ans[i])):
			v=stack.pop()
			vitmp[v]=1
			for j in G[v]:
				if(vitmp[j]==0):
					stack.append(j)
				else:
					ans[i]=True
	return all(ans[1:])

def solve(G,n):
	global visited,vis
	ans=True
	if(toposort(G)==0): ans=False
	else:
		stack=[0]
		while(len(stack)!=0 and ans):
			p=stack.pop()
			visited[p]=vis
			if(len(G[p])>=2): ans=dfs(G,n,p)
			for i in G[p]:
				if(visited[i]!=vis):
					stack.append(i)
	vis+=1
	if(ans): return 1
	else: return 0



def main():
	global visited,vis
	n,m=[int(x) for x in stdin.readline().split()]
	visited=[0 for i in range(1000)]
	while(n+m!=0):
		G=[[] for j in range(n)]
		for j in range(m):
			x,y=[int(x) for x in stdin.readline().split()]
			G[x].append(y)
		print(solve(G,n))
		n,m=[int(x) for x in stdin.readline().split()]

main()