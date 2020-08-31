from sys import *

#Nicolas Ortiz
#Competition problem
#Binary search
def solve(de,X,A,q):
	lo=0;hi=len(A)
	for i in X:
		mid=(lo+hi)>>1
		if(q[i]=='0'): hi=mid
		else: lo=mid
	return A[lo]

def main():
	line=(stdin.readline().strip())
	cont=1
	flt=False
	while line!="0":
		flt=True
		de=int(line)
		tmp=stdin.readline().split()
		X=list()
		for i in tmp: X.append(int(i[1])-1)
		A=[str(x) for x in stdin.readline().strip()]
		m=int(stdin.readline())
		ans=list()
		for i in range(m): 
			ans.append(solve(de,X,A,stdin.readline().strip()))
		print("S-Tree #{}".format(cont))
		cont+=1
		print("".join(str(i) for i in ans))
		line=(stdin.readline().strip())
		print("")
main()


