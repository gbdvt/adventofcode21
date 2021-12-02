data = open("day2.txt", "r").read().splitlines()
depth=0
horizontal=0
for i in data:
    n=i.split()
    if n[0]=="up":
        depth-=int(n[1])
    elif n[0]=="down":
        depth+=int(n[1])
    else:
        horizontal+=int(n[1])
print(depth*horizontal)