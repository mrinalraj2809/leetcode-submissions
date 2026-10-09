class MinStack:

    def __init__(self):
        self.res = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.res.append(val)
        if len(self.minStack):
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)
        

    def pop(self) -> None:
        self.res.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:
        # return min(self.res)
        return self.minStack[-1]

