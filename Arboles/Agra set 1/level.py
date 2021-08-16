# tree summing
from sys import stdin
from collections import deque
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
L,R,NEG,SPACE, CR, LPAR, RPAR, ZERO, NINE = ord('L'),ord('R'),ord('-'),ord(' '), ord('\n'), ord('('), ord(')'), ord('0'), ord('9')

def has_next(): return I<len(INPUT)

def is_par(): return RPAR==INPUT[I]
def is_digit(): return ZERO <= INPUT[I] <= NINE
def is_neg(): return INPUT[I]==NEG
def is_letter(): return L == INPUT[I] or  R == INPUT[I]

def read_blanks():
	global INPUT, I
	while has_next() and not(is_digit()) and not(is_letter()) and not(is_par()): I+=1

def read_par():
	global INPUT, I
	I = I+1
	return INPUT[I-2]==LPAR
def read_letter():
	global INPUT, I
	ans = ""
	while has_next() and is_letter():
		ans, I = ans+chr(INPUT[I]), I+1
	return ans

def read_num(s):
	global INPUT, I
	ans = 0
	if(s==-1): I+=1
	while has_next() and is_digit():
		ans, I = int(chr(INPUT[I])) + ans*10, I+1
	return ans*s
	
def next_token():
	global INPUT, I
	ans = None
	read_blanks()
	if I!=len(INPUT):
		if is_digit(): ans = read_num(1)
		elif is_letter(): ans=read_letter()
		elif is_par(): 
			if(read_par()): ans='F'
			else: ans='G'
		else: ans = read_par() 
	return ans

def solve(tree):
	que=deque()
	que.append(tree)
	ans=""
	while(len(que)!=0 and ans!=-1):
		tmp=que.popleft()
		if(tmp.val!=None):ans+=str(tmp.val) + " "
		else: ans=-1
		if(tmp.l!=None): que.append(tmp.l)
		if(tmp.r!=None): que.append(tmp.r)
	if(ans==-1): return "not complete"
	else: return ans[:len(ans)-1] 


def make(num):
	T=Binary()
	while(num!='F' and num != None):
		tmp=T
		st=next_token()
		if(st!='G'):
			for i in st:
				if(i=='L'):
					if(tmp.l==None):
						new=Binary()
						tmp.l=new
					tmp=tmp.l
				if(i=='R'):
					if(tmp.r==None):
						new=Binary()
						tmp.r=new
					tmp=tmp.r
			next_token()
		if(tmp.val!=None): return -1
		tmp.val=num
		num=next_token()
	return T


def main():
	global INPUT, I
	num = next_token()
	while num!=None:
		tree = make(num)
		if(tree==-1):
			TK=next_token()
			while(TK!='F'): TK=next_token()
			print("not complete")
		else:
			print(solve(tree))
		num = next_token()
main()

