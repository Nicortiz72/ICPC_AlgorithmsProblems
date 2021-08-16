from sys import stdin

class Binary:
	val=None
	r=None
	l=None
	def __init__(self,v,ri=None,le=None):
		self.val=v
		self.r=ri
		self.l=le
	def add(self,node):
		if(self.val==None): self.val=node
		else:
			Node=Binary(node)
			tmp=self
			while(tmp!=None):
				T=tmp
				if(node>tmp.val): tmp=tmp.r
				else: tmp=tmp.l
			if(node>T.val): T.r=Node
			else: T.l=Node
def post(A):
	if(A!=None):
		post(A.l)
		post(A.r)
		print(A.val)

def main():
	line=stdin.readline()
	A=Binary(None)
	while(line!=""):
		A.add(int(line))
		line=stdin.readline()
	post(A)
main()