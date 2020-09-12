
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
    

        

def postOrderTraversal2(root,v1,v2):
    res = []
    # pointer=None
    if root:
        res = postOrderTraversal2(root.left,v1,v2)
        res = res+ postOrderTraversal2(root.right,v1,v2)
        if root.info == v1:
            res.append(root)
        if root.info == v2:
            res.append(root)
        if len(res)==2:
            res.append(root)
            
    return res
        

def lca(root, v1, v2):

    res = postOrderTraversal2(root,v1,v2)
    
    # Nice! Now we have an array of pointers.
    # res[0] is the pointer to v1, the smaller number
    # res[1] is the pointer to v2, the larger number
    # res[2] is the pointer to the lowest common ancestor!
    
    # We also could have avoided using the array, but whatever for now.
    
    return res[2]
    

tree = BinarySearchTree()



arr = [4, 2, 3, 1, 7, 6]
t = len(arr)

for i in range(t):
    tree.create(arr[i])

ans = lca(tree.root, 1, 7)
print (ans.info)
