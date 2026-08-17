class MinStack:

    def __init__(self):
        self._stack: list = []

    
    def push(self, val: int) -> None:
        self._stack.append(val)
        
    def pop(self) -> None:
        if self._stack == []:
            raise RuntimeError("stack is empty")
        self._stack.pop()
        
    def top(self) -> int:
        if self._stack == []:
            raise RuntimeError("stack is empty")
        return self._stack[-1]
        
    def getMin(self) -> int:
        if self._stack == []:
            raise RuntimeError("stack is empty")
        return min(self._stack)    
        
