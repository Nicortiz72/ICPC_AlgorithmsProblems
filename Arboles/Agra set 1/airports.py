from sys import stdin

class dforest(object):

  def __init__(self, size=10):
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 1 for _ in range(size) ]
    self.__csize = [ 1 for _ in range(size) ]
    self.__ccount = self.__size = size

  def __str__(self):
    return str(self.__parent)

  def __len__(self):
    return self.__size

  def csize(self, x):
    return self.__csize[self.find(x)]

  def ccount(self):
    return self.__ccount
  
  def find(self, x):
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]
  
  def union(self, x, y):
    fx,fy = self.find(x),self.find(y)
    if fx!=fy:
      rx,ry = self.__rank[fx],self.__rank[fy]
      if rx>ry:
        self.__parent[fy] = fx
        self.__csize[fx] += self.__csize[fy]
      else:
        self.__parent[fx] = fy
        self.__csize[fy] += self.__csize[fx]
        if rx==ry:
          self.__rank[fy] += 1
      self.__ccount -= 1

def kruskal(graph, lenv):
  ans = list()
  suma=0
  count=0
  graph.sort(key = lambda x: x[2])
  df,i = dforest(lenv),0
  while i!=len(graph):
    u,v,d = graph[i]
    if df.find(u)!=df.find(v):
      ans.append((u, v, d))
      suma+=d
      count+=1
      if(count==lenv-1): break
      df.union(u, v)
    i += 1
  return count,suma


def solve(G,N,A):
  ans,suma=kruskal(G,N)
  n=N-ans
  suma+=A*n
  return [suma,n]


def main():
  n=int(stdin.readline())
  for i in range(n):
    N,M,A=[int(x) for x in stdin.readline().split()]
    G=[]
    for j in range(M):
      u,v,d=[int(x) for x in stdin.readline().split()]
      if(d<A): G.append((u-1,v-1,d))
    ans=solve(G,N,A)
    print("Case #{0}: {1} {2}".format(i+1,ans[0],ans[1]))

  
main()