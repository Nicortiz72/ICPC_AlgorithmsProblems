from sys import *

def solve(Nums,x):
	low=-1
	high=len(Nums)-1
	while low+1!=high:
		mid=(low+high)>>1
		if(Nums[mid]>=x): high=mid
		else: low=mid
	return high if Nums[high]==x else None


def main():
	N,Q=[int(x) for x in stdin.readline().split(" ")]
	case=1
	while N+Q!=0:
		Nums=list()
		for _ in range(N):
			Nums.append(int(stdin.readline()))
		Nums.sort()
		print("CASE# {0}:".format(case))
		for _ in range(Q):
			q=int(stdin.readline())
			ans=solve(Nums,q)
			if(ans==None):
				print("{0} not found".format(q))
			else:
				print("{0} found at {1}".format(q,ans+1))
		N,Q=[int(x) for x in stdin.readline().split(" ")]
		case+=1
main()