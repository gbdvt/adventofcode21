data=open("day3.txt", "r").read().splitlines()
zeros=[0]*12
ones=[0]*12
for i in data:
    for l in range(12):
        if i[l]=="0":
            zeros[l]+=1
        else:
            ones[l]+=1
gamma=[0]*12
epsilon=[0]*12
for i in range(12):
    if zeros[i]>ones[i]:
        gamma[i]=0
        epsilon[i]=1
    else:
        gamma[i]=1
        epsilon[i]=0
decimalgamma=0
decimalepsilon=0
for i in range(12):
    if gamma[i]==1:
        decimalgamma+=2**(11-i)
    if epsilon[i]==1:
        decimalepsilon+=2**(11-i)
print(decimalepsilon*decimalgamma)
