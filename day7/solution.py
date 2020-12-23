import os
import re

bags = open("day7/input.txt").read().splitlines()

# def getBags(bag):
#     if bag in bagsDicion.keys():
#         for parents in bagsDicion[bag]:
#             counter.add(parents)
#             getBags(parents)
#     return


# bagsDicion = {}
# for bag in bags:
#     information = re.split(r' (contain) ', bag)
#     parentBag = information[0].replace("bags", "bag")
#     bagsFound = information[2].replace(".", "")
#     bagsFound = bagsFound.split(", ")
#     for bagFound in bagsFound:
#         bagFound = bagFound.replace("bags", "bag")[2:]
#         if bagFound in bagsDicion:
#             bagsDicion[bagFound].append(parentBag)
#         else:
#             bagsDicion[bagFound] = [parentBag]



# counter = set()
# #print(bagsDicion["shiny gold bag"])
# getBags("shiny gold bag")
# print(len(counter))


# part 2
conta = 0
def sumBags(bag):
    for mala in bagsDicion2[bag]:
        if mala[0] == 0:
            return
        elif mala[1] in diciRes.keys():
            diciRes[mala[1]] += mala[0]
            for i in range(0,mala[0]):
                sumBags(mala[1])
        else:
            diciRes[mala[1]] = mala[0]
            for i in range(0,mala[0]):
                sumBags(mala[1])
         

bagsDicion2 = {}
for bag in bags:
    information = re.split(r' (contain) ', bag)
    parentBag = information[0].replace("bags", "bag")
    bagsFound = information[2].replace(".", "")
    bagsFound = bagsFound.split(", ")
    bagsDicion2[parentBag] = []
    for bagFound in bagsFound:
        if "no other bags" in bagFound:
            qty = 0
            bagFoundB = "NoBag"
        else:
            bagFoundB = bagFound.replace("bags", "bag")[2:]
            qty = int(bagFound.replace("bags", "bag")[0])
        bagsDicion2[parentBag].append((qty, bagFoundB))
    print(bagsDicion2[parentBag])

diciRes = {}
sumBags("shiny gold bag")
soma = 0
for k,v in diciRes.items():
    soma += v
    print(k,v)

print(soma)