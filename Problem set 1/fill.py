from sys import stdin

def test(A,m,mid):
	c=1;cap=mid
	for i in A:
		if(i>mid): return False
		if(i>cap):
			if(c==m): return False
			cap=mid
			c+=1
		cap-=i
	return True 

def solve(A,m):
	hi = 0
	for i in A: hi+=i
	l=1
	r=0
	while(l<=hi):
		mid=(l+hi)//2
		if(test(A,m,mid)):
			r=mid
			hi=mid-1
		else:
			l=mid+1
	return r


def main():
	line=stdin.readline().strip()
	while line != "":
		n,m=[int(x) for x in line.split()]
		A=[int(x) for x in stdin.readline().split()]
		print(solve(A,m))
		line=stdin.readline().strip()
main()