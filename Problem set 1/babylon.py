from sys import *

def per(B):
	A=[[B[0],B[1],B[2]],[B[0],B[2],B[1]],
	  [B[1],B[0],B[2]],[B[1],B[2],B[0]],
	  [B[2],B[0],B[1]],[B[2],B[1],B[0]]]
	return A
def can(A,B):
	return A[0]<B[0] and A[1] < B[1] 

def solve(A):
	if(len(A)!=0):
		A.sort(reverse=True)
		Q=[0 for i in range(len(A))]
		Q[0]=A[0][2]
		for i in range(1,len(Q)):
			mx=A[i][2]
			for j in range(1,i): 
				if(can(A[i],A[j])): mx= max(mx,Q[j]+A[i][2])
			Q[i]=mx
		return max(Q)
	else: return 0


def main():
	n=int(stdin.readline())
	cont=1
	while(n!=0):
		A=[]
		for i in range(n):
			B=per([int(x) for x in stdin.readline().split()])
			for j in B: A.append(j)
		v=solve(A)
		print("Case {0}: maximum height = {1}".format(cont,v))
		n=int(stdin.readline())
		cont+=1
main()

