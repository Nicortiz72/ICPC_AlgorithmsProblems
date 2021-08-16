from sys import stdin

def solve(T):
  ans = ""
  a,b=0,1
  c,d=1,0
  n,m=1,1
  while m*T[0]!=n*T[1]:
    if(m*T[0] > n*T[1]):
      a,b=n,m
      n,m=n+c,m+d
      ans+="R"
    else:
      c,d=n,m
      n,m=n+a,m+b
      ans+="L"
      
  return ans

def main():
  target = [int(x) for x in stdin.readline().strip().split()]
  while target[0]!=1 or target[1]!=1:
    print(solve(target))
    target = [int(x) for x in stdin.readline().strip().split()]

main()
