MAX = 100000
AUX = [ None for _ in range(MAX) ] 

def mergesort(A, low, hi):
  if low+1<hi:
    mid = low+((hi-low)>>1)
    mergesort(A, low, mid)
    mergesort(A, mid, hi)
    merge(A, low, mid, hi)

def merge(A, low, mid, hi):
  for i in range(low, hi): AUX[i] = A[i]
  l,r,i = low,mid,low
  while i!=hi:
    if r==hi:
      A[i] = AUX[l]
      i,l = i+1,l+1
    elif l==mid:
      A[i] = AUX[r]
      i,r = i+1,r+1
    else:
      if AUX[l]<=AUX[r]:
        A[i] = AUX[l]
        i,l = i+1,l+1
      else:
        A[i] = AUX[r]
        i,r = i+1,r+1