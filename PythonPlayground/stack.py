# Implement a stack in Python by hand, even though it's not really necessary since arrays do all these things for you.
class StackNode:
	def __init__(self,data):
		self.data = data
		self.next = StackNode	

class Stack:

	def __init__(self):
		self.top = StackNode(None)
	
	def isEmpty(self,top):
		if self.top.data == None:
			return True
	
	def push(self,item):
		self.temp = StackNode(item)
		self.temp.next = self.top
		self.top = self.temp

	def pop(self):
		if self.isEmpty(self.top) == True:
			return False

		else:
			item = self.top.data
			self.top =self.top.next 
			return item

	def peek(self):
		if self.isEmpty(self.top)==True:
			return False
		else:
			return self.top.data

	

stack = Stack()
print(stack.peek())
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
stack.push(5)





print("stack")

while stack.peek() !=False:
	print(stack.pop())
