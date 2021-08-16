from sys import *

def mic(L,H,a):
	ans,low,n,N = 0,L,0,len(a)
	while low<H and n!=N:
		best,n = n,n+1
		while n!=N and a[n][0]<=low:
			if a[n][1]>a[best][1]:
				best = n
			n += 1
		ans+=1
		low = a[best][1]
	return ans

def main():
	line=stdin.readline().strip()
	while line!="0 0":
		L,G=[int(x) for x in line.split()]
		a=[]
		for i in range(G):
			x,r=[int(y) for y in stdin.readline().split()]
			a.append((x-r,x+r))
		a.sort()
		low=0;flat=True
		for i in a:
			if(i[0]>low): flat=False
			low=max(low,i[1])
		if(flat and low>=L): ans=mic(0,L,a)
		else: ans=-1
		print(G-ans if ans!=-1 else -1)
		line=stdin.readline().strip()
main()
