
"""
Well, I have just learned about different traversal methods for binary trees,
which I did not know about before starting this problem. It is much easier
if you have knowledge. Using the fact that post-order traversal will visit
children before parents, we can just hit both children. As soon as we hit the
second (larger) child, we know we're about to hit parents. The first node
we hit after that will be the parent of both!
"""

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
    


def postOrderTraversal2(root,v1,v2,counter=1,pointer=None):
    # The goal is to count both children, and then immediately return whatever comes after them
    if root:
        (pointer,counter) = postOrderTraversal2(root.left,v1,v2,counter,pointer)
        (pointer,counter) = postOrderTraversal2(root.right,v1,v2,counter,pointer)
        
        # Check this first, so that we don't update and then check the same thing
        # If the counter is at 3, we've found our two child nodes already!
        # So we can quickly update the pointer and the counter.
        # This pointer is the pointer to the LCA
        if counter==3:
            pointer = root
            counter+=1
        
        # If we see one child, update the counter
        if root.info == v1:
            print("v1")
            counter+=1
        # If we see another child, update the counter
        if root.info == v2:
            print("v2")
            counter+=1
        
    return pointer, counter
        

def lca(root, v1, v2):

    res = postOrderTraversal2(root,v1,v2)
    
    # res gives the pointer and the counter
    # res[0] is the pointer, which is what we want to return
    
    return res[0]
    

tree = BinarySearchTree()



arr = [4, 2, 3, 1, 7, 6]
t = len(arr)

for i in range(t):
    tree.create(arr[i])

ans = lca(tree.root, 1, 7)
print (ans.info)
