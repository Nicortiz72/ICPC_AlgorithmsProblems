from sys import stdin

def phi(x):
  y=0
  if(x>0):
    if(x<=100):
      y+=x*2
    else:
      y+=200
    x-=100
    if(x>0):
      if(x <= 9900):
        y+=x*3
      else:
        y+=(9900)*3
      x-=9900
      if(x>0):
        if(x<=990000):
          y+=x*5
        else:
          y+=990000*5
        x-=990000
        if(x>0):
          y+=x*7
  return y
def beta(y):
  x=0
  if(y>0):
    if(y<=200):
      x+=y/2
    else:
      x+=100
    y-=200
    if(y>0):
      if(y<=9900*3):
        x+=y/3
      else:
        x+=9900
      y-=9900*3
      if(y>0):
        if(y<=990000*5):
          x+=y/5
        else:
          x+=990000
        y-=990000*5
        if(y>0):
          x+=y/7
  return x
  
def solve(tsum, diff):
  tsum=beta(tsum)
  low,hi=0,tsum
  while(low<hi):
    mid=(hi+low)//2
    x= phi(tsum-mid)-phi(mid)
    if(x==diff):
      return int(phi(mid))
    if(x>diff):
      low=mid
    else:
      hi=mid

def main():
  tsum,diff = map(int,stdin.readline().split())
  while tsum+diff!=0:
    print(solve(tsum, diff))
    tsum,diff = map(int,stdin.readline().split())
main()
