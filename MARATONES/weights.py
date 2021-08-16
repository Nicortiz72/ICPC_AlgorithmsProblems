from sys import stdin

def solve(n,R):
	D={}
	for j in range(len(R)):
		for i in range(len(R[j])):
			if(D.get(R[j][i])==None): D[R[j][i]]=list()
			D[R[j][i]].append((j,i))
	num=list(D.keys())
	num.sort(reverse=True)
	i=0;m=0
	while i<len(num) and num[i]>m:
		z=num[i]
		if(D[z][0][0]!=D[z][1][0]): m=z
		elif(abs(D[z][0][1]-D[z][1][1])>1):
			mt=0
			k=D[z][0][1]+1
			ini=k
			hi=D[z][1][1]
			r=D[z][1][0]
			while k < hi:
				tmp=R[r][k]
				if(tmp>z and D[tmp][0][1] > ini and D[tmp][0][1] < hi):
					mt=max(mt,m)
					k=D[tmp][0][1]+1
				else:
					mt=max(mt,tmp)
					k+=1
			m=max(m,min(mt,z))
		i+=1
	return m

def main():
	line=stdin.readline().strip()
	while line!="":
		n=int(line)
		R=list()
		R.append([int(x) for x in stdin.readline().split()])
		R.append([int(x) for x in stdin.readline().split()])
		print(solve(n,R))
		line=stdin.readline().strip()
main()