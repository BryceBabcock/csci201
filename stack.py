class StackEmptyError(Exception):
    def __init__(self, message = 'The stack is empty.'):
        super().__init__(message)

class Stack:
    def __init__(self):
        self._items = []
        
    def push(self, item):
        """Push an item onto the stack."""
        
        self._items.append(item)
        
    def pop(self):
        """Pop the item on top of the stack."""
        
        if len(self._items) == 0:
            raise StackEmptyError
            
        return self._items.pop()
        
    def peek(self):
        """Return the item on top of the stack but do not pop it."""
        
        if len(self._items) == 0:
            raise StackEmptyError
            
        return self._items[-1]
        
    def __len__(self):
        """Return the number of items in the stack."""
        
        return len(self._items)
        
    def isEmpty(self):
        """Return True if the stack is empty; False otherwise."""
        
        return len(self._items) == 0
        
    def __str__(self):
        stackStr = ''
        for item in reversed(self._items):
            stackStr += str(item) + '\n'
        return stackStr[:-1]                # remove last newline
