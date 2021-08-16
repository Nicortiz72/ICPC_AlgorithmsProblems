from sys import *

ans=None
Or=None
def solve(line,i):
	global ans
	if(i==len(Or)): ans.append(line)
	else:
		for j in range(i+1):
			tmp1=line[:j]
			tmp2=line[j:]
			solve(tmp1+Or[i]+tmp2,i+1)

def main():
	global ans,Or
	line=stdin.readline().strip()
	while line!="":
		ans=list()
		Or=line
		solve("",0)
		for i in ans: print(i)
		line=stdin.readline().strip()
		if(line!=""): print()
main()