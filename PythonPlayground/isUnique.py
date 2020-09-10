# This algorithm has O(N^2) runtime.

def isUnique(s):

	l = len(s)
	if l ==0:
		unique = True
	elif l==1:
		unique = True
	else:
		unique = True
		# The complicated case
		for i in range(l):
			for j in range(i+1,l):
				if s[i]==s[j]:
					unique = False
					break

	return unique

def main():
	s = "mystring"
	print(isUnique(s))

if __name__=="__main__":
	main()

