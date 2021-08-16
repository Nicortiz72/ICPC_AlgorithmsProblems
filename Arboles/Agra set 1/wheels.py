from sys import stdin
from collections import deque
change=[1000,100,10,1]
vis=1
det=[0 for _ in range(10000)]
def next_state(t):
    ans=[]
    for i in range(4):
        y=10**(3-i)
        x=(t//y)%10
        if(x == 9): tmp=t-(y*9)
        else: tmp=t+change[i]
        if(det[tmp]!=vis): ans.append(tmp)
        if(x == 0): tmp=t+(y*9)
        else: tmp=t-change[i]
        if(det[tmp]!=vis): ans.append(tmp)
    return ans

def bfs(source, tarjet):
    global det
    if(source==tarjet): return 0
    if(det[source]==vis): return -1
    dist=[-1 for _ in range(10000)]
    queue=deque() ; queue.append((source,0))
    det[source]=vis
    while(dist[tarjet]==-1 and len(queue)!=0):
        u,d=queue.popleft()
        dist[u]=d
        for v in next_state(u):
            if(v==tarjet): return d+1
            queue.append((v,d+1));det[v]=vis
        det[u]=vis
    if(dist[tarjet]==-1):
        return -1
    else:
        return dist[tarjet]
    
def main():
    global vis,det
    n=int(stdin.readline())
    vis=1
    for i in range(n):
        stdin.readline()
        start=stdin.readline().split()
        start=int(start[0])*1000+int(start[1])*100+int(start[2])*10+int(start[3])
        end=stdin.readline().split()
        end=int(end[0])*1000+int(end[1])*100+int(end[2])*10+int(end[3])
        det[end]=0
        n1=int(stdin.readline())
        for j in range(n1):
            x=stdin.readline().split()
            x=int(x[0])*1000+int(x[1])*100+int(x[2])*10+int(x[3])
            det[x]=vis
        print(bfs(start,end))
        vis+=1
        
main()
    
