from sys import *

def isPossible(Cost,P,mid):
	count=0
	for i in Cost:
		count+=i
		if(count>mid):
			if(P>0):
				P-=1
				count=i
			else:
				return False
	return True
#Binary search
def solve(Cost,P):
	high=sum(Cost)
	low=max(Cost)
	while low+1!=high:
		mid=(low+high)>>1
		if(isPossible(Cost,P,mid)):
			high=mid
		else:
			low=mid
	return low if isPossible(Cost,P,low) else high




def main():
	line=stdin.readline().strip()
	while line!="":
		N,P=[int(x) for x in line.split(" ")]
		Cost=[]
		for i in range(N+1):
			Cost.append(int(stdin.readline()))
		print(solve(Cost,P))
		line=stdin.readline().strip()
main()
