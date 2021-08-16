from sys import *
from sys import setrecursionlimit

# MAX_V = 1000 + 5
# MAX_P = 20 + 5

# def solveD(n,p,B):
# 	global MAX_V
# 	tab=[[0 for i in range(MAX_V)] for j in range(MAX_P)]
# 	for i in range(MAX_V):
# 		if i == 0:
# 			tab[p][i] = True
# 		else:
# 			tab[p][i] = False

# 	for i in range(p - 1, -1, -1):
# 		for j in range(0, n):
# 			if j - B[i] < 0:
# 				tab[i][j]=tab[i + 1][(j)]
# 				continue
# 			tab[i][j] = tab[i + 1][j - B[i]] or tab[i + 1][(j)]

# 	return tab[0][p]

def solve(i, v):
	global P, B,M
	if(M.get((i,v))==None):
		if i == P or v==0:
			M[(i,v)]=v==0
			return v == 0
		if(v-B[i]>=0): 
			ans=solve(i + 1, v - B[i]) or solve(i + 1, v)
		else:
			ans=solve(i + 1, v)
		M[(i,v)]=ans
		return ans
	else:
		return M[(i,v)]

def main():
	setrecursionlimit(500000000)
	global P, B,M
	t=int(stdin.readline())
	for _ in range(t):
		M={}
		n=int(stdin.readline())
		p=int(stdin.readline())
		P = p
		B=[int(x) for x in stdin.readline().split()]
		if(solve(0, n)):
			print("YES")
		else:
			print("NO")
main()
