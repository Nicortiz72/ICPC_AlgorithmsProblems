from sys import stdin

def solve(A,x):
	low,hi=0,len(A)
	while low+1 != hi:
		mid=(hi+low)//2
		if A[mid]>=x:
			hi=mid
		else: 
			low=mid
	if(A[0]==x): print("{0} found at {1}".format(x,1))
	elif(hi< len(A) and A[hi]==x): print("{0} found at {1}".format(x,hi+1))
	else:	print("{} not found".format(x))

def main():
	m,n=[int(x) for x in stdin.readline().split()]
	count=1
	while m + n != 0:
		print("CASE# {0}:".format(count))
		A=[]
		for i in range(m): A.append(int(stdin.readline()))
		A.sort()
		for i in range(n): solve(A,int(stdin.readline()))
		count+=1
		m,n=[int(x) for x in stdin.readline().split()]
main()

