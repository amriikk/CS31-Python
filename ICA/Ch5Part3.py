# Week 6, ICA 1
import random
# Let's play Plinko!!
def main():
total = 0
    for x in range(1,6):
        #random.seed(random.uniform(2.5,125.3))
        slot = random.randrange(1,10)
        amt = plinkToss(slot)
        print(f'Disk #{x}: You won ${amt} (slot = {slot})')
        total = total + amt
        
        
        
        

def plinkToss(slot):
    if slot == 1 or slot == 9:
        money = 100
    elif slot == 2 or slot == 8:
        money = 500
    elif slot == 3 or slot == 7:
        money == 1000
    elif slot == 5:
        money == 10000
    else: 
        moneyn = 0
    return money