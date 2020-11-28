# Databricks notebook source
#level order traversal need queue data structure
class Queue:
  def __init__(self):
    self.items = []
  
  def enqueue(self,key):
    self.items.append(key)
    
  def dequeue(self):
    if not self.is_empty():
      return self.items.pop(0)
  
  def peek(self):
    if not self.is_empty():
      return self.items[0].value
  def is_empty(self):
    return self.items == []
  
  def __len__(self):
    return self.size()
  
  def size(self):
    return len(self.items)
  
  def get_queue(self):
    return self.items
  
  

# COMMAND ----------

#for reverse order traversal
class stack:
  def __init__(self):
    self.items = []
  
  def push(self,key):
    self.items.append(key)
    
  def pop(self):
    return self.items.pop()
  
  def is_empty(self):
    return self.items == []
  
  def size(self):
    return len(self.items)
  
  def get_stack(self):
    return self.items
  
  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    
  def __iter__(self):
    return iter(self.items)
  
  def __len__(self):
    return self.size()
  
  def display(self):
    if not self.is_empty():
      for data in reserved(self.items):
        print(data)
  
  

# COMMAND ----------

class Node:
  def __init__(self,data):
    self.value = data
    self.left = None
    self.right = None
    
class BinaryTree:
  def __init__(self,root):
    self.root = Node(root)
    
  def print_tree(self,traversal_type):
    if traversal_type == 'preorder':
      return self.preorder_print(self.root,"")
    elif traversal_type == 'inorder':
      return self.inorder_print(self.root,"")
    elif traversal_type == 'postorder':
      return self.postorder_print(self.root,"")
    elif traversal_type == 'levelorder':
      return self.level_order_print(self.root,"")
    elif traversal_type == 'reverse levelorder':
      return self.reverse_order_print(self.root,"")
    
    
    
  def preorder_print(self,start,traversal):
    """right - left - right"""
    #1-2-4-5-3-6-7-
    if start:
      traversal += (str(start.value) + '-')
      traversal = self.preorder_print(start.left,traversal)
      traversal = self.preorder_print(start.right,traversal)
    return traversal
  
  def inorder_print(self,start,traversal):
    """left - root - right"""
    #4-2-5-1-6-3-7-
    if start:
      traversal = self.inorder_print(start.left,traversal)
      traversal += (str(start.value) + '-')
      traversal = self.inorder_print(start.right,traversal)
    return traversal
  
  def postorder_print(self,start,traversal):
    """left - right - root"""
    #4-5-2-6-7-3-1-
    if start:
      traversal = self.postorder_print(start.left,traversal)
      traversal = self.postorder_print(start.right,traversal)
      traversal += (str(start.value) + '-')
      
    return traversal
  
  def level_order_print(self,start,traversal):
    if start is None:
      return 
    queue = Queue()
    queue.enqueue(start)
    while len(queue) > 0:
      traversal += str(queue.peek()) + "-"
      node = queue.dequeue()
      if node.left:
        queue.enqueue(node.left)
      if node.right:
        queue.enqueue(node.right)  
    return  traversal   
        
      
  def reverse_order_print(self,start,traversal):
    if start is None:
      return None
    queue = Queue()
    s  = stack()
    queue.enqueue(start)
    while len(queue) > 0:
      node = queue.dequeue()
      s.push(node)
      if node.right:
        queue.enqueue(node.right)  
      if node.left:
        queue.enqueue(node.left)
    
    while not s.is_empty():
      node = s.pop()
      traversal += str(node.value) + "-"
      
    return traversal    
    
  def height_of_tree(self,node):
    if node is None:
      return -1
    left_height = self.height_of_tree(node.left)
    right_height = self.height_of_tree(node.right)
    
    return 1 + max(left_height,right_height)
  
  def size_of_tree(self,start):
    if start is None:
      return 0
    s = stack()
    s.push(start)
    count = 0
    while not s.is_empty():
      node = s.pop()
      count +=1 
      
      if node.left:
        s.push(node.left)
      if node.right:
        s.push(node.right)  
        
    return count    
  def recursive_size_of_tree(self,node):
    if node is None:
      return 0
    left = self.recursive_size_of_tree(node.left)
    right = self.recursive_size_of_tree(node.right)
    return 1 + left + right
    

# COMMAND ----------

tree = BinaryTree(1)
tree.root.left = Node(2) 
tree.root.right = Node(3) 
tree.root.left.left = Node(4) 
tree.root.left.right = Node(5) 
tree.root.right.left = Node(6) 
tree.root.right.right = Node(7) 
# tree.root.left.left.left = Node(8)
# tree.root.left.left.right = Node(9) 

print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
print(tree.print_tree('postorder'))
print(tree.print_tree('levelorder'))
print(tree.print_tree('reverse levelorder'))

# COMMAND ----------

#height of tree
print(tree.height_of_tree(tree.root))
print(tree.size_of_tree(tree.root))
print(tree.recursive_size_of_tree(tree.root))

# COMMAND ----------

# DBTITLE 1,BINARY SEARCH TREE 
class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
    
    
class BST:
  def __init__(self):
    self.root = None
    
  def insert(self,data):
    new_node = Node(data)
    if self.root is None:
      self.root = new_node
    else:
      self._insert(data,self.root)
      
  def _insert(self,data,cur_node):
    if data < cur_node.data:
      if cur_node.left is None:
        cur_node.left = Node(data)
      else:
        self._insert(data,cur_node.left)
    elif data > cur_node.data:
      if cur_node.right is None:
        cur_node.right = Node(data)
      else:
        self._insert(data,cur_node.right)
    else:
      print("Value is already present in tree")
      
  def find(self,data):
    if self.root:
      is_found = self._find(data,self.root)
      if is_found:
        return True
      return False
    else:
      return None
      
  def _find(self,data,cur_node):
    if data < cur_node.data and cur_node.left:
        return self._find(data,cur_node.left)
    elif data > cur_node.data and cur_node.right:
      return self._find(data,cur_node.right)
    
    if data == cur_node.data:
      return True
    
  def inorder_print_tree(self):
    if self.root:
      self._inorder(self.root)
      
  def _inorder(self,cur_node):
    if cur_node:
      self._inorder(cur_node.left)
      print(str(cur_node.data))
      self._inorder(cur_node.right)
      
  def is_bst(self):
    if self.root:
      is_satisfied = self._is_bst(self.root,self.root.data)
      if is_satisfied is None:
        return True
      return False
    return True
      
  def _is_bst(self,cur_node,data):
    if cur_node.left:
      if data > cur_node.left.data:
        return self._is_bst(cur_node.left,cur_node.left.data)
      else:
        return False
    if cur_node.right:
      if data < cur_node.right.data:
        return self._is_bst(cur_node.right,cur_node.right.data)
      else:
        return False
    
    

# COMMAND ----------

b = BST()
b.insert(5)
b.insert(1)
b.insert(3)
b.insert(9)
print(b.find(3))
b.inorder_print_tree()
print()
tree = BST()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.inorder_print_tree()

print(b.is_bst())
print(tree.is_bst())

# COMMAND ----------


