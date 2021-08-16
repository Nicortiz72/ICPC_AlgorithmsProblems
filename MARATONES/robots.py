from sys import stdin

def main():
    f,c=[int(x) for x in stdin.readline().split()]
    while(f!=-1 and c!=-1):
        ans=[1]
        while(f!=0 and c!=0):
            i=0
            while(i!=len(ans) and ans[i]>c): i+=1
            if(i==len(ans)): ans.append(c)
            else: ans[i]=c
            f,c=[int(x) for x in stdin.readline().split()]
        print(len(ans))
        f,c=[int(x) for x in stdin.readline().split()]
main()
            
