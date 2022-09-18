# https://www.hackerrank.com/challenges/tree-level-order-traversal/copy-from/232746663

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

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
        
def levelOrder(root):
    #Write your code here
    qu = []
    if root is not None:
        qu.append(root)
    while len(qu) > 0:
        node = qu.pop(0)
        print(node.info,end = " ")
        if node.left is not None:
            qu.append(node.left)
        if node.right is not None:
            qu.append(node.right)
    
    

