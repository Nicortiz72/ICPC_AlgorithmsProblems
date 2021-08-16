from sys import *

def main():
	n=int(stdin.readline())
	S=[]
	for _ in range(n):
		line=stdin.readline().split()
		if(line[0]=="Sleep"): S.append(line[1])
		elif(line[0]=="Kick"): 
			if(len(S)!=0): S.pop()
		else: 
			if(len(S)!=0): print(S[-1])
			else: print("Not in a dream")
main()