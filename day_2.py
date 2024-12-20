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
    
    if (all(asc_comparisons) or all(des_comparisons)):
        return True
    
    if (len(asc_comparisons)-sum(asc_comparisons)==1):
        i = asc_comparisons.index(False)
        if(i == 0 or i == len(report)-2):
            return True
        return asc_check(report[i],report[i+2])
    
    if (len(asc_comparisons)-sum(asc_comparisons)==2):
        i = asc_comparisons.index(False)
        if (asc_comparisons[i+1] == False):
            print(report)
            print(asc_comparisons)
            print(i)
            if(i==0):
                return asc_check(report[1],report[2]) or asc_check(report[0],report[2])
            return asc_check(report[i],report[i+2]) or asc_check(report[i-1],report[i+1])
        return False
    
    if (len(des_comparisons)-sum(des_comparisons)==1):
        i = des_comparisons.index(False)
        if(i == 0 or i == len(report)-2):
            return True
        return des_check(report[i],report[i+2]) or des_check(report[i-1],report[i+1])
        return False
    
    if (len(des_comparisons)-sum(des_comparisons)==2):
        i = des_comparisons.index(False)
        if (des_comparisons[i+1] == False):
            if(i ==0):
                return des_check(report[1],report[2]) or des_check(report[0],report[2])
            return des_check(report[i],report[i+2]) or des_check(report[i-1],report[i+1])
        return False
    return False

safe_reports_amount = 0

for report in levels:
    if(safety_check(report)):
        safe_reports_amount += 1

print(safe_reports_amount)