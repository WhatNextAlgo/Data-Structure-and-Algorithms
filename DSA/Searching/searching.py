# Databricks notebook source
# MAGIC %md ###Binary Search tree

# COMMAND ----------

class BSTNode:
  def __init__(self,key):
    self.key = key
    self.left = None
    self.right = None
    self.parent=None
    
  def insert(self,node):
    if self.key > node.key:
      if self.left is None:
        self.left = node
      else:
        self.left.insert(node)
        
    elif self.key <= node.key:
      if self.right is None:
        self.right = node
      else:
        self.right.insert(node)
        
  def inorder(self):
    if self.left is not None:
      self.left.inorder()
      
    print(self.key,end=" ")
    if self.right is not None:
      self.right.inorder()
      
      
  def preorder(self):
    print(self.key,end=" ")
    if self.left is not None:
      self.left.preorder()
      
    if self.right is not None:
      self.right.preorder()
          
      
  def postorder(self):
    
    if self.left is not None:
      self.left.postorder()
      
    if self.right is not None:
      self.right.postorder()
      
    print(self.key,end=" ")  
    
class BSTree:
  def __init__(self):
    self.root = None
    
  def inorder(self):
    if self.root is not None:
      self.root.inorder()
      
      
  def preorder(self):
    if self.root is not None:
      self.root.preorder()
      
  def postorder(self):
    if self.root is not None:
      self.root.postorder()    
      
      
  def add(self,key):
    new_node = BSTNode(key)
    if self.root is None:
      self.root = new_node
    else:
      self.root.insert(new_node)
    
        

# COMMAND ----------

bstree = BSTree()

bstree.add(5)
bstree.add(6)
bstree.add(17)
bstree.add(23)
bstree.add(13)
bstree.add(3)
bstree.add(10)
bstree.add(2)
bstree.add(4)
  
  
bstree.inorder()  
print()
bstree.preorder()  
print()
bstree.postorder()  


# COMMAND ----------

# MAGIC %md ###Linear Search

# COMMAND ----------

def linear_search(alist,key):
  for x in range(len(alist)):
    if alist[x] == key:
      return x
  return -1  

# COMMAND ----------

a =[5,3,6,2,8,9,10]
print(linear_search(a,3))

# COMMAND ----------

# MAGIC %md ###Binary search without recursion

# COMMAND ----------

