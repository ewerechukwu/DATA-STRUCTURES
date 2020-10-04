STACK
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class Stack:
  class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space()==True:
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
    # Increment stack size by 1 here:
      self.size+=1
    else:
      print("All out of space!")
      return None

  def pop(self):
    if self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
  
  def peek(self):
    if self.is_empty:
      return self.top_item.get_value()
    else:
      print("Nothing to see here!")
      
  # Define has_space() and is_empty() below:
  def has_space(self):
    if self.limit>self.size:
      return True
  def is_empty(self):
    if self.size==0:
      return True
