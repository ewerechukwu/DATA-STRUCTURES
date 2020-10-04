class Stack:

    def __init__(self):
        self.stack = []

    def add(self, value):
# Use list append method to add element
        if value not in self.stack:
            self.stack.append(value)
            return True
        else:
            return False
# Use peek to look at the top of the stack

    def peek(self):     
	    return self.stack[-1]

# Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

