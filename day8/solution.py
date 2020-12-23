import os




instructions = open("day8/input.txt").read().splitlines()
#print(instructions)

#part 1

#diciVisit = {}


# accValue = 0
# i = 0

# while 1:
#     instruction = instructions[i].split(" ")
#     print(i)
#     if i in diciVisit.keys():
#         print(accValue)
#         break
#     else:
#         diciVisit[i] = True   
#     if "jmp" in instruction[0]:
#         print("here")
#         i = i + int(instruction[1])
#         print("i", i)
#     elif "acc" in instruction[0]:
#         accValue += int(instruction[1])
#         i +=1
#     elif "nop" in instruction[0]:
#         i +=1
#         continue




#part 2
def auxLoop(i, accValue, auxDic, instruction, ml):
    trig = 0
    
    while i != ml+1:
        if trig == 0:
            instruction = instruction.split(" ")
            trig = 1
        else:
            instruction = instructions[i].split(" ")


        if i in auxDic.keys():
            return False
        else:
            auxDic[i] = True 

        if "acc" in instruction[0]:
            accValue += int(instruction[1])
            if i == ml:
                return accValue
            i +=1
            
        elif "nop" in instruction[0]:
            if i == ml:
                return accValue
            i +=1
            continue

        elif "jmp" in instruction[0]:
            if i == ml:
                return accValue
            i = i + int(instruction[1])
            
    return accValue



i = 0
accValue = 0
diciVisit = {}

while i != len(instructions)-1:
    instruction = instructions[i].split(" ")

    

    if "acc" in instruction[0]:
        diciVisit[i]=True
        accValue += int(instruction[1])
        i +=1
    elif "nop" in instruction[0]:
        auxDic = diciVisit.copy()
        res = auxLoop(i, accValue, auxDic, "jmp "+instruction[1], len(instructions)-1)
        if res != False:
            print("RESULTADO", res)
            break
        diciVisit[i]=True
        i +=1
        continue
    elif "jmp" in instruction[0]:
        auxDic = diciVisit.copy()
        res = auxLoop(i, accValue, auxDic, "nop "+instruction[1], len(instructions)-1)
        if res != False:
            print("RESULTADO", res)
            break
        diciVisit[i]=True
        i = i + int(instruction[1])
        print("i", i)

print(accValue)