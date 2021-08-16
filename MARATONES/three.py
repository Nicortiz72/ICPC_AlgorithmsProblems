from sys import *

def main():
	n=int(stdin.readline())
	while n!=0:
		l=list(bin(n-1))
		ansl=[]
		p=0
		for j in range(len(l)-1,1,-1):
			if(l[j]=='1'):
				ansl.append(str(3**p))
			p+=1
		if(len(ansl)!=0):
			print("{ ",end="")
			print(", ".join(ansl),end="")
			print(" }")
		else: print("{ }")
		n=int(stdin.readline())
main()



