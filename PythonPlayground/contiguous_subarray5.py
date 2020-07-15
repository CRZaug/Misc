import numpy as np

# Create an array of integers
testsize = 10 # Number of integers to include
signcheat = np.random.randint(2,size=testsize)
array = np.random.randint(20,size=testsize)

for i in range(testsize):
    if signcheat[i]==1:
        array[i]=array[i]*-1 # Couldn't remember how to do rand sign on the plane not changing it now
 
print(array)
print()

# T will be an array of the largest contiguous sum possible ending at element array[i]
T = np.zeros(testsize) # Initialize an empty array to store max data in

# The first element of the array T is the first value of our test array because that has to be the max
T[0] = array[0]

# Initialize the indices so we can report the subarray with the max sum
firstindex = 0
indexarray =np.zeros((2,testsize),dtype = int)

for i in range(testsize-1):
    i = i+1
    # Find the max subarray ending in index i
    T[i] = max(T[i-1]+array[i],array[i]) # Recursion relation! 

    # Correct the indices accordingly
    if T[i-1]+array[i]>array[i]:
        secondindex = i+1
    else:
        firstindex = i
        secondindex = i+1
    indexarray[0,i]=firstindex
    indexarray[1,i]=secondindex


# T[i] is supposed to be the largest sum of for an array ending with array[i]
# So if we take max(T[i]), we should get the max result for the whole array.
# Then pull the correct indices from indexarray and report the subarray

# The max possible sum for our array
result = max(T) 
index = np.where(T==result)[0][0] # Where it occurs

subresult = indexarray[:,index] # Pull the indices

print(result,array[subresult[0]:subresult[1]])



"""
Lessons learned:
1. Don't stay up too late coding; it's not actually productive!
2. Listen to intuition
3. Explore different forms of solutions
4. Start with the brute force method, examine its flaws, determine how to improve it
"""
