### Define a queue data structure
"""
Methods:
    1. add (a specific item)
    2. remove: return the top of the queue and remove it
    3. peek: 
    4. isEmpty
"""

# Create a node
class Node:
    
    def __init__(self):
        self.data = None
        self.next = None


class Queue:
    
    def __init__(self):
        self.head = Node() # The first item in the queue
        self.tail = Node() # The last item in the queue
    
    def isEmpty(self):
        if self.head.data == None:
            return True
        else:
            return False
    
    def add(self,item):
        # Add the head if this is the first thing in the list
        if self.isEmpty():
            self.head.data = item
            self.head.next = self.tail
            
        # Add to the tail, keep the last item named tail
        else:
            self.tail.data = item
            self.tail.next = Node()
            
            self.tail = self.tail.next
    
    def peek(self):
        if self.isEmpty() == False:
            return self.head.data
        else:
            raise ValueError("Empty queue")
        
    def remove(self):
        # Change the head to move up one, removing the old head
        if self.isEmpty() == False:
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            raise ValueError("Empty queue")
        
        
    def printAll(self):
        temp = self.head
        while temp.next !=None:
            print(temp.data)
            temp = temp.next
    
    

