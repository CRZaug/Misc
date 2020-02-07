"""
Pretty sure this code is not correct because it just seems like it shouldn't be.

    Why I am worried: I don't like the part where I sum the result+remainder (see below)
    Can't justify why that wouldn't cause a problem somewhere

*** General idea: ***

Choose your monetary system. For example, 6c, 5c, and 1c coin (this always assumes a 1c coin exists)
Choose an amount. For example, 16

Perform two operations:
    Find amount%coin for each coin
    Find the number of times coin goes into amount
    
Sum the result. Whatever coin results in the smallest sum of that result, subtract from amount

Repeat until you're down in the 1c range.

Return value: ([number of coin 1, number of coin 2, number of coin 3,...], total number of coins)

---------------------

This was the test case my original code broke on. But it works here.

So on what case will this code break?
    - apparently this will break (sometimes) if amount<max(coin). For example: amount = 8
    - this breaks if all remainders = the number of 1c coins too

And is there an easier way...?

"""
import numpy as np


def generate_money():
    return np.random.randint(10,size=1)[0]


# Create our money
amount = generate_money()

# Ordered from the largest to smallest coins. Quarter, dime, nickel, penny. In cents
coinvalues = [12,6,5,3,1]


def least_coins(amount, coinvalues):
    print('amount',amount)
    print()
    
    total_coins = [0]*len(coinvalues)
    #amount =8 ############### It breaks on this case
    
    # I could add a case to correct for this. Maybe.
    #    If all the amount//coin is the same as another coin then use that other coin.
    #    But I don't like how specific that sounds; I want to believe there is a more general way
    #    Because what if it's a multiple of another coin or something instead?
    #    This was indeed my concern from the beginning in a slightly different form so at least my intuition isn't totally wrong :P
    while amount>0:

        modvect = []
        numbervect = []
        for v in range(len(coinvalues)):
            coin = coinvalues[v]
            m = amount%coin # find the remainder
            n = amount//coin # find the number of times coin goes into amount: N
            modvect.append(m)
            numbervect.append(n)
        
        print(modvect)
        print(numbervect)
        
        
        sum_vect = [modvect[i]+numbervect[i] for i in range(len(modvect))] # sum the remainder and N
        print(sum_vect)
        print()

        mmm = min(sum_vect) # find the min
        
        # I'm not really sure what's going on here and it's getting too late to fix it
        # Seems like in the case that we need to add a 1 there are problems?
        # This suggests I need to deal with the last step more carefully
        # If we find that the min is 1, we've found an exact match at 1.
        # As of like 10 runs things are functioning, so there's prob just a way to make this cleaner?
        if mmm!=1:
            ind = sum_vect.index(mmm) # find what coin caused the min, aka what coin wins
            amount -= coinvalues[ind] # Subtract out that coin
            total_coins[ind] +=1 # Up the counter for the coin that wins
        else:
            modmin = min(modvect)
            modind = modvect.index(modmin)
            total_coins[modind] +=1 # In this case, we found the exact match
            amount -=coinvalues[modind] # subtract out the last coin
        
    # Sum them all
    stc = sum(total_coins)
    
    return (total_coins,stc)
        
        
    
print()
print('coins',least_coins(amount, coinvalues))

"""
Lessons learned:
1. Apparently I know more numpy than python. Adding arrays in Python concats them
2. You can do this to get an array of n zeros: [0]*n
3. I should review Python basics
"""
    