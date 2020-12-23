import os
import re
seats = open("input.txt").read().splitlines()

#rules = re.compile(r'^[FB]^^')

Avseats = list(range(0,128))
Steps = list(range(0,8))
# print(seats)
# ln = int(len(seats)/2)
# print(ln)
# seats = seats[:ln]
# print(seats)

def decode(seat, allSeats):
    if len(seat)>0:
        hf = int(len(allSeats)/2)
        if seat[0] == "F" or seat[0] == "L":
            return decode(seat[1:], allSeats[:hf])
        elif seat[0] == "B" or seat[0] == "R":
            return decode(seat[1:], allSeats[hf:])
    else:
        return allSeats
        


#decode("FBFBBFF", Avseats)
maxi = 0
alSeats = []
for seat in seats:
    row = decode(seat[:7], Avseats)[0]
    column = decode(seat[-3:], Steps)[0]
    val = row * 8 + column
    alSeats.append(val)
    if val > maxi:
        maxi = val

print(maxi)
for el in range(0, len(alSeats)):
    if sorted(alSeats)[el+1] != sorted(alSeats)[el]+1:
        print(sorted(alSeats)[el]+1)
        break
