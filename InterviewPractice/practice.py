def merge_sorted(head1, head2):
  ans=list()
  i,j=0,0
  while(i<len(head1) or j<len(head2)):
    if(i==len(head1)): ans.append(head2[j]);j+=1
    elif(j==len(head2)): ans.append(head1[i]);i+=1
    elif(head1[i]>=head2[j]): ans.append(head2[j]); j+=1
    else: ans.append(head1[i]); i+=1
  return ans

def merge_sorted(head1, head2):  #linked list
  if(head1==None): return head2
  elif(head2==None): return head1
  if(head1.data > head2.data):
    start=head2
    head2=head2.next
  else:
    start=head1
    head1=head1.next
  iterate=start
  while(head1!=None or head2!=None):
    if(head1==None): 
      iterate.next=head2
      iterate=head2
      head2=head2.next
    elif(head2==None): 
      iterate.next=head1
      iterate=head1
      head1=head1.next
    elif(head1.data<=head2.data):
      iterate.next=head1
      iterate=head1
      head1=head1.next
    else:
      iterate.next=head2
      iterate=head2
      head2=head2.next
  return start


#Verify search trees
def helper(root,mx):
  ans=True
  if(root.left!=None):
    ans = root.left.data < root.data and  helper(root.left,root.data)
  if(root.right!=None):
    ans = ans and root.right.data > root.data and root.right.data < mx and  helper(root.right,mx)
  return ans
def is_bst(root):
  if(root==None): return True
  return helper(root,float('INF'))


#segmentation
def helper(s,dictionary,i,j):
  if(j>=len(s)): return s[i:j] in dictionary
  if(s[i:j] in dictionary):
    return helper(s,dictionary,j,j+1) or helper(s,dictionary,i,j+1)
  else:
    return helper(s,dictionary,i,j+1)
def can_segment_string(s, dictionary):
  return helper(s,dictionary,0,1)


 def solve_coin_change(denominations, amount):
  solution = [0] * (amount + 1)
  solution[0] = 1;
  for den in denominations:
    for i in range(den, amount + 1):
      solution[i] += solution[i - den] 

  return solution[len(solution) - 1]


  def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n -1 )

def find_kth_permutation(v, k, result):
  if not v:
    return
  
  n = len(v)
  # count is number of permutations starting with first digit
  count = factorial(n - 1)
  selected = (k - 1) // count
  
  result += str(v[selected])
  del v[selected]
  k = k - (count * selected)
  find_kth_permutation(v, k, result)


  #clone graph
class Node:
  def __init__(self, d):
    self.data = d
    self.neighbors = []

def helper(root,new,D):
  for i in root.neighbors:
    if(i in D):
      new.neighbors.append(D[i])
    else:
      newNode=Node(i.data)
      D[i]=newNode
      new.neighbors.append(newNode)
      helper(i,newNode,D)

def clone(root):
  if(root==None): return None
  newRoot=Node(root.data)
  D=dict()
  D[root]=newRoot
  helper(root,newRoot,D)
  return newRoot    # return root




 #reversed array search
 def find_initial(arr,x):
  lw=0
  hi=len(arr)
  while lw+1!=hi:
    mid=(lw+hi)//2
    if(arr[mid]>x):
      lw=mid
    else:
      hi=mid
  return hi

def binary_search_rotated(arr, key):
  start=0
  if(arr[0]>arr[-1]):
    start=find_initial(arr,arr[0])
  lw=start
  N=len(arr)
  hi=(N+start)
  while (lw+1)%N!=hi%N:
    mid=(lw+hi)//2
    if(arr[mid%N]==key):
      return mid%N
    elif(arr[mid%N]>key):
      hi=mid
    else:
      lw=mid
  return -1


def rotateRight(head: ListNode, k: int) -> ListNode:
    iterate=head
    lenght=0
    while iterate!=None:
        lenght+=1
        iterate=iterate.next
    k=k%lenght
    iterate=head

    for _ in range(lenght-k-1): 
    	iterate=iterate.next

    tmp=iterate
    iterate=iterate.next
    tmp.next=None
    rotateList=iterate
    while iterate.next!=None: 
    	iterate=iterate.next
    iterate.next=head

    return rotateList

def countBits(n):
	count=0
	for _ in range(32):
		if(n%2==1): count+=1
		n=n>>1
	return count

