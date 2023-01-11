class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val,val))
        else:
            self.stack.append((val,min(val,self.stack[-1][1])))

    def pop(self) -> None:
        if len(self.stack) > 0:
            temp = self.stack[-1]
            self.stack = self.stack[:-1]
            return temp[0]
        else:
            return -1
            

    def top(self) -> int:
        if len(self.stack) > 0:
            temp = self.stack[-1]
            return temp[0]
        else:
            return -1

    def getMin(self) -> int:
        if len(self.stack) > 0:
            temp = self.stack[-1]
            return temp[1]
        else:
            return inf


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()