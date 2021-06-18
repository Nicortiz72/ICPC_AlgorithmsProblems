import heapq as hq

def Schedeule(power,tasks):
	heap=[-i for i in power]
	count=0
	while tasks>0:
		val=hq.heappop(heap)
		tasks-=abs(val)
		hq.heappush(heap,val//2)
		count+=1
	return count

print(Schedeule([4,2,8,3,5],19))

