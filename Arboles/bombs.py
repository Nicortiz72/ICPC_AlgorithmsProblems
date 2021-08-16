import sys

from sys import stdin
from sys import stdout
from sys import setrecursionlimit

MAX_N = 10000 + 1
N = 0
G = [list() for x in range(MAX_N)]

# Componentes que quedan al quitar i del grafo
COMPS = [0 for i in range(MAX_N)]
DEEP = [0 for i in range(MAX_N)]
LOW = [0 for i in range(MAX_N)]
PARENT = [0 for i in range(MAX_N)]

def dfs(u, d):
	global N, G, COMPS, DEEP, LOW, PARENT
	DEEP[u] = LOW[u] = d
	for v in G[u]:
		if DEEP[v] == -1:
			PARENT[v] = u
			dfs(v, d + 1)
			if LOW[v] >= DEEP[u]:
				COMPS[u] += 1

			LOW[u] = min(LOW[u], LOW[v])

			## if (low[hijo] > deep[u]) => Puente(u, hijo) 
            ## if (low[hijo] >= deep[u] and tienePapa) => artPoint(u)
		elif PARENT[u] != v:
			LOW[u] = min(DEEP[v], LOW[u])

def main():
	global N, G, COMPS, DEEP, LOW, PARENT
	setrecursionlimit(5000)
	initial = True
	while True:
		N, M = [int(x) for x in stdin.readline().split()]

		
		if N == M and N == 0:
			break

		if not initial:
			stdout.write("\n")

		initial = False
		for i in range(N):
			G[i] = list()
			COMPS[i] = 1;
			DEEP[i] = -1
			LOW[i] = 0

		while True:
			x, y = [int(w) for w in stdin.readline().split()]
			if x == y and x == -1:
				break

			G[x].append(y)
			G[y].append(x)

		# Count articulation points
		for i in range(N):
			if DEEP[i] != -1:
				continue

			dfs(i, 0)

			# Esto cubre el caso de quitarle 1 al root de las diapositivas
			COMPS[i] -= 1

		ans = list()
		for i in range(N):
			ans.append((i, COMPS[i]))

		ans = sorted(sorted(ans, key = lambda x : x[0]), key = lambda x : x[1], reverse = True)  
		for i in range(M):
			stdout.write(str(ans[i][0]) + " " + str(ans[i][1]) + "\n")

main()