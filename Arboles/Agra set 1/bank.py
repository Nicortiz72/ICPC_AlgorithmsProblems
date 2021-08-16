from sys import stdin
from heapq import heappop,heappush

INF = float('inf')
G=None
def dijkstra(B):
  global G
  ans = [ INF for _ in G ]
  for i in B: ans[i]=0
  prev = [ None for _ in G ]
  visited = [ False for _ in G ]
  heap = [ (0, s) for s in B ]
  while len(heap)!=0:
    d,u = heappop(heap)
    if visited[u]==False:
      for v,dv in G[u]:
        if d+dv<ans[v]:
          ans[v] = d+dv
          heappush(heap, (ans[v], v))
          prev[v] = u
      visited[u] = True
  for s in B: ans[s]=INF
  return ans

def minA(A,B):
  t=[]
  m=-1
  for i in range(len(A)):
    if(A[i]==m): t.append(B[i])
    elif(A[i] > m): m=A[i];t=[B[i]]
  t.sort()
  return t,m
def solve(B,P):
  global G
  dis=[]
  tmp=dijkstra(P)
  tmp2=[]
  for j in B: tmp2.append(tmp[j])
  dis.append(max(tmp2) if len(tmp2) > 0 else -1)
  dis=minA(tmp2,B)
  print(len(dis[0]),dis[1] if type(dis[1])==int and dis[1]>=0 else "*")
  for i in dis[0][0:len(dis[0])-1]: print(i,end=" ")
  print(dis[0][len(dis[0])-1])

def main():
  global G
  line=stdin.readline().strip()
  while(line!=""):
    N,M,B,P=[int(x) for x in line.split()]
    G=[[] for _ in range(N)]
    for i in range(M):
      u,v,d=[int(x) for x in stdin.readline().split()]
      G[u].append((v,d))
      G[v].append((u,d))
    Ban=[]
    tmp=stdin.readline().split()
    for i in tmp: Ban.append(int(i))
    Pol=[]
    if(P!=0):
      tmp=stdin.readline().split()
      for i in tmp: Pol.append(int(i))
    solve(Ban,Pol)
    line=stdin.readline().strip()
main()