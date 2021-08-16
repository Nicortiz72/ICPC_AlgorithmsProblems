from sys import *

def solve(A):
	N=len(A)
	tab=[[0 for i in range(N)] for j in range(N)]
	if(A[0]!=-1): tab[0][A[0]]=1
	else:
		for i in range(N): tab[0][i]=1
	n,s=1,0
	while n != N:
		if s==N: 
			n,s=n+1,0
		else:
			if(A[n]!=-1): 
				su=0
				for i in range(0,A[n]-1): su+= tab[n-1][i]
				for i in range(A[n]+2,N): su+= tab[n-1][i]
				tab[n][A[n]]=su
				n,s=n+1,0
			else:
				su=0
				for i in range(0,s-1): su+= tab[n-1][i]
				for i in range(s+2,N): su+= tab[n-1][i]
				tab[n][s]=su
				s+=1
	return sum(tab[N-1])



def main():
	line=stdin.readline().strip()
	while line != "":
		A=[]
		for i in line:
			if(ord('1')<=ord(i)<=ord('9')): A.append(int(i)-1)
			elif(ord(i)==ord('?')): A.append(-1)
			else: A.append(9+ord(i)-ord('A'))
		print(solve(A))
		line=stdin.readline().strip()
main()