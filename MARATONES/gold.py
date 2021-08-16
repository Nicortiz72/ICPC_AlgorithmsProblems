from sys import *

CX=[-1,0,1,0]
CY=[0,1,0,-1]

def next(A,u):
	flt=1
	ans=[]
	for i in range(4):
		z1=u[0]+CX[i];z2=u[1]+CY[i]
		if(0<=z1<len(A) and 0<=z2<len(A[0])):
			if(A[z1][z2]=='.' or A[z1][z2]=='G'):
				ans.append([z1,z2])
			elif(A[z1][z2]=='T'): flt=0
	if(flt): return ans
	else: return []



def solve(A,P):
	stack=[P]
	visited=[[0 for i in range(len(A[0]))] for j in range(len(A))]
	cont=0
	visited[P[0]][P[1]]=1
	while(len(stack)!=0):
		u=stack.pop()
		for i in next(A,u):
			if(visited[i[0]][i[1]]==0):
				stack.append(i)
				visited[i[0]][i[1]]=1
				if(A[i[0]][i[1]]=='G'):cont+=1
	return cont


def main():
	line=stdin.readline().strip()
	while line !="":
		n,m=[int(x) for x in line.split()]
		A=[]
		for i in range(m): 
			tmp=stdin.readline().strip()
			A.append(tmp)
			for j in range(len(tmp)):
				if(tmp[j]=='P'):
					P=[i,j]
		print(solve(A,P))
		line=stdin.readline().strip()
main()
