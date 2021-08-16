from sys import stdin
l=[]
def g(lo, hi):
#minima cantidad de flips para ordenar l de lo a hi
    #conquistar
    if hi-lo <=1:
        return 0
    #dividr
    mid = (lo+hi)//2
    cnt = g(lo,mid)
    cnt += g(mid,hi)

    #Combinar
    i1 = lo
    i2 = mid
    ln=[]
    while(i1 < mid and i2 < hi ):
        if(l[i1] <= l[i2]):
           ln.append(l[i1])
           i1+=1
        else:
           ln.append(l[i2])
           i2+=1
           cnt +=mid-i1
           
    while(i1 < mid):
        ln.append(l[i1])
        i1+=1
    while(i2 < hi):
        ln.append(l[i2])
        i2+=1
    l[lo:hi] = ln
    return cnt

def main():
  global l
  inp = stdin
  n = int(stdin.readline().strip())
  while n>0:
    l=[]
    for i in range(n):
      l.append(int(stdin.readline()))
    print(g(0, n))
    n = int(stdin.readline().strip())

main()
