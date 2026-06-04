class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        mini = float('inf')

        if (len(self.minStack) > 0):
            mini = self.minStack[-1]

        if (val <= mini):
            self.minStack.append(val)


    def pop(self) -> None:
        num = self.stack.pop()
        if (len(self.minStack) > 0):
            if (num == self.minStack[-1]):
                self.minStack.pop()


    def top(self) -> int:
        if (len(self.stack) > 0): return self.stack[-1]
        else: None

    def getMin(self) -> int:
        if len(self.minStack) > 0: return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()