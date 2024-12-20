import re
with open('day_3_input', 'r') as f:
    code = f.read()

mul_list = re.findall(r'do\(\)|don\'t\(\)|mul\(\d\d?\d?,\d\d?\d?\)', code)

enabled_muls = []
switch = True
for x in mul_list:
    if(x == "do()"):
        switch = True
        continue
    if(x == "don\'t()"):
        switch = False
        continue
    if(switch == True):
        enabled_muls.append(x)

sum = 0

for text in enabled_muls:
    mul_pair = re.findall(r'\((\d\d?\d?),(\d\d?\d?)\)', text)
    sum += int(mul_pair[0][0])*int(mul_pair[0][1])

print(sum)

    