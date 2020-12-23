import os
import re


def verPW(minR, maxR, charR, passR, pw):
    #countR = passR.count(charR)
    # if countR>= minR and countR <= maxR:
    #     return True
    passR = passR + "-"*30
    if (passR[minR-1] == charR or passR[maxR-1]==charR) and passR[minR-1] != passR[maxR-1] :
        print(pw + " True", charR,passR[minR-1], passR[maxR-1] )
        return True
    else:
        print(pw + " False", passR[minR-1], passR[maxR-1])
        return False

passwords = open("input.txt").read().splitlines()
valid = 0
for password in passwords:
    rules = re.compile(r'([0-9]{1,2})-([0-9]{1,2}) ([a-z]): ([a-zA-Z0-9]+)')
    res = rules.search(password)
    if verPW(int(res.group(1)),int(res.group(2)),res.group(3),res.group(4), password):
        valid+=1

print(valid)

