from sys import *
import math

def solve(a):
	ans=0
	if(len(a)>0):
		a.sort()
		ans=1
		low=a[0][1]
		for i in range(1,len(a)):
			if(a[i][0]>low):
				ans+=1;low=a[i][1]
			else: low=min(low,a[i][1])
	return ans

def main():
	line=stdin.readline().strip()
	count=1
	while line!="0 0":
		N,D=[int(x) for x in line.split()]
		a=[]
		D2=D**2
		flt=True
		for i in range(N):
			x,y=[int(u) for u in stdin.readline().split()]
			if(y>D):flt=False
			else: z=math.sqrt((D2 - (y**2)))
			a.append((x-z,x+z))
		#if(count==31): print(a)
		if(flt): ans=solve(a)
		else: ans=-1
		print("Case {0}: {1}".format(count,ans))
		stdin.readline()
		line=stdin.readline().strip()
		count+=1
main()
