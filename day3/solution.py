import os

def getObject(map, idx, idy):
    
    return map[idx][idy % len(map[idx])]

def getNextPosition(idx, idy, slopeX, slopeY):
    idx = idx + slopeX
    idy = idy + slopeY
    return idx, idy

tmap = open("input.txt").read().splitlines()
row = 0
col = 0

trees = 0
arbor=[]
slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]

for i in slopes:
    print(i)
    while row != len(tmap)-1:
        print(row)
        row, col = getNextPosition(row, col, i[0], i[1])
        if getObject(tmap, row, col) == "#":
            trees +=1  
    arbor.append(trees)
    row = 0
    col = 0
    trees = 0
print(arbor)
res = 1

for j in arbor:
    res = res* j

print(res)