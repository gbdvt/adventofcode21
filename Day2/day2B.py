data = open("day2.txt", "r").read().splitlines()
aim=0
depth=0
horizontal=0
for i in data:
    n=i.split()
    command=n[0]
    value=n[1]
    if command=="up":
        aim-=int(value)
    elif command=="down":
        aim+=int(value)
    elif command=="aim":
        aim=value
    elif command=="forward":
        horizontal+=int(value)
        depth+=int(value)*aim
print(horizontal*depth)