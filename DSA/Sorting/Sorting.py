# Databricks notebook source
# MAGIC %md ### Bubble Sort

# COMMAND ----------

def bubble_sort(alist):
  l = len(alist)
  no_swap = True
  for x in range(l-1,0,-1):
    for y in range(0,x):
      if alist[y+1] < alist[y]:
        alist[y+1],alist[y] = alist[y],alist[y+1]
        no_swap=False
        
    if no_swap:
      return 

# COMMAND ----------

a = [2,7,4,3,5,1,6]
bubble_sort(a)
print(a)

# COMMAND ----------

# MAGIC %md ### selection sort 

# COMMAND ----------

def selection_sort(alist):
  l = len(alist)
  for i in range(0,l-1):
    smallest = i
    for j in range(i+1,l-1):
      if alist[j] < alist[smallest]:
        smallest = j
        
    alist[i],alist[smallest] = alist[smallest],alist[i]   

# COMMAND ----------

a = [2,7,4,3,5,1,6]
selection_sort(a)
print(a)

# COMMAND ----------

# MAGIC %md ###insertion sort

# COMMAND ----------

def insertion_sort(alist):
  l = len(alist)
  for x in range(1,l):
    temp = alist[x]
    #j is use for backward direaction until 0 element
    j = x -1
    while j>=0 and temp < alist[j]:
      alist[j+1] =alist[j]
      j = j-1
    alist[j+1] = temp
    
      
    

# COMMAND ----------

a = [2,7,4,3,5,1,6]
insertion_sort(a)
print(a)

# COMMAND ----------

# MAGIC %md ### merge sort

# COMMAND ----------

def merge_sort(alist):
  n = len(alist)
  if n > 1:
    mid = n//2
    left = alist[:mid]
    right = alist[mid:]
    merge_sort(left)
    merge_sort(right)
    
    k =0
    i =0
    j =0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        alist[k] = left[i]
        i = i + 1
        
      else:
        alist[k] = right[j]
        j = j + 1
  
      k = k + 1
    
    while i < len(left):
      alist[k] = left[i]
      i = i + 1
      k = k + 1
      
    while j < len(right):
      alist[k] = right[j]
      j = j + 1
      k = k + 1  
      
        
  

      
  

# COMMAND ----------

a = [2,7,4,3,5,1,6]
merge_sort(a)
print(a)

# COMMAND ----------

# MAGIC %md ###Quick Sort

# COMMAND ----------

def quick_sort(alist,start,end):
  if end - start >1:
    p = partition(alist,start,end)
    quick_sort(alist,start,p)
    quick_sort(alist,p+1,end)
  
def partition(alist,start,end):
  pivot = alist[start]
  left_mark = start + 1
  right_mark = end - 1
  
  done = False
  while not done:
    while left_mark <= right_mark and alist[left_mark] <= pivot:
      left_mark = left_mark +1
      
    while alist[right_mark] >=pivot and right_mark >= left_mark:
      right_mark = right_mark -1  
      
    if right_mark < left_mark:
      done = True
    else:
      alist[left_mark],alist[right_mark] = alist[right_mark],alist[left_mark]
  
  alist[start],alist[right_mark] = alist[right_mark],alist[start]     
  return right_mark
  
  
  

# COMMAND ----------

alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist,0,len(alist))
print(alist)

# COMMAND ----------

# MAGIC %md ###Heap Sort

# COMMAND ----------

def heap_sort(alist):
  build_max_heap(alist)
  for i in range(len(alist)-1,0,-1):
    alist[0],alist[i] = alist[i],alist[0]
    max_heapify(alist,index= 0,size=i)
    
    
def parent(i):
  return (i-1)//2

def left(i):
  return 2*i +1

def right(i):
  return 2*i+2

def build_max_heap(alist):
  length = len(alist)
  start = parent(length-1)
  count = 0
  while start >= 0:
    print("start",start)
    max_heapify(alist,index=start,size = length)
    start = start -1
    count +=1
    
    print("count",count,"---",alist) 
   
  
def max_heapify(alist,index,size):
  largest = index
  l = left(index)
  r  = right(index)
  if l < size and alist[l] > alist[index]:
    largest = l
  else:
    largest = index
    
  if r < size and alist[r] > alist[largest]:
    largest = r
    
  if largest != index:
    alist[largest],alist[index] = alist[index],alist[largest]
    max_heapify(alist,largest,size)
    

# COMMAND ----------

alist = [54,26,93,17,77,31,44,55,20]
heap_sort(alist)
print(alist)

