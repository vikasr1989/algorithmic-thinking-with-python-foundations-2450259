doors = [False] * 100
#print (doors)
list = []
#for i in range(0,100):
#    doors[i] = not doors[i]
#print(doors)

for i in range(0,100):
    for j in range(0,100,i+1):
        doors[j] = not doors[j]
print(doors)
for i in range(0,100):
    if doors[i] == True:
        list.append(i)
print(list)