from sys import stdin
import sys
sys.setrecursionlimit(1000000000)

def phi(nums, k, ac, mod, N, memo):
	if(mod == 0 and N == 0): return 1
	elif(N == 0 and mod != 0): return 0
	elif(memo[mod][N] == -1):
		newVal1, newVal2 = ac + nums[N-1], ac - nums[N-1]
		memo[mod][N] = int(phi(nums, k, newVal1, newVal1%k, N-1, memo) or phi(nums, k, newVal2, newVal2%k, N-1, memo))

	return memo[mod][N]



def main():
	cases = int(stdin.readline())
	for case in range(cases):
		N, k = list(map(int, stdin.readline().split()))
		nums = list(map(int, stdin.readline().split()))

		memo = [[-1 for _ in range(N+1)] for _ in range(k+1)]

		if(phi(nums, k, 0, 0, N, memo)): print("Divisible")
		else: print("Not divisible")



main()