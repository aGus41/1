with open('input.txt') as f:
    lines = f.readlines()

depth=[]
for line in lines:    
    depth.append(line.rstrip())

windows=[]
for i, val in enumerate(depth):
    if i<len(depth)-2:
        windows.append(int(val) + int(depth[i+1]) + int(depth[i+2]))
# print(windows)

inc=0
for i, val in enumerate(windows):
    if i==0:
        pass
    elif int(val)>int(windows[i-1]):
        inc=inc+1

print(inc)