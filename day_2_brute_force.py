levels = []
with open('day_2_input', 'r') as file:
    for row in file:
        report = row.split()
        levels.append(report)

def asc_check(x,y):
    return 1<=int(y)-int(x)<=3

def des_check(x,y):
    return 1<=int(x)-int(y)<=3 

def safety_check(report): 
    asc_comparisons = [asc_check(x,y) for x,y in zip(report,report[1:])]
    des_comparisons = [des_check(x,y) for x,y in zip(report,report[1:])]

def safety_check(report): 
    asc_comparisons = [asc_check(x,y) for x,y in zip(report,report[1:])]
    des_comparisons = [des_check(x,y) for x,y in zip(report,report[1:])]
    
    if (all(asc_comparisons) or all(des_comparisons)):
        return True
    
def bruteforce_safety_check(report):
    asc_comparisons = [asc_check(x,y) for x,y in zip(report,report[1:])]
    des_comparisons = [des_check(x,y) for x,y in zip(report,report[1:])]
    if (all(asc_comparisons) or all(des_comparisons)):
        return True
    for x in report:
        new_report = [item for item in report if item != x]
        if(safety_check(new_report)):
            return True
    for x in report:
        new_report = [item for item in report if item != x]
        if(safety_check(new_report)):
            return True
    return False

safe_reports_amount = 0

for report in levels:
    if(bruteforce_safety_check(report)):
        safe_reports_amount += 1

print(safe_reports_amount)