# Node class 
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 
   
# Linked List class 
class LinkedList: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
        
    def printList(self):
        temp = self.head
        while (temp):
            if temp.data == 1:
                insert = temp.next
                temp.next = Node(100)
                temp.next.next = insert
                
            print (temp.data)
            temp = temp.next
        


llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

llist.printList()
    
    

    