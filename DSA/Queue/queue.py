# Databricks notebook source
# DBTITLE 1,QUEUE
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
      return self.items[0]
  def is_empty(self):
    return self.items == []
  
  def get_queue(self):
    return self.items
  
  

# COMMAND ----------

q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.dequeue()
q.get_queue()
q.enqueue("E")
q.enqueue("F")
q.dequeue()
q.get_queue()

# COMMAND ----------

# DBTITLE 1,Python Program to Implement Dequeue 
#The program creates a dequeue and allows the user to perform append and pop operations on it from both sides

class Dequeue:
  def __init__(self):
    self.items = []
    
  def append_right(self,key):
    self.items.append(key)
    
  def append_left(self,key):
    self.items.insert(0,key)
    
  def pop_left(self):
    if not self.is_empty():
      return self.items.pop(0)
  
  def pop_right(self):
    if not self.is_empty():
      return self.items.pop()
  
  def is_empty(self):
    return self.items == []
  
  def get_dequeue(self):
    return self.items

# COMMAND ----------

d = Dequeue()
d.append_left("A")
d.append_left("B")
d.append_left("C")
d.append_left("D")
d.pop_right()
d.pop_left()
print(d.get_dequeue())
d.append_left("E")
d.append_right("F")
print(d.get_dequeue())

# COMMAND ----------

# DBTITLE 1,Python Program to Implement Stack using One Queue
class stack:
  def __init__(self):
    self.q = Queue1()
    
  def push(self,key):
    self.q.enqueue(key)
    
  def pop(self):
    for _ in range(self.q.get_size() - 1):
      dequeue = self.q.dequeue()
      self.push(dequeue)
    return self.q.dequeue()
  
  def is_empty(self):
    return self.q.empty()
  
  def get(self):
    return self.q.items
    
class Queue1:
  def __init__(self):
    self.items = []
    self.size = 0
    
  def enqueue(self,key):
    self.size +=1
    self.items.append(key)
    
  def dequeue(self):
    self.size -=1
    return self.items.pop(0)
  
  def empty(self):
    return self.items == []
  
  def get(self):
    return self.items
  
  def get_size(self):
    return self.size

# COMMAND ----------

s = stack()

s.push("A")
s.push("B")
s.push("C")
s.push("D")

s.pop()
print(s.get())
s.push("E")
s.push("F")

s.pop()
print(s.get())

# COMMAND ----------

# DBTITLE 1,Python Program to Implement Stack Using Two Queues
# class Stack:
#     def __init__(self):
#         self.queue1 = Queue()
#         self.queue2 = Queue()
 
#     def is_empty(self):
#         return self.queue2.is_empty()
 
#     def push(self, data):
#         self.queue1.enqueue(data)
#         while not self.queue2.is_empty():
#             x = self.queue2.dequeue()
#             print("x",x)
#             self.queue1.enqueue(x)
#         self.queue1, self.queue2 = self.queue2, self.queue1
 
#     def pop(self):
#         return self.queue2.dequeue()
 
class stack:
  def __init__(self):
    self.queue1 = Queue()
    self.queue2 = Queue()
    
  def push(self,data):
    self.queue1.enqueue(data)
    while not self.queue2.is_empty():
      x = self.queue2.dequeue()
      print("X",x)
      self.queue1.enqueue(x)
    self.queue1,self.queue2 = self.queue2, self.queue1
    
  def pop(self):
    self.queue2.dequeue()
    
  def empty(self):
    return self.queue2.is_empty()
  
  def get(self):
    return self.queue2.get_queue()
  def print(self):
    print("1",self.queue1.get_queue())
    print("2",self.queue2.get_queue())

# COMMAND ----------


s = stack()

s.push("A")
s.push("B")
s.push("C")
s.push("D")

s.pop()
print(s.get())
s.push("E")
s.push("F")

s.pop()
print(s.get())
