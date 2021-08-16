from sys import stdin

def solve(n):
	f,e=n,0
	cont=0
	while (f+e>2):
		cont+=f
		e+=f
		tmp=e%3
		f=e//3
		e=tmp
	cont+=f
	if(f+e==2): cont+=1
	return cont


def main():
	line=stdin.readline().strip()
	while line!="":
		print(solve(int(line)))
		line=stdin.readline().strip()
main()