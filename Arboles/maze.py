from sys import stdin
from heapq import heappop,heappush

INF = float('inf')

def dijkstra(G, s):
  ans = [ INF for _ in G ] ; ans[s] = 0
  prev = [ None for _ in G ]
  visited = [ False for _ in G ]
  heap = [ (0, s) ]
  while len(heap)!=0:
    d,u = heappop(heap)
    if visited[u]==False:
      for v,dv in G[u]:
        if d+dv<ans[v]:
          ans[v] = d+dv
          heappush(heap, (ans[v], v))
          prev[v] = u
      visited[u] = True
  return ans

def solve(G,exit,time):
  ans=dijkstra(G,exit)
  count=0
  for i in ans:
    if(i<=time):
      count+=1
  return count

def main():
  n=int(stdin.readline())
  f=False
  for i in range(n):
    stdin.readline()
    lenv=int(stdin.readline())
    exit=int(stdin.readline())
    time=int(stdin.readline())
    lene=int(stdin.readline())
    G=[list() for _ in range(lenv)]
    for j in range(lene):
      u,v,d = map(int, stdin.readline().split())
      G[u-1].append((v-1,d))
    if(f): print();f=True
    print(solve(G,exit,time))

main()