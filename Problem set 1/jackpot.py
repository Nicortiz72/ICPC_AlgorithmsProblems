from sys import *

def solve(A):
	Q=[A[0]];mx=A[0]
	for i in range(1,len(A)):
		Q.append(max(A[i]+Q[i-1],A[i]))
		mx=max(mx,Q[i])
	if(mx>0): print("The maximum winning streak is {}.".format(mx))
	else: print("Losing streak.") 

def main():
	n=int(stdin.readline())
	while(n!=0):
		A=[int(x) for x in stdin.readline().split()]
		solve(A)
		n=int(stdin.readline())
main()
