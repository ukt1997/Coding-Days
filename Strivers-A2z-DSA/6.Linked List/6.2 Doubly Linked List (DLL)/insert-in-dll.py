# Q1 is just Revision -no Code

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''


# Function to insert a new node at given position in doubly linked list.
def addNode(head, p, data):
    # Code here
    start = 0
    while start < p:
        head = head.next
        start += 1
    new_node = Node(data)
    new_node.next = head.next
    new_node.prev = head
    if new_node.next is not None:
        new_node.next.prev = new_node
    head.next = new_node


# {
# Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data

        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, new_data):
        new_node = Node(new_data)
        if (self.head == None):
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        return

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = map(int, input().strip().split())
        llist = DoublyLinkedList()
        for e in arr:
            llist.add(e)

        pos, data = map(int, input().strip().split())

        addNode(llist.head, pos, data)
        llist.printList(llist.head)

# } Driver Code Ends