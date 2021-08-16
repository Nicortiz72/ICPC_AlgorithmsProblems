from sys import stdin

c=0
cont=0
def SCCUtil(G,u, low, disc, stackMember, st):
	global c,cont
	disc[u] = c
	low[u] = c
	c += 1
	stackMember[u] = True
	st.append(u)
	for v in G[u]:
		if disc[v] == -1 :
			SCCUtil(G,v, low, disc, stackMember, st)
			low[u] = min(low[u], low[v])    
		elif stackMember[v] == True: 
			low[u] = min(low[u], disc[v])
	w = -1 
	if low[u] == disc[u]:
		while w != u:
			w = st.pop()
			print(w,)
			stackMember[w] = False
		print("")
def solve(G,n):
	global c,cont
	c=0;cont=0
	low=[-1 for i in range(n)]
	disc=[-1 for i in range(n)]
	stackMember=[False for i in range(n)]
	st=[]
	SCCUtil(G,0,low,disc,stackMember,st)
	return cont


def main():
	n=int(stdin.readline())
	for i in range(n):
		if(i!=0): stdin.readline()
		n,m=[int(x) for x in stdin.readline().split()]
		G=[[] for j in range(n)]
		for j in range(m):
			x,y=[int(x) for x in stdin.readline().split()]
			G[x-1].append(y-1)
		print("Case",str(i+1)+":",solve(G,n))
main()