import itertools

preamble = open("day9/input.txt").read().splitlines()

#Part 1

def getError(arrayP, preamble):
    for i in range(0, len(preamble)):
        valor = 0
        n = 0
        while valor == 0:
            if n==len(arrayP):
                return preamble[i], i
            if preamble[i]-arrayP[n] in arrayP:
                #print(preamble[i]-n, n)
                arrayP.append(preamble[i])
                valor +=1
            else:
                n+=1


arrayP = preamble[:25]
arrayP = [int(i) for i in arrayP] 
preambleaux = preamble[25:]
preambleaux = [int(i) for i in preambleaux]

res = getError(arrayP, preambleaux)
print(res)
tIx = res[1]+25
searchArray = preamble[:tIx]
searchArray = [int(i) for i in searchArray]
print(searchArray[-1])

# MATCH THIS NUMBER:  104054607
# 532

for i,j in itertools.combinations(range(len(searchArray)+1),2):
    if sum(searchArray[i:j]) == res[0]:
        print(min(searchArray[i:j])+ max(searchArray[i:j]))
        break
    
