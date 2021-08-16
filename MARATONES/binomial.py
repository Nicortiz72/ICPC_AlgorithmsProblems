import math
from sys import stdin

def binarySearch(k, c):
    n = 1
    while n ** k < c: n *= 2
    lo = n//2
    hi = n
    while lo + 1 < hi:
        mid = lo + ((hi - lo) // 2)
        if mid ** k < c:
            lo = mid
        else:
            hi = mid
    return hi

def Choose (n, k):
    k = min(k, n - k)
    ans = 1
    for i in range(k):
        ans *= n - i
        ans //= i + 1
    return ans

def find(x):
    ans=[]
    k = 1
    while ((2 * k) + 1) * x > 4**k:
        nd = binarySearch(k, math.factorial(k) * x)
        nu = nd + (k + 1)
        nd = max(nd, 2 * k)
        C = Choose(nd, k)
        for n in range(nd, nu):
            if C == x:
                ans.append((n, k))
                if k < n - k:
                    ans.append((n, n - k))
            C = (C*(n + 1))//(n + 1 - k)
        k += 1
    return ans

def main():
    n=int(stdin.readline())
    for i in range(n):
        a=int(stdin.readline())
        ans=find(a)
        ans.sort()
        print(len(ans))
        print("({0},{1})".format(ans[0][0],ans[0][1]),end="")
        for (n,k) in ans[1:]: print(" ({0},{1})".format(n,k),end="")
        print()
main()