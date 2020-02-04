import numpy as np

def generate_money():
    dollar = np.random.randint(5,size=1)
    cents = np.random.randint(99,size=1)*0.01
    return dollar+cents

amount = generate_money()
#amount = 3.49

# Ordered from the largest to smallest coins. Quarter, dime, nickel, penny. In cents
coinvalues = [25,10,5,1]
coinnames = ['Quarters','Dimes','Nickels','Pennies']

def least_coins(amount, coinvalues,coinnames):
    amount = int(amount*100) #Apparently floats are awful so we're not using them anymore
    totalnumber = 0
    i=0
    for v in coinvalues:
        num_o_v = (amount//v)
        print('Number of '+coinnames[i]+' : '+str(num_o_v))
        amount = amount-num_o_v*v
        totalnumber +=num_o_v
        i+=1
    print('Total Number of Coins: '+str(totalnumber))
    return totalnumber

print('Dollar amount: '+str(amount))        
print()
least_coins(amount, coinvalues,coinnames)

#print(198-175)
    