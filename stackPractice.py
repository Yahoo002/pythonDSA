class Stack:
  def __init__(self) -> None:
    self.stack = []

  def push(self, item):
    self.stack.append(item)
    print("Pushed item: " + item)
  
  def peek(self):
    if not self.is_empty():
      return self.stack[-1]
    else:
      return "Empty stack"
  
  def is_empty(self):
    return len(self.stack) == 0
  
  def pop(self):
    if self.is_empty():
      return "stack is empty"
    return self.stack.pop()

s = Stack()
s.push('h')
s.push('e')
s.push('l')
s.push('l')
s.push('o')


popped_item = s.pop()

print(s.stack)
print(popped_item)

print(s.stack)
print(s.peek())

# stack2 = []

# while(len(s.stack) != 0):
#   print(s.pop(s))
  
  