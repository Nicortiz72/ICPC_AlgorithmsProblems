from sys import *

def solve(A,N):
	print(A)
	R=[]
	best=-float('inf')
	neg=0
	negl=list()
	pro=1
	flt=False
	for i in range(N):
		print(pro,R,negl)
		if(A[i]<=0):
			if(flt): R.append(pro)
			else: R.append(0)
			pro=1
			if(A[i]==0): 
				negl.append(neg)
				neg=0
				flt=False
			else: neg+=1;flt=True
			R.append(A[i])
		else:
			pro*=A[i];flt=True
	R.append(pro)
	negl.append(neg)
	print(pro,R,negl)
	z=0
	for i in negl:
		tmp=1;u=0;p=0
		if(i==1):
			if(R[z]==0): p=-2
			elif(R[z+2]==0): u=2
			else: u=1;p=-1
		elif(i%2!=0):
			if(-R[z]*R[z+1]>=-R[i*2]*R[(i*2)-1]): p=-2
			else: u=2
		for j in range(z+u,1+z+(i*2)+p):
			tmp*=R[j]
		z=2+z+(i*2)
		best=max(best,tmp)
		print(tmp,z)
	return best




def main():
	line=stdin.readline().strip()
	while line!="":
		A=[int(x) for x in line.split()]
		print(solve(A,len(A)-1))
		line=stdin.readline().strip()
main()