def maxBoundArray(L,U,n):
	if(n>(2*(U-L+1))-1): return None
	arr=list()
	if(U-L+2>=n):
		arr.append(U-1)
		for i in range(n-1):
			arr.append(U-i)
	else:
		for i in range(n-(U-L+1),0,-1):
			arr.append(U-i)
		for i in range((U-L+1)):
			arr.append(U-i)
	return arr


