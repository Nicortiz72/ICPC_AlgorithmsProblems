from sys import *

def maxarr(A):
	tab=[0 for i in range(len(A)+1)]
	tab[1]=A[0]
	for n in range(2,len(A)+1):
		tab[n]=max(tab[n-2]+A[n-1],tab[n-1])
	return tab[len(A)]


def solve(M):
	Mx=list()
	for i in M:
		Mx.append(maxarr(i))
	return maxarr(Mx)


def main():
	line=stdin.readline().split()
	while line[0]!="0":
		m,n=[int(x) for x in line]
		M=list()
		for i in range(m):
			M.append([int(x) for x in stdin.readline().split()])
		print(solve(M))
		line=stdin.readline().split()
main()