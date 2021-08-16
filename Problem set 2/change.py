from sys import *

a=[5,10,20,50,100,200]

auxt=[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]

INF=float('inf')
def cc_tab(C, P):
	N = len(a)
	S=P+200
	tab = [ [ INF for s in range(S+1) ] for n in range(N+1) ]
	for n in range(N+1): tab[n][0] = 0
	n,s = 1,0
	while n!=N+1:
		if s==S+1: n,s = n+1,0
		else:
			tab[n][s] = tab[n-1][s]
			if a[n-1]<=s and C[n-1]>0:
				tmp=min(s//a[n-1],C[n-1]) 
				tab[n][s] = min(tmp+tab[n-1][s-(a[n-1]*tmp)],tab[n][s])
			s += 1
	ans=float('inf')
	for i in range(P,S+1):
		ans=min(ans,tab[N][i]+auxt[i-P])
	return ans

def main():
	line=stdin.readline().strip()
	while line!="0 0 0 0 0 0":
		num=[float(x) for x in line.split()]
		e=int(num[6]*100)
		A=[int(num[x]) for x in range(len(num)-1)]
		n=cc_tab(A,e)
		if(n>=100): print(n)
		elif(n>=10): print(" "+str(n))
		else: print(" ",n)
		line=stdin.readline().strip()
main()