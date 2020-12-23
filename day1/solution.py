import os
import itertools


def sumwithlist(n, li):
    for i in li:
        for j in li:
            if n+i+j == 2020:
                print(n, i, j, n+i+j, n*i*j)


def sumup(listnumbers):
    for i in range(0, len(listnumbers)):
        auxlst = listnumbers[0:i]+listnumbers[i+1::]
        sumwithlist(listnumbers[i], auxlst)
        #print(sum_result[0], sum_result[1])

#def genSublists:
    


f = open("input.txt").readlines()
numbso = []

for number in f:
    number_ax = int(number.replace("\n", ""))
    numbso.append(number_ax)

sumup(numbso)