def binary_search(alist, key):
    """Search key in alist[start... end - 1]."""
    start = 0
    end = len(alist)
    while start < end:
        mid = (start + end)//2
        if alist[mid] > key:
            end = mid
        elif alist[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1   

# COMMAND ----------

a =[3 ,5 ,10 ,12, 15 ,20]
print(binary_search(a,12))

# COMMAND ----------

# MAGIC %md ### Binary serach with recursion

# COMMAND ----------

def binary_search(alist,start,end,key):
  if not start < end:
    return -1
  mid = (start+end)//2
  if alist[mid] > key:
    return binary_search(alist,start,mid,key)
  elif alist[mid] < key:
    return binary_search(alist,mid+1,end,key)
  else:
    return mid

# COMMAND ----------

a =[3 ,5 ,10 ,12, 15 ,20]
print(binary_search(a,0,len(a),20))

# COMMAND ----------

# MAGIC %md ###Python Program to Select the ith Smallest Element from a List in Expected Linear Time

# COMMAND ----------

def select(alist, start, end, i):
    """Find ith smallest element in alist[start... end-1]."""
    if end - start <= 1:
        return alist[start]
    
    pivot = partition(alist, start, end)
 
    # number of elements in alist[start... pivot]
    k = pivot - start + 1
    print(alist,"--pv",alist[pivot],"--",pivot,'__i',i,"--k",k)
    if i < k:
        return select(alist, start, pivot, i)
    elif i > k:
        return select(alist, pivot + 1, end, i - k)
 
    return alist[pivot]
 
def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1
    print("start",start)
    print("pivot",pivot,"I",i,"j",j)
 
    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1
 
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j

# COMMAND ----------

a =[3,4 ,5 ,-1 ,0, 2 ,-2,6]
print(select(a,0,len(a),6))

# COMMAND ----------

# MAGIC %md ###Python Program to Find Element Occurring Odd Number of Times in a List

# COMMAND ----------

def find_odd_occurring(alist):
    """Return the element that occurs odd number of times in alist.
 
    alist is a list in which all elements except one element occurs an even
    number of times.
    """
    ans = 0
 
    for element in alist:
        ans ^= element
        
    return ans
 
 
  

# COMMAND ----------

a = [ 1, 2, 3 ,1, 2, 3, 4, 1, 2 ,3 ,1, 2 ,4, 3, 4,1,4]
print(find_odd_occurring(a))

# COMMAND ----------

# MAGIC %md ###Python Program to solve Maximum Subarray Problem using Divide and Conquer

# COMMAND ----------

def find_max_subarray(alist,start,end):
  if start == end -1:
    return start,end, alist[start]
  else:
    mid = (start+end)//2
    left_start, left_end, left_max= find_max_subarray(alist,start,mid)
    right_start, right_end, right_max = find_max_subarray(alist,mid,end)
    cross_start, cross_end, cross_max = find_cross_max_subarray(alist,start,mid,end)
    if (left_max > right_max and left_max > cross_max):
      return left_start, left_end, left_max
    elif (right_max > left_max  and right_max > cross_max):
      return right_start, right_end, right_max
    else:
      return cross_start, cross_end, cross_max
    
def find_cross_max_subarray(alist,start,mid,end):
  sum_left = float('-inf')
  sum_temp = 0
  cross_start = mid
  for i in range(mid -1,start -1 ,-1):
    sum_temp = sum_temp + alist[i]
    if sum_temp > sum_left:
      sum_left = sum_temp
      cross_start = i
  
  sum_right = float('-inf')
  sum_temp = 0
  cross_end = mid +1
  for i in range(mid,end):
    sum_temp = sum_temp + alist[i]
    if sum_temp > sum_right:
      sum_right = sum_temp
      cross_end = i + 1
  return cross_start,cross_end,sum_left + sum_right    
      

# COMMAND ----------

a = [2,-9,3,5,-13,5,6,-10,1,-2,5]
find_max_subarray(a,0,len(a))

# COMMAND ----------

#         3 -2 5 - 1 == l =3,r=5,m=-2 max = 6

# left half lm=3                right half 5
# 3 -2                          5 -1

# lf rh   l=3,r=-2,lr=1         lf rh     l=5,r=-1,lr=4
# 3  -2                         5  -1

# COMMAND ----------

# MAGIC %md ###Python Program to solve Maximum Subarray Problem using Kadane’s Algorithm

# COMMAND ----------

def find_max_subarray(alist,start,end):
  """Return (l,r,m) such that alist[l:r] is max subarray list in
  A[start:end] with sum of m. Here A[start:end] means all A[x] for start <= x <
  end."""
  
  max_end_at_i = max_seen_so_far = alist[start]
  max_left_at_i = max_left_so_far = start
  # max_right_at_i is always i + 1
  max_right_so_far = start + 1
  
  for i in range(start+1,end):
    if max_end_at_i > 0:
      max_end_at_i += alist[i]
    else:
      max_end_at_i = alist[i]
      max_left_at_i = i
      
    if max_end_at_i > max_seen_so_far:
      max_seen_so_far = max_end_at_i
      max_left_so_far = max_left_at_i
      max_right_so_far = i + 1
  return max_left_so_far, max_right_so_far,max_seen_so_far

# COMMAND ----------

a = [2,-9,3,5,-13,5,6,-10,11,-2,5]
find_max_subarray(a,0,len(a))

# COMMAND ----------


