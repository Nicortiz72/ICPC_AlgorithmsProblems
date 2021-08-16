from sys import *

x=None;y=None;d=None
def euclid(a,b):
	global x,y,d
	if(b==0):
		x=1;y=0;d=a
		return
	euclid(b,a%b)
	x1=int(y)
	y1=int(x - (a/b) * y)
	x=x1
	y=y1

def main():
	global x,y,d
	line=stdin.readline().strip()
	while line!="":
		x=None;y=None;d=None
		A,B=[int(x) for x in line.split()]
		if(A<B):
			r=True
			a=B;b=A
		else:
			r=False
			a=A;b=B
		euclid(a,b)
		if(r): print(int(y),int(x),int(d))
		else: print(int(x),int(y),int(d))

		line=stdin.readline().strip()
main()