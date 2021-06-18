import heapq as hq
def fiveStartReviews(productRatings, ratingsThreshold):
    N=len(productRatings)
    val=0
    productHeap=list()
    for n,d in productRatings:
        if(n!=d):
            productHeap.append((d,n))
        val+=n*100/d  
    val/=N
    count=0
    while val<ratingsThreshold:
        print(val)
        d,n=hq.heappop(productHeap)
        print(d,n)
        val+=((((n*d)+(d)-(n*d)-n)/(d*(d+1)))/N)*100
        hq.heappush(productHeap,(d+1,n+1))
        count+=1
    return count
print(fiveStartReviews([[4,4], [1,2], [3, 6]],77))