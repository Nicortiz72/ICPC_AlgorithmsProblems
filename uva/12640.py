from sys import stdin

def main():
	line=stdin.readline().strip()
	while line!="":
		line=[int(x) for x in line.split(" ")]
		ans=0
		count=0
		for i in line:
			if(count+i<=0):
				count=0
			else:
				count+=i
				ans=max(ans,count)
		print(ans)
		line=stdin.readline()
main()