from sys import stdin
mx=1000000
def creation():
  S=[1 for i in range(mx)]
  for i in range(2,(mx/2)+1):
    for j in range(i,mx,i):
      S[j]+=1
  arr=[1]
  N=1
  while(N<mx):
    N+=S[N]
    arr.append(N)
  return arr
M=creation()

def search1(n):
  lw,hi=0,len(M)
  mid=(lw+hi)//2
  while(M[mid]!=n and lw +1 < hi):
    if(M[mid]>n):
      hi=mid
    else:
      lw=mid
    mid=(lw+hi)//2
  if(M[mid]!=n):
    mid=lw+1
  return mid
def search2(n):
  lw,hi=0,len(M)
  mid=(lw+hi)//2
  while(M[mid]!=n and lw +1 < hi):
    if(M[mid]>n):
      hi=mid
    else:
      lw=mid
    mid=(lw+hi)//2
  if(M[mid]!=n):
    mid=lw
  return mid

def solve(A, B):
  return (search2(B)-search1(A))+1

def main():
  tcnt = int(stdin.readline())
  for tc in range(1, tcnt+1):
    A,B = map(int, stdin.readline().split())
    print('Case {0}: {1}'.format(tc, solve(A, B)))

main()


