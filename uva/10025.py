from sys import *

Sumatory=[]
n=0
i=1
while n<=1000000000:
	Sumatory.append(n)
	n+=i;i+=1

def binarySearch(k):
	low=0;high=len(Sumatory)
	while low+1!=high:
		mid=(low+high)>>1
		if(Sumatory[mid]==k): return mid
		elif(Sumatory[mid]>k): high=mid
		else: low=mid
	return high 

def solve(k):
	n=binarySearch(k)
	while Sumatory[n]%2 != k%2: n+=1
	return n

def main():
	T=int(stdin.readline())
	for i in range(T):
		stdin.readline()
		k=int(stdin.readline())
		if(i!=0): print()
		print(solve(k if k>0 else -k))
main()