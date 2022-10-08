# This is Q4 to find the length of 1D-LL
# Q5 is to search a Value in LL , Can be done in same way by Checking value for each node and return if found

# User function Template for python3

'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''


class Solution:

    # Function to count nodes of a linked list.
    def getCount(self, head_node):
        # code here
        if head_node is None:
            return 0
        elif head_node.next is None:
            return 1
        else:
            count = 1
            while head_node.next is not None:
                head_node = head_node.next
                count += 1

            return count


# {
# Driver Code Starts
# Initial Template for Python 3

import io
import sys


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # append at the end of the list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = self.tail.next


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))  # list containing nodes
        for x in nodes:
            node = Node(x)  # create a new node
            a.append(node)
        print(Solution().getCount(a.head))
# } Driver Code Ends