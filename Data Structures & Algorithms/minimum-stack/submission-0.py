class MinStack:
    def __init__(self) -> None:
        #store all elements in a stack
        self.stack = []
        self.min_stack = [float('inf')]  
    def push(self, val: int) -> None:
  
        self.stack.append(val)
        # Keep track of minimum by comparing with current minimum
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        #remove element from stack and pop
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        #get top element without removing it
        return self.stack[-1]

    def getMin(self) -> int:
        #get minimum element with O(1) time
        return self.min_stack[-1]