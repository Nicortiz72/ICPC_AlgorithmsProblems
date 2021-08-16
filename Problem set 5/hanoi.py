from sys import *
import math

Mem=[-1 for i in range(51)]

def main():
	T=int(stdin.readline())
	for _ in range(T):
		n=int(stdin.readline())
		if(Mem[n]==-1):
			i=1;ok=True
			board=[0 for i in range(n)]
			while ok:
				flt=True
				for e in range(len(board)):
					if(board[e]==0): 
						flt=False
						board[e]=i
						break
					t=math.sqrt(i+board[e])
					if(int(t)==t):
						flt=False
						board[e]=i
						break
				if(flt): ok=False
				i+=1
			Mem[n]=i-2
			print(i-2)
		else:
			print(Mem[n])
main()
