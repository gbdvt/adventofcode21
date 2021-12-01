data=open("file.txt", "r").read().splitlines()
t=0
for i in range(len(data)):
	c=int(data[i])
	if (i==0):p=c
	if c>p:t+=1
	p=c
print(t)
