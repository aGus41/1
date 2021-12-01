with open('input.txt') as f:
    lines = f.readlines()

depth=[]
for line in lines:    
    depth.append(line.rstrip())

inc=0
for i, val in enumerate(depth):
    if i==0:
        pass
    elif int(val)>int(depth[i-1]):
        inc=inc+1

print(inc)

