from sys import stdin
import time

def recursiveSolution(n,d):
	if(n==1): 
		result=d
	else:
		result=0
		for k in range(1,d+1): result+=1+recursiveSolution(n-1,k-1)
	return result

def DPSolution(N,D):
	Tab=[[i for i in range(D+1)] for _ in range(N+1)]
	for n in range(2,N+1):
		for d in range(1,D+1):
			Tab[n][d]=Tab[n][d-1]+Tab[n-1][d-1]+1
	return Tab[N][D]

def main():
	n,d=[int(x) for x in stdin.readline().split()]

	print("\nDP solution:")
	currentTime = time.time()
	print(DPSolution(n,d))
	print("Time:",time.time() - currentTime)
	print("----------------------------------\nRecursive solution:")
	currentTime = time.time()
	print(recursiveSolution(n,d))
	print("Time:",time.time() - currentTime)

	
main()

