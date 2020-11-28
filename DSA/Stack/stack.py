# Databricks notebook source
# DBTITLE 1,STACK
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
  
  def display(self):
    if not self.is_empty():
      for data in reserved(self.items):
        print(data)
  
  

# COMMAND ----------

#Determine if Parenthesis are Balanced

def is_balanced_parenthesis(string_params):
  s = stack()
  is_balanced  = True
  index = 0
  while index < len(string_params) and is_balanced:
    paren = string_params[index]
    if paren in "{([":
      s.push(paren)
    else:
      if s.is_empty():
        is_balanced = False
      else:
        top = s.pop()
        if not match(top,paren):
          is_balanced = False
    index = index +1
    
  return is_balanced  
    
    
def match(p1,p2):
  if p1 =="("  and p2 == ")":
    return True
  elif p1 =="["  and p2 == "]":
    return True
  elif p1 =="{"  and p2 == "}":
    return True
  else:
    return False

# COMMAND ----------

is_balanced_parenthesis("{([])}")

# COMMAND ----------

#Convert Integer to Binary

def con_int_to_bin(num):
  string = ""
  s = stack()
  while num > 0:
    rem = num%2
    s.push(rem)
    num = num //2
  
  while not s.is_empty():
    string += ""+str(s.pop())
    
  return string  

# COMMAND ----------

con_int_to_bin(10)

# COMMAND ----------

# DBTITLE 1,Python Program to Reverse a Stack using Recursion
#Using Above stack implement

def insert_to_bottom(s,key):
  if s.is_empty():
    s.push(key)
  else:
    popped = s.pop()
    insert_to_bottom(s,key)
    s.push(popped)
    
def reserve_stack(s):
  if not s.is_empty():
    popped = s.pop()
    reserve_stack(s)
    insert_to_bottom(s,popped)
    

# COMMAND ----------

s = stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
insert_to_bottom(s,"E")
insert_to_bottom(s,"F")
reserve_stack(s)
s.get_stack()

# COMMAND ----------

# DBTITLE 1,Python Program to Check if String is Palindrome using Stack
text ="sumit"
s = stack()
for char in text:
  s.push(char)
  
reserve_text = "" 
while not s.is_empty():
  reserve_text = reserve_text + str(s.pop())

if text == reserve_text:
  print("String is Palindrome")
else:
  print("String is not Palindrome")

# COMMAND ----------

# DBTITLE 1,Python Program to Check if Expression is Correctly Parenthesized
exp = "(3 + 4 * (1 + (2))/(7 * (8 + 9)))"
s = stack()
for c in exp:
  if c == "(":
    s.push(c)
  elif c == ")":
    if s.is_empty():
      is_balanced = True
      break
    s.pop()
else:
  if s.is_empty():
    is_balanced = True
  else:
    is_balanced = False

    
if is_balanced:
    print('Expression is correctly parenthesized.')
else:
    print('Expression is not correctly parenthesized.')    

# COMMAND ----------

# DBTITLE 1,Python Program to Implement Queues using Stacks
class Queue:
  def __init__(self):
    self.inbox = stack()
    self.outbox = stack()
    
  def is_empty(self):
    return (self.inbox.is_empty() and self.outbox.is_empty())
  
  def enqueue(self,key):
    self.inbox.push(key)
    
  def dequeue(self):
    if  self.outbox.is_empty():
      while not self.inbox.is_empty():
        popped = self.inbox.pop()
        self.outbox.push(popped)
    if not self.is_empty():
      return self.outbox.pop()   
    
  def get_stack(self):
    return self.outbox.items

# COMMAND ----------

q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.enqueue("E")
q.dequeue()
q.enqueue("F")
q.enqueue("G")
