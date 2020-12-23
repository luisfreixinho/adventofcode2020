import os
import re

passports = open("input.txt").read().split("\n\n")


#allrules = re.compile(r'(byr:[0-9]{4})|(iyr:[0-9]{4})|(eyr:[0-9]{4})|(hgt:[0-9]{3}cm)|((hcl|ecl):#[0-9a-f]{6})|((ecl|hcl):[a-z]{3})|(pid:[0-9]+)|(cid:[0-9]{1,3})')

#allrules = re.compile(r'((byr|iyr|eyr):[0-9]{4})|(hgt:[0-9]{1,3}cm)|((ecl|hcl)(:[a-z]+|:#[0-9a-f]{6}))|(pid:[0-9]+)')
allentries = re.compile(r'(byr:(19[2-9][0-9])|(200[0-2]))|(iyr:(201[0-9]|2020))|(eyr:(202[0-9]|2030))|(hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in))|(hcl:#[a-f0-9]{6})|(ecl:(amb|blu|brn|gry|grn|hzl|oth))|(pid:[0-9]{9})')



valid = 0
for passport in passports:
    rules = len(re.findall(allentries, passport))
    #print(rules, passport)
    if rules == 7:
        valid+=1
        print(rules, passport)
        print()

print(valid)



