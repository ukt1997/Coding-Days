# https://www.hackerrank.com/challenges/is-binary-search-tree/problem

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def in_order(node ,Li):
    if node.left is not None:
        in_order(node.left,Li)
    Li.append(node.data)
    if node.right is not None:
        in_order(node.right,Li)
    return
        
def check_binary_search_tree_(root):
    Li = []
    in_order(root,Li)
    #print(Li)
    for i in range(len(Li) - 1):
        if Li[i] >= Li[i+1]:
            return False
    return True
    