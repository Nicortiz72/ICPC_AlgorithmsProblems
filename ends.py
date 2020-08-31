from sys import *

M={}
#Nicolas Ortiz
#Competition training problem ends
#Memorization and DP
def dp(C):
	print(C)
	N=len(C)
	tab=[[0 for i in range(N+1)] for j in range(N+1)]
	for i in range(len(C)):
		if(i<len(C)): tab[i][i+1]=-C[i]
	n=N-2;m=N
	while n!=-1:
		if(m==N+1): n=n-1;m=n+2
		tmp=max(C[n],C[m-1])
		if(C[n]>=C[m-1]):
			tab[n][m]=max(C[n+1]+tab[n+2][m],C[m-1]+tab[n+1][m-1])-tmp
		else:
			tab[n][m]=max(C[n]+tab[n+1][m-1],C[m-2]+tab[n][m-2])-tmp
		m+=1
	ans=max(C[0]+tab[1][N],C[N-1]+tab[0][N-1])
	return ans

def phi(C,i,j):
	global M
	ans=M.get((i,j))
	if(ans==None):
		if(i==j): return -C[i]
		if(i>j): return 0
		tmp=max(C[i],C[j])
		if(C[i]==tmp):i+=1
		else: j-=1
		p=(max(C[i]+phi(C,i+1,j),C[j]+phi(C,i,j-1))-tmp)
		M[(i,j)]=p
		return p
	else:
		return ans

def solve(C):
	global M
	i=0;j=len(C)-1
	M={}
	return (max(C[i]+phi(C,i+1,j),C[j]+phi(C,i,j-1)))


def main():
	line=stdin.readline().strip()
	cont=1
	while line!="0":
		C=[int(x) for x in line.split()]
		print("In game {0}, the greedy strategy might lose by as many as {1} points.".format(cont,dp(C[1:])))
		line=stdin.readline().strip()
		cont+=1
main()