# COMMAND ----------

# MAGIC %md ###Counting Sort

# COMMAND ----------

def counting_sort(alist,k):
  c = [0]* (k +1)
  
  for x in range(0,len(alist)):
    #based on value go to the index increment by 1
    c[alist[x]] = c[alist[x]] +1
    
  print("step 1",c) 
  c[0] = c[0]
  for x in range(1,k+1):
    c[x] = c[x] + c[x-1]
   
  print("step 2",c)
  
  result = [None] * len(alist)
  
  for y in range(len(alist)-1,-1,-1):
    c[alist[y]]= c[alist[y]]-1
    result[c[alist[y]]] = alist[y]
    
  return result

# COMMAND ----------

a = [1,3,4,5,4,6,4,4,7,3,7,2,2,1,9]
counting_sort(a,k=9)

# COMMAND ----------

# 199//10**1 % 10

# COMMAND ----------

# MAGIC %md ### Radix sort

# COMMAND ----------

def radix_sort(alist,base=10):
  if alist == []:
    return
  #digit is  index place  of a number ex : 298 -- 8 is digit 10 ** 0 = 1th place, 9 is digit 10 **1 = 10th place, 2 is digit 10 **2 = 100th place. 
  #digit refers to 10 ** digit
  def key_factory(digit,base):
    def key(alist,index):
      return ((alist[index]//base ** digit) % base)
    return key
  
  largest = max(alist)
  exp = 0
  while base**exp <= largest:
    alist = radix_counting_sort(alist,base -1,key_factory(exp,base))
    exp = exp +1
  return alist  
    
def radix_counting_sort(alist,largest,key):
  c = [0] * (largest+1)
  
  for i in range(len(alist)):
    c[key(alist,i)] = c[key(alist,i)] +1
    
    
  c[0] = c[0]
  for x in range(1,largest+1):
    c[x] = c[x] + c[x-1] 
    
  result = [None]*len(alist)
  
  for i in range(len(alist)-1,-1,-1):
    c[key(alist,i)] = c[key(alist,i)] -1
    result[c[key(alist,i)]] = alist[i]
    
  return result

# COMMAND ----------

a = [432,8,530,90,88,231,11,45,677,199]
radix_sort(a)

# COMMAND ----------

# MAGIC %md ###bucket sort

# COMMAND ----------

def bucket_sort(alist):
  largest= max(alist)
  length = len(alist)
  size = largest/length
  
  buckets = [[] for _ in range(length)]
  print(buckets)
  for i in range(length):
    j=  int(alist[i]/size)
    if j  != length:
      buckets[j].append(alist[i])
    else:
      buckets[length -1].append(alist[i])
      
  print(buckets)  
  
  for i in range(length):
    insertionSort(buckets[i])
    print(buckets[i])
  
  result = []
  for x in range(length):
    result = result + buckets[x]
    
 
  return result  
    
    
def insertionSort(alist):
  for i in range(1,len(alist)):
    temp = alist[i]
    j = i -1
    
    while j >=0 and alist[j] >temp:
      alist[j+1] = alist[j]
      j = j -1
      
    alist[j+1] = temp
      
      

# COMMAND ----------

a = [432,8,530,90,88,231,11,45,677,199]
bucket_sort(a)

# COMMAND ----------

# MAGIC %md ###gnome sort.

# COMMAND ----------

def gnome_sort(alist):
  for pos in range(1,len(alist)):
    while pos !=0 and alist[pos] < alist[pos-1]:
      alist[pos],alist[pos-1]= alist[pos-1],alist[pos]
      pos =pos-1
      

# COMMAND ----------

a = [432,8,530,90,88,231,11,45,677,199]
gnome_sort(a)
print(a)

# COMMAND ----------

def cocktail_shaker_sort(alist):
  def swap(i,j):
    alist[i],alist[j] = alist[j],alist[i]
  
  lower = 0
  upper = len(alist) -1
  no_swap = False
  while (not no_swap and upper -lower >1):
    no_swap = True
    for j in range(lower,upper):
      if alist[j+1] < alist[j]:
        swap(j+1,j)
        no_swap = False
        
    upper = upper-1 
    for j in range(upper,lower,-1):
      if alist[j-1] > alist[j]:
        swap(j-1,j)
        no_swap = False
        
    lower = lower + 1 
        
        
         
         

# COMMAND ----------

a = [432,8,530,90,88,231,11,45,677,199]
cocktail_shaker_sort(a)
print(a)

# COMMAND ----------

# MAGIC %md ### Comb sort

# COMMAND ----------

def comb_sort(alist):
  gap = len(alist)
  shrink = 1.3
  
  def swap(i,j):
    alist[i],alist[j]=alist[j],alist[i]
    
  no_swap =False
  while not no_swap:
    gap = int(gap/shrink)
    
    if gap < 1:
      gap = 1
      no_swap=True
    else:
      no_swap =False
    i = 0
    while i+gap < len(alist):
      if alist[i] > alist[i+gap]:
        swap(i,i+gap)
        no_swap =False
      i = i +1  

# COMMAND ----------

a = [432,8,530,90,88,231,11,45,677,199]
comb_sort(a)
print(a)

# COMMAND ----------

# MAGIC %md ### shell Sort

# COMMAND ----------

def gaps(size):
  length = size.bit_length()
  for k in range(length -1,0,-1):
    yield 2**k -1
    
def shell_sort(alist):
  def insertion_sort_gap(gap):
    for i in range(gap,len(alist)):
      temp = alist[i]
      j = i - gap
      while j >=0 and alist[j] > temp:
        alist[j+ gap] = alist[j]
        j = j - gap
      
      alist[j+gap] = temp
      
  for g in gaps(len(alist)):
    insertion_sort_gap(g)
  

# COMMAND ----------

a = [432,8,530,90,88,231,11,45,677,199]
shell_sort(a)
print(a)

# COMMAND ----------

# MAGIC %md ###Intro Sort

# COMMAND ----------

def intro_sort(alist):
  max_depth = (len(alist).bit_length() -1)*2
  intro_sort_helper(alist,0,len(alist),max_depth)
  
def intro_sort_helper(alist,start,end,max_depth):
  if end - start <= 1:
    return 
  elif max_depth == 0:
    heap_sort(alist,start,end)
  else:
    p = partiton(alist,start,end)
    intro_sort_helper(alist,start,p+1,max_depth-1)
    intro_sort_helper(alist,p+1,end,max_depth-1)
    
def partiton(alist,start,end):
  pivot = alist[start]
  i = start -1 
  j = end
  
  while True:
    i = i + 1
    while alist[i] < pivot:
      i = i+1
      
    j = j - 1
    while alist[j] > pivot:
      j = j - 1
      
    if i <= j:
      swap(alist,i,j)
    else:
      return j
    
def swap(alist, i, j):
  alist[i], alist[j] = alist[j], alist[i]    
  
def heap_sort(alist,start,end):
  build_max_heap(alist,start,end)
  for i in range(end -1,start,-1):
    swap(alist,start,i)
    max_heapify(alist,index = 0,start=start,end =i)
    
def build_max_heap(alist, start, end):
    def parent(i):
        return (i - 1)//2
    length = end - start
    index = parent(length - 1)
    while index >= 0:
        max_heapify(alist, index, start, end)
        index = index - 1
        
        
        
def max_heapify(alist, index, start, end):
    def left(i):
        return 2*i + 1
    def right(i):
        return 2*i + 2
 
    size = end - start
    l = left(index)
    r = right(index)
    if (l < size and alist[start + l] > alist[start + index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[start + r] > alist[start + largest]):
        largest = r
    if largest != index:
        swap(alist, start + largest, start + index)
        max_heapify(alist, largest, start, end)        

# COMMAND ----------

a = [432,8,530,90,88,231,11,45,677,199]
intro_sort(a)
print(a)

# COMMAND ----------

# MAGIC %md ###Binary Insertion Sort

# COMMAND ----------

def Binary_insertion_search(alist):
  for i in range(1,len(alist)):
    temp =alist[i]
    print("temp",temp)
    pos= binary_search(alist,temp,0,i) + 1
    print("pos",pos)
    
    for k in range(i,pos,-1):
      alist[k]= alist[k-1]
      print(alist[k],"---",alist[k-1])
      
    alist[pos] = temp
    
    print(alist)
    
def binary_search(alist,key,start,end):
  print("key",key,"--",alist[start],"--end",end)
  if end-start <=1:
    if key < alist[start]:
      return -1
    else:
      return  start
    
  mid = (start+end)//2 
  if alist[mid] < key:
    return binary_search(alist,key,mid,end)
  elif alist[mid]>key:
    return binary_search(alist,key,start,mid)
  else:
    return mid
  

# COMMAND ----------

a = [432,8,530,90,88,231,11,45,677,199]
Binary_insertion_search(a)
print(a)
