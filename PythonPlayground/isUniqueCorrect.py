
# This alogrithm has complexity O(N), which is better than my original implementation. However, it does require an additional data structure.

def isUnique(s):
	l = len(s)

	# There are ways to do this that don't require dynamically updating arrays. This requires using facts about ASCII, like the one below.)
	charArray = []
	
	# Apparently there are only 128 unique ASCII characters, so any more characters than that and it is not unique.
	if l > 128: return False

	for i in range(l):
		if s[i] in charArray:
			return False
		else:
			charArray.append(s[i])
	return True

def isUniqueNLogN(s):
	sSorted = sorted(s)
	
	for i in range(1,len(sSorted)-1):
		if (sSorted[i]== sSorted[i-1]) or (sSorted[i]== sSorted[i+1]):
			# This is not a unique string
			return False
	return True 
	


def main():
	s = input()
	print(isUnique(s))
	print(isUniqueNLogN(s))

if __name__=="__main__":
	main()
