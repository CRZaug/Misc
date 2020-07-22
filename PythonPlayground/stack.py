# Implement a stack in Python by hand, even though it's not really necessary since arrays do all these things for you.

class Stack():

	def __init__(self):
		self.stack = []
	
	def isEmpty(self,stack):
		if len(self.stack) == 0:
			return True
	
	def push(self,item):
		self.stack.append(item)
		return self.stack

	def pop(self):
		if self.isEmpty(self.stack) == True:
			return -Inf
		else:
			item = self.stack[-1]
			self.stack = self.stack[:-1]
		return item 

	def peek(self):
		
		return self.stack[-1]

	

stack = Stack()

print(stack.stack)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.stack)

print()

print(stack.peek())
print(stack.pop())
print(stack.stack)



