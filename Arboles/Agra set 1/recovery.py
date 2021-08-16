from sys import stdin

def solve(P,I,Pi,Pf,Ii,If):
	ans=""
	tmp=I.index(P[Pi])
	y=-1
	if(tmp!=Ii):
		y=Pi
		while(y<Pf and I.index(P[y+1])<tmp): y+=1
		if(y!=Pi):ans+=solve(P,I,Pi+1,y,Ii,tmp-1)
	if(tmp!= If):
		if(y!=-1): ans+=solve(P,I,y+1,Pf,tmp+1,If)
		else: ans+=solve(P,I,Pi+1,Pf,tmp+1,If)
	ans+=P[Pi]
	return ans

def main():
	line=stdin.readline()
	while(line!=""):
		line=line.split()
		print(solve(line[0],line[1],0,len(line[0])-1,0,len(line[1])-1))
		line=stdin.readline()
main()