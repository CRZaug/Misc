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
        
    def __repr__(self):
        
        nodes = []
        
        node = self.head
        
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        
        nodes.append("None")
        
        return " -> ".join(nodes)
        
    def __iter__(self):
        
        node = self.head
        
        while node is not None:
            yield node
            node = node.next
    
    def insertFirst(self,node):
        node.next = self.head
        self.head = node
        
    def insertLast(self,node):
        
        temp = self.head
        
        while temp.next is not None:
            
            temp=temp.next
            
        temp.next = node
        
    def insertBefore(self,newNode,oldNodeData):
        
        temp = self.head
        
        while temp.next.data is not oldNodeData:
            temp=temp.next
        
        temp2 = temp.next 
        
        temp.next = newNode
        
        newNode.next = temp2
        
        print(temp.data)
        
    def insertAfter(self,newNode,oldNodeData):
        temp = self.head
        
        while temp.data is not oldNodeData:
            temp=temp.next
        
        temp2 = temp.next 
        
        temp.next = newNode
        
        newNode.next = temp2
        
        print(temp.data)
        
    def removeNode(self,nodeData):
        
        temp = self.head
        
        while temp.next.data is not nodeData:
            temp=temp.next
            
        
        temp.next = temp.next.next
    


llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node("new")
seventh = Node("second new")



llist.head.next = second
second.next = third

llist.insertFirst(fourth)


    
llist.insertLast(fifth)


llist.insertBefore(sixth,2)
llist.insertAfter(seventh,5)

llist.removeNode(3)

print(llist)
    