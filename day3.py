with open('day3-input.txt') as f:
    lines = f.readlines()

input=[]
for line in lines:    
    input.append(line.rstrip())

# n0, n1 = 0, 0
# gamma=""
# epsilon=""
# for i in range(12):
#     for line in input:
#         if int(line[i])==0:
#             n0+=1
#         else:
#             n1+=1
#     if n1>n0:
#         gamma+="1"
#         epsilon+="0"
#     else:
#         gamma+="0"
#         epsilon+="1"
#     n1, n0 = 0, 0
# print(gamma, int(gamma,2))
# print(epsilon, int(epsilon,2))

# print(int(gamma,2)*int(epsilon,2))


n0, n1 = 0, 0
ogr, co2 = input.copy(), input.copy()
i1, i0 = [], []
for i in range(12):
    for j,line in enumerate(ogr):
        if int(line[i])==0:
            n0+=1
        else:
            n1+=1
    if n1>n0 or n1==n0:
        ogr=[item for item in ogr if int(item[i])==1]
    else:
         ogr=[item for item in ogr if int(item[i])==0]

    i0.clear()
    i1.clear()
    n1, n0 = 0, 0

for i in range(12):
    if len(co2)==1:
        break
    for j,line in enumerate(co2):
        if int(line[i])==0:
            n0+=1
        else:
            n1+=1
    if n1>n0 or n1==n0:
        co2=[item for item in co2 if int(item[i])==0]


    else:
        co2=[item for item in co2 if int(item[i])==1]

    n1, n0 = 0, 0

print(ogr)
print(co2)

print(int(ogr[0],2)*int(co2[0],2))