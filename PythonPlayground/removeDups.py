# In this problem, I am attempting to remove duplicates from a linked list
# First, create the node structure
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
           
    # Code to insert a node somehwere (haven't checked this)
    def insertNode(self,data):
        temp = self.head
        insert = temp.next
        temp.next = Node(data)
        temp.next.next = insert
        
    # Code to append a node to the linked list 
    def appendNode(self,data):
        temp = self.head
        while temp.next!=None:
            temp = temp.next
        temp.next = Node(data)

            
# Create the Linked List
list = "FOLLOW UP"
llist = LinkedList()
llist.head = Node(list[0])
for i in range(1,len(list)):
    llist.appendNode(list[i])

# Now actually implement the algo

# We're going to use division % 10 to find indices for our hash table
num = 10

#Create the table (LL will be stored here)
hashTable = [None]*10

# Move to the first location on the linked list that we want
node = llist.head
i = 0
while node != None:
    h = node.data # Get the char
    loc = ord(h)%10 # This is where it'll be stored in the hash table
    
    # We will either have a linked list or "none" in the has table
    if hashTable[loc] == None: # There's no linked list in this location
        newll = LinkedList() # Initialize a linked list
        newll.head = Node(h) # Add data to the head
        hashTable[loc]=newll # Put the linked list in the hash table
    
        # If it's our first time through the loop, create our buffer
        # We know it's our first time encountering the char h
        if i ==0:
            noDups = LinkedList()
            noDups.head = Node(h)
        else: 
            noDups.appendNode(h)
        
    else: # This means a linked list exists here
        newll = hashTable[loc] # Pull out the linked list
        newllN = newll.head # Move to the first node in the linked list           
        while newllN!=None: # As long as we are in a place with data, perform the following:
            
            # Look for a match
            if newllN.data == h:
                break # We break now, before newllN == None. This allows us to append to noDups
            
            newllN = newllN.next # If we don't break, check the next entry in the linked list for a match (move forward)
        
        # If we did NOT find a match (IE, completed loop until newllN == None), append to noDups
        if newllN == None:
            noDups.appendNode(h)
        
        # Since we didn't find a match, we want to find one "next" time. So add the char to the hash table's linked list.
        newll.appendNode(h)
        
    # Move on to the next node in the original linked list
    node = node.next

        
    i+=1
    
# And now the result
print("NoDups")
noDups.printList()