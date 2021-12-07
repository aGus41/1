with open('day4-input.txt') as f:
    lines = f.readlines()

input=[]
for line in lines:    
    input.append(line.rstrip())

input= [x for x in input if x]

draw_numbers=input.pop(0).split(",")

tables = [input[x:x+5] for x in range(0, len(input), 5)]

for i in range(len(tables)):
    for j in range(len(tables[0])):
        tables[i][j]=tables[i][j].split(" ")
        tables[i][j]= [x for x in tables[i][j] if x] # String == "False" if empty       

def mark_drawn(table, drawn):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j]==drawn:
                table[i][j]=""

def check_rows(table):
    for i in range(len(table)):
        counter=0
        for j in range(len(table[0])):
            if not table[i][j]:
                counter+=1
            if counter==5:
                return True
    return False

def check_columns(table):
    for i in range(len(table)):
        counter=0
        for j in range(len(table[0])):
            if not table[j][i]:
                counter+=1
            if counter==5:
                return True
    return False

def sum_rest(table):
    counter=0
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j]:
                counter+=int(table[i][j])
    return counter

def part1():
    for num in draw_numbers:
        for table in tables:
            mark_drawn(table,num)
            if check_columns(table) or check_rows(table):
                print(int(num)*sum_rest(table))
                break
        else:
            continue
        break       

def part2():
    restart = True
    while restart:
        for num in draw_numbers:
            for i,table in enumerate(tables):
                mark_drawn(table,num)
                if check_columns(table) or check_rows(table):
                    if len(tables)==1:
                        restart=False
                        print(int(num)*sum_rest(table))
                    del tables[i]
                    # print(len(tables))
                    break
            else:
                continue  # only executed if the inner loop did NOT break
            break       # only executed if the inner loop DID break


if __name__ == "__main__":
    part1()
    part2()




