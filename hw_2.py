import random

def mine (metal_name):
    copper_chance=random.random()
    iron_chance=random.random()
    if metal_name=="iron":
            if iron_chance<=0.2:
                return 1
    elif metal_name=="copper":
            if copper_chance<=0.5:
                return 1
    return 0

def simulate(max_day, iron_worker, copper_worker):
    iron_counter=0
    copper_counter=0
    alloy_counter=0
    total_profit=0
    for days in range(max_day):
        for iron_worker_number in range(iron_worker):
            iron_counter+=mine("iron")  
        for copper_worker_number in range(copper_worker):
            copper_counter+=mine("copper")
        if iron_counter>=3 and copper_counter >=3:
            alloy_counter+=1
            iron_counter-=3
            copper_counter-=3
            total_profit+=13
        if iron_counter+copper_counter>10:
            if iron_counter>=5:
                iron_counter-=5
                total_profit+=5*1
            if copper_counter>=5:
                copper_counter-=5
                total_profit+=5*0.5
    total_profit+=(copper_counter*0.5)+(iron_counter*1)
    return total_profit

def estimateProfit(n, max_day, iron_worker, copper_worker):
    profit_per_year=0
    for sim in range(n):
        profit_per_year+=simulate(max_day, iron_worker, copper_worker)
    return profit_per_year/n

print("Iron Worker: 1, Copper Worker: 4, Profit:",estimateProfit(1000,365,1,4))
print("Iron Worker: 2, Copper Worker: 3, Profit:",estimateProfit(1000,365,2,3))
print("Iron Worker: 3, Copper Worker: 2, Profit:",estimateProfit(1000,365,3,2))
print("Iron Worker: 4, Copper Worker: 1, Profit:",estimateProfit(1000,365,4,1))


