from sys import *

def match(p):
	m=[-1 for i in p]
	i=1
	if(len(m)!=1): m[1]=0;i+=1
	while(i<len(m)):
		if(p[m[i-1]]==p[i-1]):
			m[i]=m[i-1]+1
		else:
			m[i]=0
		i+=1
	return m

def subcompare(t,p,l):
	m=match(p)
	ok=True
	j=0
	while(ok and l<len(t)):
		if(t[l]==p[j]): 
			j+=1
			if(j==len(p)): ok=False
		else:
			while(j!=-1 and p[j]!=t[l]): j=m[j]
			j+=1
		l+=1
	return not(ok),l

def solve(t,p):
	p=p.split("*")
	ok=True;i=0;l=0
	while(i<len(p) and ok):
		if(len(p[i])!=0): ok,l=subcompare(t,p[i],l)
		i+=1
	if(ok): print("yes")
	else: print("no")

def main():
	n=(stdin.readline().strip())
	while(n!=""):
		n=int(n)
		t=stdin.readline().strip()
		for i in range(n):
			p=stdin.readline().strip()
			solve(t,p)
		n=(stdin.readline().strip())
main()