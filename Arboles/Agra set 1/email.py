from sys import stdin
visited=None
vis=1
def dfs(E,v,Dis):
	global visited,vis
	stack=[v]
	q=v
	Dis[v]=-1
	visited[q]=vis
	cont=1
	while(visited[E[q]]!=vis):
		visited[E[q]]=vis
		cont+=1
		q=E[q]
		Dis[q]=-1
		stack.append(q)
	if(Dis[E[q]]==-1):
		q1=stack.pop()
		while(q1!=E[q]):
			Dis[q1]=cont
			q1=stack.pop()
		Dis[E[q]]=cont
	while(len(stack)!=0):
		q1=stack.pop()
		Dis[q1]=Dis[E[q1]]+1
	return Dis

def solve(E):
	global visited,vis
	Dis=[0 for i in range(len(E))]
	for i in range(len(E)):
		if(visited[i]!=vis):
			Dis=dfs(E,i,Dis)
	j=0
	for i in range(len(Dis)):
		if(Dis[j]<Dis[i]):
			j=i
	return j

#dfs
	

def main():
	global visited,vis
	n=int(stdin.readline())
	visited=[0 for i in range(50000)]
	for i in range(n):
		v=int(stdin.readline())
		E=[0 for i in range(v)]
		for j in range(v):
			q1,q2=stdin.readline().split()
			E[int(q1)-1]=int(q2)-1
		print('Case {0}: {1}'.format(i+1, solve(E)+1))
		vis+=1

main()
