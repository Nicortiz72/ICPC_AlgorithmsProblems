from sys import stdin
from collections import deque
change=[1000,100,10,1]
def next_state(t):
    ans=[]
    for i in range(4):
        y=change[i]
        x=(t//y)%10
        if(x == 9): tmp=t-(y*9)
        else: tmp=t+change[i]
        if(dist[tmp]==-1): ans.append(tmp)
        if(x == 0): tmp=t+(y*9)
        else: tmp=t-change[i]
        if(dist[tmp]==-1): ans.append(tmp)
    return ans

def bfs(source, tarjet):
    global dist
    if(source==tarjet): return 0
    if(dist[source]==0): return -1
    queue=deque() ; queue.append((source,0))
    dist[source]=0
    while(dist[tarjet]==-1 and len(queue)!=0):
        u,d=queue.popleft()
        dist[u]=d
        for v in next_state(u):
            if(v==tarjet): return d+1
            queue.append((v,d+1));dist[v]=d+1
    if(dist[tarjet]==-1 or dist[tarjet]==0):
        return -1
    else:
        return dist[tarjet]
    
def main():
    global dist
    n=int(stdin.readline())
    for i in range(n):
        stdin.readline()
        start=stdin.readline().split()
        start=int(start[0])*1000+int(start[1])*100+int(start[2])*10+int(start[3])
        end=stdin.readline().split()
        end=int(end[0])*1000+int(end[1])*100+int(end[2])*10+int(end[3])
        n1=int(stdin.readline())
        dist=[-1 for _ in range(10000)]
        for j in range(n1):
            x=stdin.readline().split()
            x=int(x[0])*1000+int(x[1])*100+int(x[2])*10+int(x[3])
            dist[x]=0
        print(bfs(start,end))
        
main()
    
