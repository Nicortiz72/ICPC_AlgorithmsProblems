from collections import deque
def bfs(G,initial,x):
	queue = deque([initial])
	visited=[False for _ in range(len(G))]
	while len(queue)!=0:
		v=queue.popleft()
		visited[v]=True
		for i in G[v]:
			if(not visited[i]):
				queue.append(i)
	return visited[x]

def dfs(G,initial,x):
	stack=[initial]
	visited=[False for _ in range(len(G))]
	while len(stack)!=0:
		v=stack.pop()
		visited[v]=True
		for i in G[v]:
			if(not visited[i]):
				stack.append(i)
	return visited[x]

def knapsack(W,B,c):
	N=len(W)
	Tab=[[0 for _ in range(N+1)] for _ in range(c+1)]
	for cap in range(1,c+1):
		for n in range(1,N+1):
			if(W[n-1]<=cap):
				Tab[cap][n]=max(Tab[cap-W[n-1]][n-1]+B[n-1],Tab[cap][n-1])
			else:
				Tab[cap][n]=Tab[cap][n-1]
	return Tab[c][N]

def knapsackUnbounded(W,B,c):
	N=len(W)
	Tab=[[0 for _ in range(N+1)] for _ in range(c+1)]
	for cap in range(1,c+1):
		for n in range(1,N+1):
			if(W[n-1]<=cap):
				Tab[cap][n]=max(Tab[cap-W[n-1]][n]+B[n-1],Tab[cap][n-1])
			else:
				Tab[cap][n]=Tab[cap][n-1]
	return Tab[c][N]

def longestSubstring(s1,s2):
	N1=len(s1);N2=len(s2)
	Tab=[[0 for _ in range(N2+1)] for _ in range(N1+1)]
	maxim=0
	maximIndex=0
	for i in range(1,N1+1):
		for j in range(1,N2+1):
			if(s1[i-1]==s2[j-1]):
				Tab[i][j]=Tab[i-1][j-1]+1
				if(Tab[i][j]>maxim):
					maxim=Tab[i][j]
					maximIndex=j-1
	return s2[maximIndex-maxim+1:maximIndex+1]

def longestSubsecuence(s1,s2):
	N1=len(s1);N2=len(s2)
	Tab=[[0 for _ in range(N2+1)] for _ in range(N1+1)]
	maxim=0
	for i in range(1,N1+1):
		for j in range(1,N2+1):
			if(s1[i-1]==s2[j-1]):
				Tab[i][j]=Tab[i-1][j-1]+1
			Tab[i][j]=max(Tab[i][j],Tab[i-1][j],Tab[i][j-1])
	return Tab[N1][N2]

def helper(A,Memory,i,x):
	if((i,x) in Memory):
		return Memory[(i,x)]
	else:
		if(i==0): 
			ans = A[i]==x
		else:
			ans= helper(A,Memory,i-1,x-A[i]) or helper(A,Memory,i-1,x+A[i])
		Memory[(i,x)]=ans
		return ans
		
def EqualSubsetSum(A):
	Memory=dict()
	return helper(A,Memory,len(A)-1,0)
	

def SubsetSum(A,t):
	N=len(A)
	minimum=min(A)
	if(minimum<0):
		for i in range(N): A[i]-=minimum
	T=max(A)
	Tab=[[False for _ in range(N+1)] for _ in range(T+1)]
	for i in range(N+1):
		for targ in range(T+1):
			if(A[i-1]<=targ):
				Tab[targ][i]=Tab[targ][i-1] or Tab[targ-A[i-1]][i-1] or A[i-1]==targ
			else:
				Tab[targ][i]=Tab[targ][i-1]
	return Tab[t][N]


def taskScheduler(Tasks):
	Tasks.sort(key= lambda x: x[1])
	answer=0
	timeTmp=0
	for s,e in Tasks:
		if(timeTmp<=s):
			answer+=1
			timeTmp=e
	return answer


def merge(left,right):
	i=0;j=0
	ans=list()
	while i<len(left) or j < len(right):
		if(i==len(left)):
			ans.append(right[j])
			j+=1
		elif(j==len(right)):
			ans.append(left[i])
			i+=1
		elif(left[i]>right[j]):
			ans.append(right[j])
			j+=1
		else:
			ans.append(left[i])
			i+=1
	return ans

def mergeSort(S):
	if(len(S)==1): return S
	mid=(len(S))//2
	left=mergeSort(S[:mid])
	right=mergeSort(S[mid:])
	return merge(left,right)

def pivotPoint(A,i,j):
	pivot=i
	pivotVal=A[pivot]
	for k in range(i+1,j):
		if(pivotVal>A[k]):
			pivot+=1
			tmp=A[k]
			A[k]=A[pivot]
			A[pivot]=tmp
	tmp=A[i]
	A[i]=A[pivot]
	A[pivot]=tmp
	return pivot

def quickSort(A,i,j):
	if(i+1<j):
		pivot=pivotPoint(A,i,j)
		quickSort(A,i,pivot)
		quickSort(A,pivot+1,j)
	return A

def getDigit(n,i):
	num=str(n).replace("-","")
	if(i<len(num)):
		return int(num[len(num)-i-1])
	else:
		return 0

def concatArray(A,B):
	Ans=list()
	for i in A:
		for j in i:
			Ans.append(j)
	for i in B:
		for j in i:
			Ans.append(j)
	return Ans

def radixSort(A):
	maxDigits=len(str(max(A)))
	for i in range(maxDigits):
		positiveBuck=[[] for _ in range(10)]
		negativeBuck=[[] for _ in range(10)]
		for j in A:
			if(j>=0):
				positiveBuck[getDigit(j,i)].append(j)
			else:
				negativeBuck[getDigit(j,i)].append(j)
		A=concatArray(negativeBuck,positiveBuck)
		
	return A



def lengthOfLongestSubstring(s):
        maxim=0
        D=dict()
        ans=0
        rep=0
        for i,v in enumerate(s):
            if(v in D):
                rep=max(rep,D[v]+1)
            ans=max(ans,i-rep+1)
            D[v]=i
        return ans

def coinChange(S,m):
	N=len(S)
	Tab=[[float('INF') for _ in range(m+1)] for _ in range(N+1)]
	for i in range(N+1):
		Tab[i][0]=0
	for i in range(1,N+1):
		for j in range(m+1):
			if(j>=S[i-1]):
				Tab[i][j] = Tab[i][j-S[i-1]]+1
			Tab[i][j]=min(Tab[i-1][j],Tab[i][j])
	return Tab[N][m]

		


