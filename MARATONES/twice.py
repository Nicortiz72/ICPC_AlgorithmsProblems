from sys import stdin
from sys import stdout

    
ref=-1#
U=stdin.readline().strip()

while(len(U)!=0):
    arrFixed=[]
    jump=[e for e in range(len(U))]
    
    Fixed=[0 for e in range(10)]
    i=0
    ref=-1 #
    while(i<len(U)):
        valU=int(U[i])
        Fixed[valU]+=1
        newFixed=Fixed[:]
        arrFixed.append(newFixed)
        m=valU-1
        while(m>=0):
            if(Fixed[m])>=2:
                m-=1
                continue
            break
        if(m==-1 and i!=0):
            jump[i]=jump[i-1]
        if(Fixed[valU]==3):
            ref=jump[i]
            Fixed=list(arrFixed[ref])
            break
        i+=1
    
    tmp=U
    U=list()
    for e in range(len(tmp)):
        U.append(int(tmp[e]))

    flag=True
    while(flag and ref!=-1):
        j=ref
        while(j>=0):
            #print(U)
            last=U[j]-1
            if(last==-1):
                last=9
            Fixed[U[j]]-=1
            Fixed[last]+=1
            U[j]=last
            if(last!=9):
                break
            j-=1
        flag=False
        for e in range(10):
            if Fixed[e]>=3:
                flag=True
                break
    fi=9
    while(fi>=0):
        if Fixed[fi]==2:
            fi-=1
            continue
        break
    if(ref!=-1):
        for e in range(ref+1,len(U)):
            U[e]=fi
            Fixed[fi]+=1
            while(Fixed[fi]>=2):
                fi-=1
    i=0
    for e in range(len(U)):
        if(U[e]!=0):
            break
        i+=1
    U=U[i:]
            
    print("".join([str(x) for x in U]))
    U=stdin.readline().strip()

stdout.close()
