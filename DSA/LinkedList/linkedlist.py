# Databricks notebook source
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
  
  def print_list(self):
    curr = self.head
    while curr:
      print(curr.data)
      curr = curr.next
    print()  
      
      
  def append(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return 
    
    last_node = self.head
    while last_node.next :
      last_node = last_node.next
    
    last_node.next = new_node
  
  def prepend(self,data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    
  def insert_after_node(self,prev_node,data):
    if not prev_node:
      print("Node not in alist")
      return
    
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    
  def delete_node(self,key):
    curr_node = self.head
    if curr_node and curr_node.data == key:
      self.head = curr_node.next
      curr_node = None
      return 
    prev = None
    while curr_node and curr_node.data !=key:
      prev = curr_node
      curr_node = curr_node.next
      
    if curr_node is None:
      return
    
    prev.next = curr_node.next
    curr_node = None
    
  def delete_node_at_pos(self,pos):
    curr_node = self.head
    if pos == 0:
      self.head = curr_node.next
      curr_node = None
      return 
    prev = None
    count =0
    while curr_node and count !=pos:
      prev = curr_node
      curr_node = curr_node.next
      count +=1
      
    if curr_node is None:
      return
    
    prev.next = curr_node.next
    curr_node = None  
      
  def len_iterative(self):
    curr = self.head
    count = 0
    while curr:
      curr = curr.next
      count +=1
    return count 
  
  def len_recursive(self,node):
    if node is None:
      return 0
    return 1 + self.len_recursive(node.next)
    
  def swap_nodes(self,key_1,key_2):
    if key_1 == key_2:
      return 
    prev_1 = None
    curr_1 = self.head
    while curr_1 and curr_1.data != key_1:
      prev_1 = curr_1
      curr_1 = curr_1.next
      
    prev_2 = None
    curr_2 = self.head
    while curr_2 and curr_2.data != key_2:
      prev_2 = curr_2
      curr_2 = curr_2.next  
      
      
    print("prev1",prev_1.data)  
    print("prev2",prev_2.data)
    print("curr_1",curr_1.data)  
    print("curr_2",curr_2.data) 
      
    if not curr_1 or not curr_2:
      return 
    
    if prev_1:
      prev_1.next = curr_2
    else:
      self.head = curr_2
      
    if prev_2:
      prev_2.next = curr_1
    else:
      self.head = curr_1
      
    curr_1.next,curr_2.next = curr_2.next,curr_1.next
    
  # A->B->C->D->null
  # D->C->B->A->null
  
  def print_helper(self,node,name):
    if node is None:
      print(name , " : None")
    else:
      print(name , " : ", node.data)
  
  def reserve_iterative(self):
    prev =None
    curr = self.head
    while curr:
      temp = curr.next
      curr.next = prev
      self.print_helper(prev,"PREV")
      self.print_helper(curr,"CURR")
      self.print_helper(temp,"NXT")
      print()
      prev = curr
      curr = temp
    
    print("head",prev.data)
    self.head= prev
      
  def reserve_recursive(self):
    
    def _reserve_recursive(curr,prev):
      if curr is None:
        return prev
      temp = curr.next
      curr.next = prev
      self.print_helper(prev,"PREV")
      self.print_helper(curr,"CURR")
      self.print_helper(temp,"NXT")
      print()
      prev = curr
      curr = temp
      return _reserve_recursive(curr,prev)
    
    self.head = _reserve_recursive(curr = self.head,prev=None)
    
    
  def merge_sorted(self,llist):
    p = self.head
    q = llist.head
    s= None
    
    if not p:
      return q
    if not q:
      return p
    
    if p and q:
      if p.data <= q.data:
        s = p
        p = s.next
      else:
        s = q
        q = q.next
      
      new_head =s
      
    while p and q:
      if p.data <= q.data:
        s.next =p
        s = p
        p = s.next
      else:
        s.next =q
        s = q
        q = s.next
    
    if not p:
      s.next = q
    if not q:
      s.next = p
      
    return new_head 
  
  def remove_duplicates(self):
    curr = self.head
    prev = None
    dup_values = dict()
    while curr:
      if curr.data in dup_values:
        prev.next = curr.next
        curr = None
      else:
        dup_values[curr.data] = 1
        prev = curr
      curr = prev.next  
    
  def nth_node(self,n):

    if n < 1:
      return 
    
    curr = self.head
    count = 1
    while curr:
      if count == n:
        print(curr.data)
        return curr
      count +=1
      curr = curr.next
      
    if n > count:
      return
    

  def count_iterative(self,data):
    curr = self.head
    count = 0
    while curr:
      if curr.data == data:
        count +=1
      curr = curr.next
      
    return count  
  def count_recursive(self,node,data):
    if not node:
      return 0
    if node.data == data:
      return 1 + self.count_recursive(node.next,data)
    else:
      return self.count_recursive(node.next,data)
      
  def rotate(self,k):
    p = self.head
    q = self.head
    prev = None
    count = 0
    
    while p and count < k:
      prev = p
      p = p.next
      q = q.next
      count +=1
    p  = prev
    print("p",p.data)
    
    while q:
      prev = q
      q = q.next
    q = prev
    print("q",q.data)
    
    q.next = self.head
    self.head = p.next
    p.next = None
    
  def is_palindrome(self):
#     Method 1:
#     s = ""
#     p = self.head
#     while p :
#       s += p.data
#       p = p.next
#     return s == s[::-1]
#       #Method 2
#       s = []
#       p =self.head
#       while p :
#         s.append(p.data)
#         p = p.next
#       p = self.head

#       while p :
#         data = s.pop()
#         if p.data != data:
#           return False
#         p = p.next

#       return True  
        #Method 1:
      p = self.head
      q = self.head
      prev = []
      i = 0
      while q:
        prev.append(q)
        q = q.next
        i +=1
      q  = prev[i-1]
      count =1
      while count <= i//2 +1:
        if prev[-count].data != p.data:
          return False
        p = p.next
        count +=1
      
      return True
    
  def move_tail_to_head(self):
    last_node = self.head
    sec_to_last = None
    while last_node.next:
      sec_to_last = last_node
      last_node =last_node.next
    
    last_node.next =self.head
    sec_to_last.next=None
    self.head=last_node
    
  def sum_two_list(self,llist):
    p =self.head
    q = llist.head
    sum_list=LinkedList()
    carry=0
    while p or q:
      if not p:
        i = 0
      else:
        i = p.data
      if not q:
        j = 0
      else:
        j = q.data
        
      s = i + j+ carry
      if s >= 10:
        carry =1
        rem = s%10
        sum_list.append(rem)
      else:
        carry=0
        sum_list.append(s)
      
      if p:
        p = p.next
      if q:
        q = q.next
    sum_list.print_list()    
      
    
      

# COMMAND ----------

l = LinkedList()
l.append("A")
l.append("B")
#l.print_list()
l.append("C")
l.append("D")
#l.prepend("E")
#l.print_list()

#l.insert_after_node(l.head.next,"E")
#l.print_list()
#l.delete_node("E")
#l.delete_node_at_pos(1)
#l.print_list()
#print(l.len_iterative())
#print(l.len_recursive(l.head))
#l.swap_nodes("B","C")
#l.reserve_iterative()
#l.print_list()

#recursive
l.reserve_recursive()
l.print_list()

# COMMAND ----------

l1 = LinkedList()
l2 = LinkedList()

l1.append(1)
l1.append(5)
l1.append(7)
l1.append(9)
l1.append(10)

l2.append(2)
l2.append(3)
l2.append(4)
l2.append(6)
l2.append(8)
l1.print_list()
l2.print_list()
l1.merge_sorted(l2)
l1.print_list()

# COMMAND ----------

#remove duplicates in linked list
l1 = LinkedList()

l1.append(1)
l1.append(5)
l1.append(1)
l1.append(9)
l1.append(5)
l1.append(2)

l1.print_list()
l1.remove_duplicates()
l1.print_list()

# COMMAND ----------

l1 = LinkedList()

l1.append('A')
l1.append('B')
l1.append('A')
l1.append('D')
l1.append('E')
l1.append('F')

#print(l1.nth_node2(4))
print(l1.count_iterative("A"))
print(l1.count_recursive(l1.head,"A"))


# COMMAND ----------

l1 = LinkedList()


l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.print_list()
l1.rotate(4)
l1.print_list()

# COMMAND ----------

# DBTITLE 1,palindrome
l1 = LinkedList()
l2 = LinkedList()

l1.append("R")
l1.append("A")
l1.append("D")
l1.append("A")
l1.append("R")

l2.append("S")
l2.append("U")
l2.append("M")
l2.append("I")
l2.append("T")
print(l1.is_palindrome())
print(l2.is_palindrome())

# COMMAND ----------

# DBTITLE 1,Move tail  to head
l2 = LinkedList()
l2.append("S")
l2.append("U")
l2.append("M")
l2.append("I")
l2.append("T")
l2.move_tail_to_head()
l2.print_list()

# COMMAND ----------

# DBTITLE 1,sum of two linked list
l1 = LinkedList()
l2 = LinkedList()

l1.append(5)
l1.append(6)
l1.append(3)

l2.append(8)
l2.append(4)
l2.append(2)
l1.sum_two_list(l2)
print(365 + 248)

# COMMAND ----------

# DBTITLE 1,Circular LinkedList
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
class CircularLinkedList:
  def __init__(self):
    self.head = None
    
  def append(self,data):
    
    if not self.head :
      self.head = Node(data)
      self.head.next = self.head
    else:
      new_node = Node(data)
      curr= self.head
      prev = None
      while  curr.next != self.head:
        prev = curr
        curr = curr.next
      curr.next = new_node 
      new_node.next = self.head
      
  def prepend(self,data):
    new_node = Node(data)
    curr = self.head
    new_node.next = self.head
    
    if not self.head:
      new_node.next = new_node
    else:
      while curr.next != self.head:
        curr = curr.next
      curr.next = new_node
    self.head = new_node
    
    
  def remove(self,data):
    if self.head.data == data:
      curr = self.head
      while curr.next != self.head:
          curr = curr.next
      
      curr.next = self.head.next
      self.head = self.head.next
    else:
      prev = None
      curr =  self.head
      while curr.next != self.head:
        prev = curr
        curr = curr.next
        if curr.data == data:
          prev.next = curr.next
          curr = curr.next
          
  def __len__(self):
    count = 0
    curr = self.head
    while curr :
      count +=1
      curr = curr.next
      if curr == self.head:
        break
    return count
  
  def split_list(self):
    size = len(self)
    
    if size ==0:
      return None
    if size ==1:
      return self.head
    mid = size//2
    count = 0
    prev =None
    curr = self.head
    while curr and  count < mid:
      count +=1
      prev = curr
      curr = curr.next
      
    
    prev.next = self.head
    
    split_list= CircularLinkedList()
    while  curr.next != self.head:
      split_list.append(curr.data)
      curr = curr.next
    split_list.append(curr.data)
    
    self.print_list()
    print("")
    split_list.print_list()
      
  
  def remove_node(self,node):
    if self.head == node:
      curr = self.head
      while curr.next != self.head:
          curr = curr.next
      
      curr.next = self.head.next
      self.head = self.head.next
    else:
      prev = None
      curr =  self.head
      while curr.next != self.head:
        prev = curr
        curr = curr.next
        if curr == node:
          prev.next = curr.next
          curr = curr.next
          
  def josephus_circle(self,step):
    curr = self.head
    while  len(self) > 1:
      count =1
      while count != step:
        curr = curr.next
        count +=1
      print("remove",curr.data)  
      self.remove_node(curr)
      curr = curr.next
    self.print_list()  
      
  def is_circular_linkedlist(self,input_list):
    curr = input_list.head
    while curr.next :
      curr = curr.next
      if curr.next == input_list.head:
        return True
    return False
  
  def print_list(self):
    curr = self.head
    while curr:
      print(curr.data)
      curr = curr.next
      if curr == self.head:
        break
    print() 
    
    
      
    
    

# COMMAND ----------

c = CircularLinkedList()
c.append("B")
c.append("C")

c.print_list()
c.append("D")
c.print_list()
c.prepend("A")
c.print_list()

# COMMAND ----------

#remove node
c = CircularLinkedList()
c.append("A")
c.append("B")
c.append("C")
c.append("D")
c.remove("B")
c.remove("D")
c.print_list()

# COMMAND ----------

#split list
c = CircularLinkedList()
c.append("A")
c.append("B")
c.append("C")
c.append("D")
c.append("E")
#c.split_list()
#c.print_list()
print(len(c))
c.split_list()


# COMMAND ----------

#josephus circle
c = CircularLinkedList()
c.append("A")
c.append("B")
c.append("C")
c.append("D")
c.append("E")
c.josephus_circle(2)
c.print_list()

# COMMAND ----------

#is_circular_linkedList
l1 = LinkedList()


l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.print_list()

c = CircularLinkedList()
c.append("A")
c.append("B")
c.append("C")
c.append("D")
c.append("E")

print(c.is_circular_linkedlist(c))
print(c.is_circular_linkedlist(l1))

# COMMAND ----------

# DBTITLE 1,DOUBLY LINKED LIST
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
  
  def prepend(self,data):
    new_node = Node(data)
    if self.head is  None:
      self.head = new_node
      new_node.prev = None 
    else:
      curr = self.head
      new_node.next = self.head
      self.head.prev = new_node
      new_node.prev = None
      self.head = new_node
  
  def append(self,data):
    new_node = Node(data)
    if self.head is  None:
      self.head = new_node
      new_node.prev = None 
    else:
      curr = self.head
      while curr.next:
        curr = curr.next
      curr.next = new_node 
      new_node.prev = curr
      new_node.next =None
        
  def add_before_node(self,key,data):
      curr = self.head
      while curr:
        if curr.prev is None and curr.data ==data:
          self.prepend(data)
          return
        elif curr.data == key:
          new_node = Node(data)
          prev = curr.prev
          prev.next = new_node
          new_node.prev = prev
          new_node.next = curr
          curr.prev = new_node
          
        curr = curr.next
        
      
  def add_after_node(self,key,data):
    curr = self.head
    while curr:
      if curr.next is None and curr.data == key:
        self.append(data)
        return
      elif curr.data == key:
        new_node = Node(data)
        nxt = curr.next
        curr.next = new_node
        new_node.prev = curr
        new_node.next = nxt
        nxt.prev = new_node
      curr = curr.next  
      
      
  def delete(self,key):
    curr = self.head
    while curr:
      if curr == self.head and  curr.data == key:
        #case 1
        if not curr.next:
          curr = None
          self.head =None
          return 
        #case 2
        else:
          nxt = curr.next
          curr.next = None
          nxt.prev = None
          curr = None
          self.head = nxt
          return 
        
      elif curr.data == key:
        if curr.next :
          nxt = curr.next
          prev = curr.prev
          prev.next = nxt
          nxt.prev = prev
          curr.next = None
          curr.prev = None
          curr = None
          return
        else:
          prev = curr.prev
          prev.next = None
          curr.prev =None
          curr = None
          return 
      curr = curr.next 
        
  
  def delete_node(self,node):
    curr = self.head
    while curr:
      if curr == self.head and  curr == node:
        #case 1
        if not curr.next:
          curr = None
          self.head =None
          return 
        #case 2
        else:
          nxt = curr.next
          curr.next = None
          nxt.prev = None
          curr = None
          self.head = nxt
          return 
        
      elif curr == node:
        if curr.next :
          nxt = curr.next
          prev = curr.prev
          prev.next = nxt
          nxt.prev = prev
          curr.next = None
          curr.prev = None
          curr = None
          return
        else:
          prev = curr.prev
          prev.next = None
          curr.prev =None
          curr = None
          return 
      curr = curr.next 
      
  def reverse(self):
    temp = None
    curr = self.head
    
    while curr:
      temp = curr.prev
      curr.prev = curr.next
      curr.next = temp
      curr = curr.prev
    print("temp",temp.data)
    print("temp.prev",temp.prev.data)
    if temp :
      self.head = temp.prev
      
  def remove_duplicates(self):
    curr = self.head
    dup_values = dict()
    
    while curr:
      if curr.data not in dup_values:
        dup_values[curr.data] = 1
        curr = curr.next
      else:
        nxt = curr.next
        self.delete_node(curr)
        curr = nxt
  
  def pairs_with_sum(self,sum_val):
    p = self.head
    q = None
    count = 0
    pair = list()
    while p:
      q = p.next
      while q:
        if p.data + q.data == sum_val:
          pair.append("("+ str(p.data) + ","+str(q.data) + ")")
          count +=1
        q = q.next
      p = p.next
    return pair , count
  
  def print_list(self):
    curr = self.head
    while curr:
      print(curr.data)
      curr = curr.next
  

# COMMAND ----------

d = DoublyLinkedList()
d.append("A")
d.append("B")
d.print_list()
d.prepend("C")
d.print_list()

# COMMAND ----------

d = DoublyLinkedList()
d.append("A")
d.append("B")
d.append("C")
#d.print_list()
#d.add_after_node("B","D")
d.add_before_node("B","E")
d.print_list()


# COMMAND ----------

#delete
d = DoublyLinkedList()
d.append("A")
d.append("B")
d.append("C")
d.append("D")
d.delete("D")
#d.print_list()
d.delete("A")
d.delete("B")
d.print_list()

# COMMAND ----------

#reverse
d = DoublyLinkedList()
d.append("A")
d.append("B")
d.append("C")
d.append("D")
d.print_list()
print("\n")
d.reverse()
d.print_list()

# COMMAND ----------

#remove_duplicates
d = DoublyLinkedList()
d.append(8)
d.append(4)
d.append(4)
d.append(5)
d.append(6)
d.append(8)
d.remove_duplicates()
d.print_list()

# COMMAND ----------

#pairs with sums
d = DoublyLinkedList()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
print(d.pairs_with_sum(5))


# COMMAND ----------

#Array advance game

def array_advance(a):
  furthest_advanced = 0
  last_idx = len(a)-1
  i = 0
  while i <= furthest_advanced and furthest_advanced < last_idx:
    furthest_advanced = max(furthest_advanced,a[i] + i)
    i +=1
  return furthest_advanced >= last_idx
a = [3,3,1,0,2,0,1]
print(array_advance(a))

a1 = [3,2,0,0,2,0,1]
print(array_advance(a1))

# COMMAND ----------

#Two Sum Problem
A = [-2,1,2,4,7,11]
def two_sum_brute_force(A,target):
  for i in range(len(A)-1):
    for j in range(i+1,len(A)):
      if A[i] + A[j] == target:
        print(A[i],A[j])
        return True
  return False  
print(two_sum_brute_force(A,13))


#method 1
def two_sum_hash_table(A,target):
  ht = dict()
  
  for i in range(len(A)):
    if A[i] in ht:
      print(ht[A[i]],A[i])
      return True
    else:
      ht[target - A[i]] = A[i]
  return False
print(two_sum_hash_table(A,13))
    
def two_sum(A,target):
  i  = 0
  j = len(A) -1
  while i <= j:
    if A[i] + A[j] == target:
      print(A[i],A[j])
      return True
    elif A[i] + A[j] < target:
      i +=1
    else:
      j-=1
  return False

print(two_sum(A,13))

# COMMAND ----------

#Buy and Sell Stock
def buy_sell_once(A):
  max_profit = 0
  for i in range(len(A)-1):
    for j in range(i+1,len(A)):
      if A[j] - A[i] > max_profit:
        max_profit = A[j] - A[i]
  return max_profit      

def buy_spell(A):
  max_profit = 0
  min_price = A[0]
  for price in A:
    min_price = min(min_price,price)
    compare_price = price - min_price
    max_profit = max(max_profit,compare_price)
  return   max_profit
A = [310,315,275,295,260,270,290,230,255,250]
print(buy_sell_once(A))

print(buy_spell(A))

# COMMAND ----------


