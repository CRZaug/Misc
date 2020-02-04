import numpy as np

def generate_money():
    dollar = np.random.randint(5,size=1)
    cents = np.random.randint(99,size=1)*0.01
    return dollar+cents

amount = generate_money()
#amount = 3.49

# Ordered from the largest to smallest coins. Quarter, dime, nickel, penny.
coinvalues = [.25,.1,0.05,0.01]
coinnames = ['Quarters','Dimes','Nickels','Pennies']

def least_coins(amount, coinvalues,coinnames):
    totalnumber = 0
    i=0
    for v in coinvalues:
        num_o_v = (amount//v)
        print('Number of '+coinnames[i]+' : '+str(num_o_v))
        amount = amount-num_o_v*v
        totalnumber +=num_o_v
        i+=1
    return totalnumber

print('Dollar amount: '+str(amount))        
print()
print('Total Number of Coins:')
print(least_coins(amount, coinvalues,coinnames))

print(198-175)
    