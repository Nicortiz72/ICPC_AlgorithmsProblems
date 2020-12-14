from sys import stdin
import math

def bruteForce(P):
	mn=10000
	for i in range(len(P)):
		for j in range(i+1,len(P)):
			mn=min(mn,distance(P[i],P[j]))
	return mn

def distance(p1,p2):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def solve(P,low,high):
	if(low+3<high):
		mid=(low+high)>>1
		left=solve(P,low,mid)
		right= solve(P,mid,low)
		mn=min(left,right)
		possible=list()
		for i in range(low,high):
			if(abs(P[i][0]-P[mid][0])<mn):
				possible.append(P[i])
		possible.sort(key = lambda x: x[1])
		for i in range(len(possible)):
			for j in range(i+1,len(possible)):
				if(abs(P[i][1]-P[j][1])>=mn): break
				mn=min(mn,distance(P[i],P[j]))

	else:
		if(low+1==high): return 10000
		else: return bruteForce(P[low:high])
	return mn


def main():
	N=int(stdin.readline())
	while N!=0:
		P=list()
		for _ in range(N):
			x,y=[float(x) for x in stdin.readline().split(" ")]
			P.append((x,y))
		if(N<2): print("INFINITY")
		elif(N<=3): print("%.4f"%bruteForce(P))
		else:
			P.sort()
			ans=solve(P,0,len(P))
			if(ans>=10000): print("INFINITY")
			else: print("%.4f"%ans)
		N=int(stdin.readline())
main()
		
