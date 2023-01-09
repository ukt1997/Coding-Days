class MyQueue:

    def __init__(self):
        self.queue = []
        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if len(self.queue) == 0:
            return -1
        elif len(self.queue) == 1:
            temp = self.queue[0]
            self.queue = []
            return temp
        else:
            temp = self.queue[0]
            self.queue = self.queue[1:]
            return temp
        

    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        if len(self.queue) >= 1:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()