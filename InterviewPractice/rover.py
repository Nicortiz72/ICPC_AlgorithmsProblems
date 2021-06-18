from sys import stdin
def roverMove():
	n=int(stdin.readline())
	m=int(stdin.readline())
	cmd=list()
	for i in range(m):
		cmd.append(stdin.readline().strip())
	posR=0
	posC=0
	for i in cmd:
		if(i=="UP"): posR=max(0,posR-1)
		elif(i=="DOWN"): posR=min(n-1,posR+1)
		elif(i=="LEFT"): posC=max(0,posC-1)
		elif(i=="RIGHT"): posC=min(n-1,posC+1)
	return (posR*n)+posC
while True:
	print(roverMove())
