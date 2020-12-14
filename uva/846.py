from sys import *

Sumatory=[0,1]
Values=[0,1]
n=3
i=2
lim=1<<31
while n<=lim:
	Sumatory.append(n)
	Values.append((2*Sumatory[i//2])+(0 if i%2==0 else (i//2)+1))
	i+=1;n+=i

def binarySearch(k):
	low=0;high=len(Values)
	while low+1!=high:
		mid=(low+high)>>1
		if(Values[mid]==k): return mid
		elif(Values[mid]>k): high=mid
		else: low=mid
	return high

def main():
	t=int(stdin.readline())
	for _ in range(t):
		f,s=[int(x) for x in stdin.readline().split(" ")]
		print(binarySearch(s-f))
main()