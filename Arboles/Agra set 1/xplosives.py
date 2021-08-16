from sys import stdin

class dforest(object):
  """implements an union-find with path-compression and ranking"""

  def __init__(self, con):
    self.__parent ={}
    self.__rank = {}
    self.__csize = {}
    for i in con:
      self.__parent[i[0]]=i[0]
      self.__parent[i[1]]=i[1]
      self.__rank[i[0]]=1
      self.__rank[i[1]]=1
      self.__csize[i[0]]=1
      self.__csize[i[1]]=1
    self.__ccount = self.__size = len(self.__parent)

  def __str__(self):
    """return the string representation of the forest"""
    return str(self.__parent)

  def __len__(self):
    """return the number of elements in the forest"""
    return self.__size

  def csize(self, x):
    """return the number of elements in the component of x"""
    return self.__csize[self.find(x)]

  def ccount(self):
    """return  the numnber of components"""
    return self.__ccount
  
  def find(self, x):
    """return the representative of the component of x"""
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]
  
  def union(self, x, y):
    """computes the union of the components of x and y, if they are different"""
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

def solve(con):
  if(len(con)==0): return 0
  forest=dforest(con)
  o=0
  while(o<len(con) and con[o][0]==con[o][1]): o+=1
  if(o==len(con)): return o
  forest.union(con[o][0],con[o][1])
  comp=1
  ans=o
  for i in con[o+1:]:
    p=forest.find(con[o][0])
    sz=forest.csize(p)
    fx,fy = forest.find(i[0]),forest.find(i[1])
    if(fx!=p and fy!=p):
      if(i[0]==i[1]): sz-=1
      if(comp+1!=sz+2):
        forest.union(i[0],p)
        forest.union(i[1],p)
        comp+=1
        #print("p1",forest.csize(p),comp)
      else: ans+=1
    elif(fx!=p or fy!=p):
      if(comp+1!=sz+1):
        if(fx!=p): forest.union(i[0],p)
        else: forest.union(i[1],p)
        comp+=1
        #print("p2",forest.csize(p),comp)
      else: ans+=1
    else:
      if(comp+1!=sz):
        comp+=1
        #print("p3",forest.csize(p),comp)
      else: ans+=1
  return ans

def solve2(con):
  if(len(con)==0): return 0
  forest=dforest(con)
  ans=0
  for i in con: forest.union(i[0],i[1])
  for i in con:
    fx=forest.find(i[0])
    fy=forest.find(i[1])
    if(fx!=fy and forest.csize(con[0][1]) != forest.ccount()): forest.union(i[0],con[0][1])
    else: ans+=1
  return ans

def main():
  line="  "
  while(line!=""):
    line=stdin.readline()
    con=[]
    while(line!="-1"):
      a,b=[int(x) for x in line.split()]
      con.append((a,b))
      line=stdin.readline().strip()
    print(solve(con))
    line=stdin.readline()

main()