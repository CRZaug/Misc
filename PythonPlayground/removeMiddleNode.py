# Code to remove any middle node in a linked list (NOT the first or last node, by construction)

class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
            
   
# Next, create the linked list class
class LinkedList: 
     
    # Function to initialize the Linked List Object
    def __init__(self):  
        self.head = None
        
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
            
        # Code to append a node to the linked list 
    def appendNode(self,data):
        temp = self.head
        while temp.next!=None:
            temp = temp.next
        temp.next = Node(data)
        
# Create the Linked List
list = "abcde"
llist = LinkedList()
llist.head = Node(list[0])
for i in range(1,len(list)):
    llist.appendNode(list[i])
    
    
toRemove = "b"

node = llist.head
while node.next != None:
    a = node
    b = a.next
    print(a.data,b.data)
    if b.data == toRemove:
        a.next = b.next
    node = a.next

print()
llist.printList()
    