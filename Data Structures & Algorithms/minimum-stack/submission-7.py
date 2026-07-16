class MinStack:

    def __init__(self):
        self.res = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))
        self.res.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.res.pop()

    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
