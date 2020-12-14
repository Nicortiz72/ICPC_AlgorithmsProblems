from sys import stdin

MAX = 100000
AUX = [ None for _ in range(MAX) ] 

def mergesort(A, low, hi):
  count=0
  if low+1<hi:
    mid = low+((hi-low)>>1)
    mergesort(A, low, mid)
    mergesort(A, mid, hi)
    count+=merge(A, low, mid, hi)
  return count

def merge(A, low, mid, hi):
  for i in range(low, hi): AUX[i] = A[i]
  l,r,i = low,mid,low
  count=0
  while i!=hi:
    if r==hi:
      A[i] = AUX[l]
      i,l = i+1,l+1
    elif l==mid:
      A[i] = AUX[r]
      count+=r-i
      i,r = i+1,r+1
    else:
      if AUX[l]<=AUX[r]:
        A[i] = AUX[l]
        i,l = i+1,l+1
      else:
        A[i] = AUX[r]
        count+=r-i+1
        i,r = i+1,r+1
  return count

def main():
  line=int(stdin.readline())
  while line!=0:
    n=(line)
    A=[]
    for i in range(n):
      A.append(int(stdin.readline()))
    print(mergesort(A,0,n))
    line=int(stdin.readline())
main()