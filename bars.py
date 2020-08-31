from sys import *
from sys import setrecursionlimit

#Nicolas Ortiz
#Competition uva problem bars
#Recursion

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
