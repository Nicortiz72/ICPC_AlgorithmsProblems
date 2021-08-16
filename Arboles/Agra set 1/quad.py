from sys import stdin
l=0
class Tree:
	val=None
	ch=[]
	def __init__(self,v,cha=[],d=None):
		val=v
		ch=cha
	def printT(self):
		print(self.val)
		print("..")
		for i in self.ch: print(i.val,end="")
		print()
		for i in self.ch:
			i.printT()

def add(line):
	global l
	T=Tree(None)
	if(line[l]=='f'): T.val=1
	elif(line[l]=='e'): T.val=0
	else:
		T.val=2
		arr=list()
		for i in range(4):
			l+=1
			arr.append(add(line))
		T.ch=arr
	return T

def sum(T,mul):
	cont=0
	if(T.val==1): return mul
	elif(T.val==0): return 0
	else:
		for j in range(4):
			cont+=sum(T.ch[j],mul/4)
		return cont

def solve(T1,T2,mul=1024):
	cont=0
	if(T1.val==0 and T2.val==0): return 0
	elif(T1.val==1 or T2.val==1): return mul
	elif(T1.val==2 and T2.val==0): return sum(T1,mul)
	elif(T1.val==0 and T2.val==2): return sum(T2,mul)
	else:
		for j in range(4):
			cont+=solve(T1.ch[j],T2.ch[j],mul/4)
		return cont


def main():
	global l
	n=int(stdin.readline())
	for i in range(n):
		l=0
		line=stdin.readline().strip()
		T1=add(line)
		l=0
		line=stdin.readline().strip()
		T2=add(line)
		print("There are {0} black pixels.".format(int(solve(T1,T2))))
main()

