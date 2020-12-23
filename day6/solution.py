import os

anss = open("day6\input.txt").read()

groups = anss.split("\n\n")
# val = 0
# for group in groups:
#     group = group.replace("\n","").replace(" ","")
#     val += len(list(set(group)))
#     break
# print(val)

def getReap(group):
    count = 0
    letters = []

    group = [x for x in group if x]

    for letter in min(group, key=len):
        letC = 0
        for ppl in group:
            if letter in ppl:
                letC +=1 
        if letC == len(group):
            count +=1
            letters.append(letter)
    print(count, letters, group)
    return count

totalsum = 0
for group in groups:
    group = group.split("\n")
    #print(group)
    totalsum += (getReap(group))
    
print(totalsum)