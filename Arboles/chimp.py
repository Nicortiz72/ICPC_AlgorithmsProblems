from sys import stdin
M=None
def search(n):
  lw,hi=0,len(M)
  mid=(lw+hi)//2
  while(M[mid]!=n and lw +1 < hi):
    if(M[mid]>n):
      hi=mid
    else:
      lw=mid
    mid=(lw+hi)//2
  return mid

def solve(t):
	x1=search(t)
	x2=x1
	if(M[x1]==t):
		if(x1==0):
			x1="X"
		else:
			x1=str(M[x1-1])
	else: x1=str(M[x1])
	if(M[x2]==t or M[x2]<t):
		if(x2==len(M)-1):
			x2="X"
		else:
			x2=str(M[x2+1])
	else: x2=str(M[x2])
	return x1+" "+x2

def main():
	global M
	n=int(stdin.readline())
	M=[int(i) for i in stdin.readline().split()]
	c=int(stdin.readline())
	T=[int(i) for i in stdin.readline().split()]
	for i in T:
		print(solve(i))
main()
