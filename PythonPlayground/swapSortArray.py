# Complete the minimumBribes function below.
def minimumBribes(q, moves, numSwapsDict):

    # This loop can handle everything execept the very first index
    for i in range(1,len(q)):
        # print(q)

        if q[i]<i+1:
            # Thus number q[i] is NOT in its proper place. Move it forwards
            temp = q[i-1]
            q[i-1]=q[i]
            q[i]=temp
            moves+=1
            
            # Track that we took a swap for this number in. It's the one that moved backwards, the one that did the bribing
            try:
    
                numSwapsDict[str(q[i])]+=1 # Attempt to add new move count
                if numSwapsDict[str(q[i])] >= 3:

                    return "Too chaotic"
            except KeyError:
                numSwapsDict[str(q[i])]=1 # If we can't, this key doesn't exist, so add it and up its count
    
   # If it is still not sorted, run the algorithm again.
    if q != sorted(q):
        moves = minimumBribes(q,moves,numSwapsDict)
    return moves
if __name__ == '__main__':
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    moves = 0
    numSwapsDict = {
    }
    moves = minimumBribes(q,moves,numSwapsDict)
    
    print(moves)