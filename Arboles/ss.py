from sys import stdin

line=stdin.readline().strip()
New=[]
D={}
con=0
while(line!="-1"):
    print("--->   ",line)
    line=[int(x) for x in line.split()]
    for i in line:
        if not(i in list(D.keys())):
            D[i]=con
            con+=1
    New.append([D[line[0]], D[line[1]]])
    line=stdin.readline().strip()

for i in New:
    print(i[0],i[1])
            
