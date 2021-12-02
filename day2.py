from types import ModuleType


with open('day2-input.txt') as f:
    lines = f.readlines()

movements=[]
for line in lines:    
    movements.append(line.rstrip().split(" "))

horizontal, depth, aim = 0, 0, 0
for move in movements:
    if move[0]=="forward":
        horizontal+=int(move[1])
        depth     +=aim*int(move[1])
    elif move[0]=="down":
        # depth     +=int(move[1])
        aim+=int(move[1])
    elif move[0]=="up":
        # depth     -=int(move[1])
        aim       -=int(move[1])


result=horizontal*depth
print(result)