def findZeroSubArray(A):
	out=[]
	D=dict()
	sumi=0
	for i,v in enumerate(A):
		sumi+=v
		if(sumi==0):
			out.append((0,i))
		if(sumi in D):
			for j in D[sumi]:
				out.append((j+1,i))
			D[sumi].append(i)
		else:
			D[sumi]=[i]
	return out


def JosephusProblem(n,k):
	if(n==1): return 1
	return (JosephusProblem(n-1,k)+k-1)%(n+1)

def DecodeHuffman(root,code):
	out=""
	iterate=root
	for i in code:
		if(iterate.data!=None):
			out+=iterate.data
			iterate=root
		elif(i==0): 
			iterate=iterate.left
		else:
			iterate=iterate.right
	return out


def helper(A1,A2,D,i,j):
	if(i>=len(A1) or j>=len(A2)): return 0
	else:
		if A1[i]==A2[j]:
			ans=1
		if((i+1,j) in D):
			ansi=D[(i+1,j)]
		else:
			ansi=helper(A1,A2,D,i+1,j)
			D[(i+1,j)]=ansi
		if((i,j+1) in D):
			ansj=D[(i,j+1)]
		else:
			ansj=helper(A1,A2,D,i,j+1)
			D[(i,j+1)]=ansj

		ans+=max(ansi,ansj)
		return ans
def LongestCommonSubsequence(A1,A2):
	return helper(A1,A2,dict(),0,0)


def longestIncreasingSubsequence(A):
	prev=0
	maxim=-float('INF')
	for i in A:
		prev=max(prev+i,i)
		maxim=max(maxim,prev)
	return maxim


class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def helper(root,lw,hi):
	if(root==a or root==b): return root
	if(root.data < hi and root.data > lw): return root
	if(root.data < hi): return helper(root.right,lw,hi)
	else: return helper(root.left,lw,hi)

def lowestCommonAncestorBST(root,a,b):
	if(a==b): return a
	if(a.data>b.data):
		highest = a
		lowest = b
	else:
		lowest = a
		highest = b
	return helper(root,lowest,highest)

def lowestCommonAncestorBT(root,a,b):
	if(root==None): return None
	if(root==a or root==b): return root

	left_lca=lowestCommonAncestorBT(root.left,a,b)
	right_lca=lowestCommonAncestorBT(root.right,a,b)

	if(left_lca !=None and right_lca!=None): 
		return root
	elif(left_lca==None):
		return right_lca
	else:
		return left_lca

def findPath( root, path, k):
 
    # Baes Case
    if root is None:
        return False
 
    # Store this node is path vector. The node will be
    # removed if not in path from root to k
    path.append(root.data)
 
    # See if the k is same as root's key
    if root.data == k :
        return True
 
    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))):
        return True
 
    # If not present in subtree rooted with root, remove
    # root from path and return False
      
    path.pop()
    return False

def eggDrop(n, k): 
    # A 2D table where entery eggFloor[i][j] will represent minimum 
    # number of trials needed for i eggs and j floors. 
    eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)] 
  
    # We need one trial for one floor and0 trials for 0 floors 
    for i in range(1, n + 1): 
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
  
    # We always need j trials for one egg and j floors. 
    for j in range(1, k + 1): 
        eggFloor[1][j] = j 
  
    # Fill rest of the entries in table using optimal substructure 
    # property 
    for i in range(2, n + 1): 
        for j in range(2, k + 1): 
            eggFloor[i][j] = float("INF") 
            for x in range(1, j + 1): 
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]) 
                if res < eggFloor[i][j]: 
                    eggFloor[i][j] = res 
  
    # eggFloor[n][k] holds the result 
    return eggFloor[n][k]

def LPS(s2,N2):
	lps=[0]*N2
	lenght=0
	i=1
	while i<N2:
		if(s2[i]==s2[lenght]):
			lenght+=1
			lps[i]=lenght
			i+=1
		elif(lenght!=0):
			lenght=lps[lenght-1]
		else:
			i+=1
	return lps

 def rotationString(s1,s2):
 	s1=s1+s1
 	N1=len(s1);N2=len(s2)
 	if (N1//2!=N2): return False
 	lps=LPS(s2,N2)
 	i=0;j=0
 	while i < N1 and j<N2:
 		if(s1[i]==s2[j]):
 			i+=1
 			j+=1
 			if(j==N2): return True
 		elif(j!=0):
 			j=lps[j]
 		else:
 			i+=1
 	return False

https://www.educative.io/blog/6-dp-problems-to-solve-for-your-next-coding-interview
https://www.educative.io/blog/crack-amazon-coding-interview-questions