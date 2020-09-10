"""
Given a string s repeated infinitely, count the number of occurences of a in the substring of length n
"""

def repeatedString(s, n):

    # How many times does a appear in the string s?
    # How many times can the sting s appear in the subset?
    # If truncated at the end, what part of the string s is NOT cut off?

    # Iterate thru the string s to count the occurences of a
    numAinS = 0
    for l in s:
        if l == "a":
            numAinS +=1
    
    print(numAinS)
    # Find out how many times the string can fit in the subset
    lens = len(s) 

    n = n*lens 

    #First, find the remainder
    r = n%lens

    # (the length of the substring - remainder)/(length of s) = # of times it fits
    numRep = (n-r)/lens

    print(numRep)
    # Use the remainer to cut short s and count the number of 'a's in the remainder
    smalls = s[:r] # r remaining letters in the string
    numAinS2 = 0
    for l in smalls:
        if l == "a":
            numAinS2 +=1
    
    print(numAinS2)
    # Now multiply numRep*numAinS and add the remaining 'a's found in numAinS2

    numATotal = numRep*numAinS+numAinS2

    return numATotal

# Hot damn my code is not concise compared to some other folx solutions!

if __name__ == '__main__':
    
    s = "aba"
    n = 10
    
    repeatedString(s,n)