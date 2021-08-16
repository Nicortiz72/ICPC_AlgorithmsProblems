# tree summing
from sys import stdin

class Binary:
	val=None
	l=None
	r=None
	def __init__(self,v=None,le=None,ri=None):
		val=v
		l=le
		r=ri

def printT(T):
	if(T.l!=None): printT(T.l)
	print(T.val, end=" ")
	if(T.r!=None): printT(T.r)

INPUT, I = stdin.buffer.read(),0	
SPACE, CR, LPAR, RPAR, ZERO, NINE = ord(' '), ord('\n'), ord('('), ord(')'), ord('0'), ord('9')

def has_next(): return I<len(INPUT)

def is_par(): return LPAR==INPUT[I] or RPAR==INPUT[I]
def is_digit(): return ZERO <= INPUT[I] <= NINE

def read_blanks():
	global INPUT, I
	while has_next() and not(is_digit()) and not(is_par()): I+=1

def read_par():
	global INPUT, I
	ans, I = chr(INPUT[I]), I+1
	return ans

def read_num():
	global INPUT, I
	ans = 0
	while has_next() and is_digit():
		ans, I = int(chr(INPUT[I])) + ans*10, I+1
	return ans
	
def next_token():
	global INPUT, I
	ans = None
	read_blanks()
	if I!=len(INPUT):
		if is_digit(): ans = read_num()
		else: ans = read_par() 
	return ans

def solve(n, tree):
	stack=[(tree,tree.val)]
	ok=True
	while(len(stack)!=0 and ok):
		p,q=stack.pop()
		if(p.l==None and p.r==None and q==n): ok=False
		else:
			if(p.l!=None): stack.append((p.l,q+p.l.val))
			if(p.r!=None): stack.append((p.r,q+p.r.val))
	return not(ok)

def make():
	T=Binary()
	c=next_token()
	if(c=='('):
			p=next_token()
			if(p==')'):
				return None
			else:
				new=make()
				T.l=new
				new=make()
				T.r=new
				T.val=p
				next_token()
	return T


def main():
	global INPUT, I
	num = next_token()
	while num!=None:
		tree = make()
		if(tree!=None):
			print('yes'if solve(num,tree) else 'no')
		else:
			print('no')
		num = next_token()
main()
