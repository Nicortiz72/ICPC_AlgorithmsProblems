from sys import *
#Nicolas Ortiz
#Uva problem 12146

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
	#input
	line=stdin.readline().split()
	while line[0]!="0":
		m,n=[int(x) for x in line]
		M=list()
		for i in range(m):
			M.append([int(x) for x in stdin.readline().split()])
		print(solve(M))
		line=stdin.readline().split()
main()

# Sample Input
# 5 5
# 1 8 2 1 9
# 1 7 3 5 2
# 1 2 10 3 10
# 8 4 7 9 1
# 7 1 3 1 6
# 4 4
# 10 1 1 10
# 1 1 1 1
# 1 1 1 1
# 10 1 1 10
# 2 4
# 9 10 2 7
# 5 1 1 5
# 0 0
# Sample Output
# 54
# 40
# 17