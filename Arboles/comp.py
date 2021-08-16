import random
def fuc(n,m):
    ls=[0 for i in range(m)]
    cont=0
    dia=1
    while (1):
        Tmp=0
        lsn=list()
        for i in range(len(ls)):
            if(ls[i]<n):
                ls[i]+=random.randint(0,n)
                lsn.append(ls[i])
        for i in lsn:
            if(i >= n):
                Tmp+=1
        ls=lsn
        cont+=Tmp
        if(len(lsn)==0):
            break
        print("Dia",dia)
        print((cont/m)*100,"%")
        print("Tmp=",Tmp)
        print("Cont=",cont,"\n")
        
        dia+=1
    
