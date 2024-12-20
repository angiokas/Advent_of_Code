page_order_rules = []
updates = []

with open('day_5_input', 'r') as file:
    for row in file:
        if "|" in row:
            page_order_rules.append(row.strip().split("|"))
        if "," in row:
            updates.append(row.strip().split(","))

rules = {}

for rule in page_order_rules:
    if rule[1] not in rules:
        rules[rule[1]] = []
    rules[rule[1]].append(rule[0])

print(rules)
def check_update(update,rules):
    for i in range(len(update)):
        for y in update[i+1:]:
            x = update[i]
            if(y in rules[x]):
                return False
    return True              

correct_updates = []

for update in updates:
    if(check_update(update,rules)):
        correct_updates.append(update)

sum_middle_numbers = 0
for update in correct_updates:
    sum_middle_numbers += int(update[int((len(update)-1)//2)])

print(sum_middle_numbers)
