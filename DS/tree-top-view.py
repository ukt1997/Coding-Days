# https://www.hackerrank.com/challenges/tree-top-view/problem 

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
def find_list(root,l,h,m):
    # h : Height (Depth)
    # l : Horizontal Postion of Node when we see it from Top 
    if root is None:
        return

    if l not in m:
        # if No Node is Present at this Horizontal Position , Add it 
        m[l] = [root.info,h]
    elif m[l][1] > h:
        # if already node is present at That Position , Keep the one with less Depth as it will be viewd from Top  
        m[l] = [root.info,h]
    find_list(root.left,l-1,h+1,m)
    find_list(root.right,l+1,h+1,m) 
        
    

def topView(root):
    #Write your code here
    if root is None:
        return
    m = {}
    find_list(root,0,0,m)
    for it in sorted(m.keys()):
        print(m[it][0],end = " ")
        
# 1 2 4 14 23 37 108 111 115 116 83 84 85 

