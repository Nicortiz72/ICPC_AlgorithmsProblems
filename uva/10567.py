from sys import stdin

def encode(s):
	ans=[]
	prev=None
	for i,v in enumerate(s):
		if(prev==None):
			prev=v
			count=1
		elif(prev!=v):
			ans.append((prev,count))
			prev=v
			count=1
		else: count+=1
	if(prev!=None):
		ans.append((prev,count))
	return ans

def solve(S,Q):
	ans1=None
	ans2=None
	i=0
	j=0
	count=0
	while (i<len(S) and j<len(Q)):
		if(S[i][0]==Q[j][0] and S[i][1]>=Q[j][1]):
			if(ans1==None):
				if(i==0): ans1=0
				else: ans1=count
			ans2=count+Q[j][1]-1
			j+=1
		count+=S[i][1]
		i+=1
		
	return (None,None) if j!=len(Q) else (ans1,ans2)

def main():
	S=encode(stdin.readline().strip())
	q=int(stdin.readline())
	for _ in range(q):
		Q=(encode(stdin.readline().strip()))
		ans1,ans2=solve(S,Q)
		if(ans2==None): print("Not matched")
		else: print("Matched",ans1,ans2)

main()