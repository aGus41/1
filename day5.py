# --- Day 5: Hydrothermal Venture ---
# You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

# They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

# An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
# An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

# So, the horizontal and vertical lines from the above list would produce the following diagram:

# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....
# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

# Your puzzle answer was 6113.

# --- Part Two ---
# Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

# Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

# An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
# An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# Considering all lines from the above example would now produce the following diagram:

# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....
# You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

# Consider all of the lines. At how many points do at least two lines overlap?

# Your puzzle answer was 20373.

# Both parts of this puzzle are complete! They provide two gold stars: **



from pandas import DataFrame

def is_horizontal(move):
    if move[0][1] == move[1][1]:
        return True
    else:
        return False

def is_vertical(move):
    if move[0][0] == move[1][0]:
        return True
    else:
        return False

def is_diagonal(move):
    if ((move[0][0] == move[0][1] and move[1][0] == move[0][1]) 
        or (move[0][0]==move[1][1] and move[0][1]==move[1][0])):
        return True
    else:
        return False

def format_move(move):
    copy=move.split(" -> ")
    copy[0]=copy[0].split(",")
    copy[1]=copy[1].split(",")
    return copy

def write_horizontal(move):
    x1=int(move[0][0])
    x2=int(move[1][0])
    y=int(move[0][1])
    if x1 < x2:
        for i in range(x1, x2+1):
            diagram[y][i] += 1
    else:
        for i in range(x1, x2-1, -1):
            diagram[y][i] += 1

def write_vertical(move):
    y1=int(move[0][1])
    y2=int(move[1][1])
    x=int(move[0][0])
    if y1 < y2:
        for i in range(y1, y2+1):
            diagram[i][x] += 1
    else:
        for i in range(y1, y2-1, -1):
            diagram[i][x] += 1

def write_diagonal(move):
    y1=int(move[0][1])
    y2=int(move[1][1])
    x1=int(move[0][0])
    x2=int(move[1][0])
    diff=abs(x1-x2)

    if (x2>x1 and y2>y1) or (x1>x2 and y1>y2) :
        for i in range(diff+1):
            diagram[min(y1,y2)+i][min(x1,x2)+i]+=1

    else:
        for i in range(diff+1):
            diagram[max(y1,y2)-i][min(x1,x2)+i]+=1
    
if __name__ == '__main__':
    with open('day5-input.txt') as f:
        lines=f.readlines()

    # with open('day5test-input.txt') as f:
    #     lines = f.readlines()

    input=[]
    for line in lines:
        input.append(line.rstrip())

    ex_hor='0,6 -> 5,6'
    ex_ver='2,0 -> 2,2'

    diagram=[[0 for y in range(1000)] for x in range(1000)]
    # diagram=[[0 for y in range(10)] for x in range(10)]
    for move in input:
        cpy=format_move(move)
        if is_vertical(cpy):
            write_vertical(cpy)
        elif is_horizontal(cpy):
            write_horizontal(cpy)
        else:
            write_diagonal(cpy)
    counter=0
    for x in range(len(diagram)):
        for y in range(len(diagram[0])):
            if diagram[y][x] > 1:
                counter += 1

    print(DataFrame(diagram))
    print(counter)
