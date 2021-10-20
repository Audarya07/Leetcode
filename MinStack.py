class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.temp = []
        

    def push(self, x: int) -> None:
        self.data.append(x)
        if self.temp:
            self.temp.append(min(x,self.temp[-1]))
        else:
            self.temp.append(x)
            
    def pop(self) -> None:
        self.data.pop()
        self.temp.pop()

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        return self.temp[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
