class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.minTable = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (not self.min or self.min >= val):
            self.min = val
            self.minTable.append(val)


    def pop(self) -> None:
        num = self.stack.pop()
        if (num == self.minTable[-1]):
            self.minTable.pop()


    def top(self) -> int:
        if (len(self.stack) > 0): return self.stack[-1]
        else: return []

    def getMin(self) -> int:
        return self.minTable[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()