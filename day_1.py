list_1 = []
list_2 = []

with open('day_1_input.txt', 'r') as file:
    for row in file:
        entry = row.strip().split()
        list_1.append(int(entry[0]))
        list_2.append(int(entry[1]))

list_1.sort()
list_2.sort()

total_distance = 0
for (x,y) in zip(list_1,list_2):
    total_distance += abs(x-y)

print(total_distance)

similarity_score = 0

for x in list_1:
    similarity_score += x*list_2.count(x)

print(similarity_score)