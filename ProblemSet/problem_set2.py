# Databricks notebook source
# DBTITLE 1,Python Program to Accept a Hyphen Separated Sequence of Words as Input and Print the Words in a Hyphen-Separated Sequence after Sorting them Alphabetically
s = "red-green-blue-yellow"
lst = s.split("-")
lst.sort()
"-".join(lst)

# COMMAND ----------

# DBTITLE 1,Python Program to Calculate the Number of Digits and Letters in a String
s = "Hello123"
l = 0
d = 0
for x in s:
  l +=1
  if x.isdigit():
    d +=1  
    
print("The number of digits is:")
print(d)
print("The number of characters is:")
print(l)    

# COMMAND ----------

# DBTITLE 1,Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String
s = "sumit maurya"

print(s[:2] + s[-2:])

# COMMAND ----------

# DBTITLE 1,Python Program to Count the Occurrences of Each Word in a Given String Sentence
s = "orange blue red orange"
w = "orange"
count = 0
lst = s.split()
for x in lst:
  if w == x:
    count +=1

print(count)

# COMMAND ----------

# DBTITLE 1,Python Program to Check if a Substring is Present in a Given String
s = "orange blue red orange"
w = "orange"
flag = False
lst = s.split()
for x in lst:
  if w == x:
    flag = True
    break
    
if flag:
  print("substring is present")
else:
  print("substring is not present")
  
  
if(s.find(w)==-1):
  print("Substring not found in string!")
else:
  print("Substring in string!")

# COMMAND ----------

# DBTITLE 1,Python Program to Print All Permutations of a String in Lexicographic Order without Recursion
from math import *
def print_permutations_lexicographic_order(s):
  seq = list(s)
  # there are going to be n! permutations where n = len(seq)
  for _ in range(factorial(len(seq))):
    print("".join(seq))
    
    p = len(seq) - 1
    while p > 0 and seq[p - 1] > seq[p]:
      p -=1
    
    #print("before",seq)
    seq[p:] = reversed(seq[p:])
    print("after",seq[p:],"-",p)
    
    if p > 0:
      #find q such that seq[q] is the smallest element in seq[p:] such that
      #seq[q] > seq[p-1]
      
      q = p
      print(" p",seq[p-1],p-1)
      print(" q",seq[q], q)
      while seq[p - 1] > seq[q]:
        print(" in p",seq[p-1],p-1)
        print(" in q",seq[q], q) 
        
        q +=1
        # swap seq[p - 1] and seq[q]
      print("out ",seq[p-1])
      print("out ",seq[q])
      seq[p - 1], seq[q] = seq[q], seq[p - 1]
      print("seq",seq)
print_permutations_lexicographic_order("pig")      

# COMMAND ----------

def permut(string,left,right):
  if left ==right:
    print(string)
  else:
    for x in range(left,right):
      swaped = swap(string,left,x)
      #print("swaped",swaped,"--left",left,"x",x)
      permut(swaped,left+1,right)
      print("p swaped",swaped,"--left",left,"x",x)
  
  
def swap(string,i,j):
  lst = list(string)
  lst[i],lst[j]= lst[j],lst[i]
  return "".join(lst)

permut("ABC",0,3)

# COMMAND ----------

#           ABC
#        /   | \
#       /   BAC  CBA
#     ABC    |\   \  \
#  /   \     | \    \  \
# ABC   ACB BAC BCA  CAB CBA

# COMMAND ----------

# DBTITLE 1,DICTIONARY - Python Program to Add a Key-Value Pair to the Dictionary
d = {}
n = 12
d[n] = 2*n
print(d)

# COMMAND ----------

# DBTITLE 1,Python Program to Concatenate Two Dictionaries Into One
d = {12:24}
d1 = {3:9}
d.update(d1)
print(d)
#z ={**d,**d1}
#print(z)

# COMMAND ----------

# DBTITLE 1,Python Program to Check if a Given Key Exists in a Dictionary or Not
d = {1:2,2:4,3:9,4:16,5:25}
n= 6
if n in d:
  print("Key %s is present and value of the key is:"%n,d[n])
else:
  print("Key %s isn't present!"%n)

# COMMAND ----------

# DBTITLE 1,Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
d= {}
n=12
for x in range(1,n):
  d[x] = x*x
print(d)

# COMMAND ----------

# DBTITLE 1,Python Program to Sum All the Items in a Dictionary
d= {}
n=12
for x in range(1,n):
  d[x] = x*x
print(d)

print(sum(d.values()))


# COMMAND ----------

# DBTITLE 1,Python Program to Multiply All the Items in a Dictionary
d= {}
n=12
for x in range(1,n):
  d[x] = x*x
print(d)
tot = 1
for i in d:
  tot = tot * d[i]
  
print(tot)

# COMMAND ----------

# DBTITLE 1,Python Program to Remove the Given Key from a Dictionary
d= {}
n=12
for x in range(1,n):
  d[x] = x*x
print(d)

key = 13
if key in d:
  del d[key]
else:
  print("key not found")
  
print("Updated dictionary")
print(d)  

# COMMAND ----------

# DBTITLE 1,Python Program to Form a Dictionary from an Object of a Class
class A(object):
  def __init__(self):
    self.a = 1
    self.b = 2
obj = A()

print(obj.__dict__)

# COMMAND ----------

# DBTITLE 1,Python Program to Map Two Lists into a Dictionary
lst1 = [1,2,3]
lst2 = [1,4,9]
d = dict(zip(lst1,lst2))
print(d)


# COMMAND ----------

# DBTITLE 1,Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
d = {}
string = "hello world program world test"
lst = list(string.split())

for x in lst:
  if x in d:
    d[x] +=1
  else:
    d[x] = 1
    
print(d)    

# COMMAND ----------

# DBTITLE 1,Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character
string = "Hello world this is a test string sanfoundry"
lst = list(string.split())

for x in lst:
  d[x[0]] = x
print(d)

# COMMAND ----------

# DBTITLE 1,Python Program to Count the Number of Vowels Present in a String using Sets
s = "Python Program"
vowels = set("aeiou")
count = 0
for x in s:
  if x.lower() in vowels:
    count +=1
    
print(count)

# COMMAND ----------

# DBTITLE 1,Python Program to Check Common Letters in Two Input Strings
s = "Test string"
s1 = "checking"
lst = list(set(s)&set(s1))

for x in lst:
  print(x)

# COMMAND ----------

# DBTITLE 1,Python Program that Displays which Letters are in the First String but not in the Second
s1 = "Test string"
s2 = "checking"

a=list(set(s1)-set(s2))

for x in a:
  print(x)

# COMMAND ----------

# DBTITLE 1,Python Program that Displays which Letters are Present in Both the Strings
s1 = "hello world"
s2 = "how are you"
a = list(set(s1)&set(s2))
for x in a:
  print(x)

# COMMAND ----------

# DBTITLE 1,Python Program that Displays which Letters are in the Two Strings but not in Both
s1 = "hello world"
s2 = "how are you"
a=list(set(s1)^set(s2))
print("The letters are:")
for i in a:
    print(i)

# COMMAND ----------

# DBTITLE 1,Python Program to Determine Whether a Given Number is Even or Odd Recursively
def check(n):
  if (n < 2):
    return (n % 2 == 0)
  return check(n-2)

n = 123
if check(n):
  print("%s is even"%n)
else:
  print("%s is odd"%n)

# COMMAND ----------

# DBTITLE 1,Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively
def occur(string,ch):
  if not string:
    return 0
  elif string[0] == ch:
    return 1 + occur(string[1:],ch)
  else:
    return occur(string[1:],ch)
  
  
n = "how are you"
print(occur(n,"o"))

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Fibonacci Series Using Recursion
# def fibonaci(n):
#   if n <=1:
#     return 1
#   return n * fibonaci(n-1)

def fibonaci(n):
  if n <=1:
    return n
  else:
    return fibonaci(n-1) + fibonaci(n-2)

for x in range(5):
  print(fibonaci(x),end=" ")

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Factorial of a Number Using Recursion
def factorial(n):
  if n <=1:
    return 1
  return n * fibonaci(n-1)

print(factorial(5))
  

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Sum of Elements in a List Recursively
def sum_of_element(arr,size):
  if size == 0:
    return 0
  return arr[size-1] + sum_of_element(arr,size -1)

sum_of_element([3, 56, 7],3)

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Binary Equivalent of a Number Recursively
l = []
def convert(b):
  if b == 0:
    return l.reverse()
  dig =  b % 2
  l.append(dig)
  convert(b//2)

convert(10) 
for x in l:
  print(x,end='')

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Sum of the Digits of the Number Recursively
total = 0
def sum_of_digits(n):
  global total
  if (n == 0):
    return total
  dig = n % 10
  total +=dig
  print(total)
  sum_of_digits(n//10)

sum_of_digits(123)
print(total)


# COMMAND ----------

# DBTITLE 1,Python Program to Find the LCM of Two Numbers Using Recursion
def lcm(a,b):
  lcm.multiple = lcm.multiple+ b
  print(lcm.multiple)
  if ((lcm.multiple % a == 0) and (lcm.multiple% b ==0)):
    return lcm.multiple
  else:
    print("else")
    print("else",lcm.multiple)
    lcm(a,b)
  return lcm.multiple

lcm.multiple=0
a , b = 75,35
if a > b:
  LCM = lcm(b,a)
else:
  LCM = lcm(a,b)
  
print(LCM)  

  

# COMMAND ----------

# DBTITLE 1,Python Program to Find the GCD of Two Numbers Using Recursion
def gcd(a,b):
  if b == 0:
    return a
  return gcd(b,a%b)

gcd(7,5)

# COMMAND ----------

# DBTITLE 1,Python Program to Find if a Number is Prime or Not Prime Using Recursion
def check(n, div = None):
    if div is None:
        div = n - 1
        print("1",div)
    print("2",div)
    while div >= 2:
        if n % div == 0:
            print("Number not prime")
            return False
        else:
            return check(n, div-1)
    else:
        print("Number is prime")
        return 'True'
      
check(13)      

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Product of two Numbers Using Recursion
def product(a,b):
  if a < b:
    product(b,a)
  elif( b != 0):
    return a + product(a,b-1)
  else:
    return 0
  
product(12,10)  
    

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Power of a Number Using Recursion
def power(base,exp):
  if exp == 1:
    return base
  if exp != 1:
    return (base * power(base, exp -1))
  
power(10,2)  

# COMMAND ----------

# DBTITLE 1,Python Program to Check Whether a String is a Palindrome or not Using Recursion
def is_palindrome(s):
  if len(s) < 1:
    return True
  else:
    if s[0] == s[-1]:
      return is_palindrome(s[1:-1])
  
  return False
  
if is_palindrome("madam"):
  print("String is a palindrome!")
else:
  print("String isn't  a palindrome!")

# COMMAND ----------

# DBTITLE 1,Python Program to Reverse a String Using Recursion
def reverse_string(s):
  if len(s) == 0:
    return s
  else:
    return reverse_string(s[1:]) + s[0]
  
reverse_string("yes")  

# COMMAND ----------

# DBTITLE 1,Python Program to Flatten a Nested List using Recursion
def flatten_list(s):
  if s == []:
    return s
  if isinstance(s[0],list):
    return flatten_list(s[0]) + flatten_list(s[1:])
  return s[:1] + flatten_list(s[1:])


S=[[1,2],[3,4]]
flatten_list(S)

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Total Sum of a Nested List Using Recursion
def sum_list(s):
  total = 0
  for item  in s:
    if type(item) == type([]):
      total = total + sum_list(item)
      
    else:
      total = total + item
  return total

S=[[1,2],[3,4]]
sum_list(S)

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Length of a List Using Recursion
def length(s):
  if s == []:
    return 0
  return 1 + length(s[1:])

length([1,2,3,4,5,6,7,8,9,0])

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Fibonacci Series without Using Recursion
def fibonaci(n):
  a = 0
  b = 1
  print(a,b,end =' ')
  while n - 2:
    c = a + b
    a = b
    b = c
    print(c,end=" ")
    n = n -1
fibonaci(10)    

# COMMAND ----------

# DBTITLE 1,Python Program to find the factorial of a number without recursion
def factorial(n):
  fact = 1
  while n > 0:
    fact = fact * n
    n = n - 1
  print(fact)
factorial(5)    

# COMMAND ----------

# DBTITLE 1,Python Program to Flatten a List without using Recursion
# [[1,2,3],[4,5]]
#result = [1,2,3,4,5]

S = [[1,2,3],[4,5],6]
def flatten_list(s):
  a = []
  for x in s:
    if type(x) == type([]):
      for y in x:
        a.append(y)
    else:
      a.append(x)
      
  return a

print(flatten_list(S))
      
flatten_list2 = lambda l : sum(map(flatten_list2,l),[]) if isinstance(l,list) else [l]      
flatten_list2(S)

# COMMAND ----------

# DBTITLE 1,Python Program to Reverse a String without using Recursion
def reverse_s(s):
  if s == '':
    return s
  return s[::-1]
reverse_s("sumit")

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Binary Equivalent of a Number without Using Recursion
a = []
n =10
while n > 0:
  dig = n % 2
  a.append(dig)
  n = n //2
  
for x in a[::-1]:
  print(x,end="")
  

# COMMAND ----------

# DBTITLE 1,Python Program to Find All Numbers which are Odd and Palindromes Between a Range of Numbers without using Recursion
l = 100
u = 150
a = []
for x in range(l,u+1):
  if x % 2 != 0:
    if str(x) == str(x)[::-1]:
      a.append(x)
      
print(a)      
  
  

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Sum of Digits in a Number without Recursion
n = 123
sum = 0
while n > 0:
  dig = n % 10
  sum  = sum + dig
  n = n // 10
  
print(sum)  

# COMMAND ----------

# DBTITLE 1,Class - Python Program to Find the Area of a Rectangle Using Classes
class Rectangle(object):
  def __init__(self,breadth,lenght):
    self.breadth = breadth
    self.lenght = lenght
    
  def area(self):
    return self.breadth * self.lenght
  
r = Rectangle(24,12)
r.area()
    

# COMMAND ----------

# DBTITLE 1,Python Program to Append, Delete and Display Elements of a List Using Classes
class check(object):
  def __init__(self):
    self.n = []
  def add(self,a):
    self.n.append(a)
    
  def remove(self,d):
    self.n.remove(d)
    
  def display(self):
    return (self.n)
  
c = check()
c.add(3)
c.add(4)
c.add(5)
c.display()
c.add(6)
c.add(7)
c.remove(5)
c.display()
  

# COMMAND ----------

# DBTITLE 1,Python Program to Create a Class and Compute the Area and the Perimeter of the Circle
import math 
class circle(object):
  def __init__(self,radius):
    self.radius = radius
    
  def area(self):
    return math.pi * (self.radius**2)
  
  def perimeter(self):
    return 2 * math.pi * self.radius
  
obj=circle(5)
print(obj.area())
print(obj.perimeter())


# COMMAND ----------

# DBTITLE 1,Python Program to Create a Class which Performs Basic Calculator Operations
class calculator(object):
  def __init__(self,a,b):
    self.a = a
    self.b =b
    
  def add(self):
    return self.a + self.b
  
  def sub(self):
    return self.a - self.b
  
  def mul(self):
    return self.a * self.b
  
  def div(self):
    return self.a /self.b
  
  
c = calculator(5,5)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())
    

# COMMAND ----------

# DBTITLE 1,Python Program to Create a Class and Get All Possible Subsets from a Set of Distinct Integers
class sub:
  def f1(self,s1):
    return self.f2([],sorted(s1))
  
  def f2(self,curr,s1):
    
    if s1:
      print("s1",curr,s1)
      return self.f2(curr,s1[1:]) + self.f2(curr + [s1[0]],s1[1:])
    print("out",curr)
    return [curr]
    

a = [4,5,6]
print(sub().f1(a))  

# COMMAND ----------

# DBTITLE 1, Linked List - Python Program to Read a Linked List in Reverse
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    
  def insert_at_beg(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head = new_node
      
  def display(self):
    curr = self.head
    while curr:
      print(curr.data,end = " ")
      curr = curr.next
      
      
l = LinkedList()  
l.insert_at_beg(10)
l.insert_at_beg(5)
l.insert_at_beg(2)
l.insert_at_beg(1)
l.display()

# COMMAND ----------

# DBTITLE 1,Python Program to Create a Linked List & Display the Elements in the List
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    self.last_node =None
    
  def append(self,data):
    new_node  = Node(data)
    if self.last_node is None:
      self.head = new_node
      self.last_node = self.head
    else:
      self.last_node.next = new_node
      self.last_node = self.last_node.next
      
  def display(self):
    curr = self.head
    while curr:
      print(curr.data,end = " ")
      curr = curr.next  
      
  def display_recursion(self):
    curr = self.head
    self.display_reversed_helper(curr)
    
  def display_reversed_helper(self,curr):
    if curr is None:
      return
    self.display_reversed_helper(curr.next)
    print(curr.data,end=" ")
      
  def find(self,key):
    curr = self.head
    return self.find_helper(curr,0,key)
  
  def find_helper(self,curr,start,key):
    if curr is None:
      return -1
    if curr.data == key:
      return start
    return self.find_helper(curr.next,start+1,key)
  
  def find_node(self,key):
    curr = self.head
    return self.find_node_helper(curr,key)
  
  def find_node_helper(self,curr,key):
    if curr is None:
      return None
    if curr.data == key:
      return curr
    return self.find_helper(curr.next,key)
  
  
  def find_iter(self,key):
    curr = self.head
    start = 0
    while curr :
        if curr.data == key:
          return start
        curr = curr.next
        start += 1
    return -1

  def lenght_iter(self):
    curr = self.head
    count = 0
    while curr:
      print(curr.data,end = " ")
      count += 1
      curr = curr.next   
    return count   
  
  def lenght_recursion(self):
    curr = self.head
    return self.lenght_recursion_helper(curr)
  
  def lenght_recursion_helper(self,curr):
    if curr is None:
      return 0
    return 1 + self.lenght_recursion_helper(curr.next)
  
  def occurrences_key(self,key):
    curr = self.head
    return self.occurrences_heplers(curr,key)
  
  def occurrences_heplers(self,curr,key):
    if curr is None:
      return 0
    if curr.data == key:
      return 1  + self.occurrences_heplers(curr.next,key)
    else:
      return self.occurrences_heplers(curr.next,key)

  def occurrences_iter(self,key):
    curr = self.head
    count = 0
    while curr:
      if curr.data == key:
        count += 1
      curr = curr.next  
    return count  
  
  def alternate(self):
    return self.alternate_helper(self.head)
  
  def alternate_helper(self,curr):
    if curr is None:
      return None
    print(curr.data,end = " ")
    if curr.next :
      self.alternate_helper(curr.next.next)
  
  def alternate_iter(self):
    curr = self.head
    while curr:
      print(curr.data,end=" ")
      curr = curr.next.next
    
  
# l = LinkedList()  
# l.append(10)
# l.append(5)
# l.append(2)
# l.append(1)
# l.display()      
# print(l.find(1))
# print(l.find_iter(10))
# print(l.find_node(10).data)
# l.display_recursion()
# l.lenght_recursion()

# COMMAND ----------

l = LinkedList()  
l.append(10)
l.append(5)
l.append(1)
l.append(3)
l.append(5)
l.append(1)
print(l.occurrences_key(10))
print(l.occurrences_iter(6))
l.alternate()
l.alternate_iter()

# COMMAND ----------

# DBTITLE 1,Python Program to Search for an Element in the Linked List using Recursion
# def find_helper(self,curr,start,key):
#     if curr is None:
#       return -1
#     if curr.data == key:
#       return start
#     return self.find_helper(curr.next,start+1,key)

# COMMAND ----------

# DBTITLE 1,Python Program to Search for an Element in the Linked List without using Recursion
# def find_iter(self,key):
#     curr = self.head
#     start = 0
#     while curr :
#         if curr.data == key:
#           return start
#         curr = curr.next
#         start += 1
#     return -1

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Length of the Linked List using Recursion
# def lenght_recursion(self):
#     curr = self.head
#     return self.lenght_recursion_helper(curr)
  
#   def lenght_recursion_helper(self,curr):
#     if curr is None:
#       return 0
#     return 1 + self.lenght_recursion_helper(curr.next)

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Length of the Linked List without using Recursion
# def lenght_iter(self):
#     curr = self.head
#     count = 0
#     while curr:
#       print(curr.data,end = " ")
#       count += 1
#       curr = curr.next   
#     return count

# COMMAND ----------

# DBTITLE 1,Python Program to Count the Number of Occurrences of an Element in the Linked List using Recursion
# def occurrences_heplers(self,curr,key):
#     if curr is None:
#       return 0
#     if curr.data == key:
#       return 1  + self.occurrences_heplers(curr.next,key)
#     else:
#       return self.occurrences_heplers(curr.next,key)

# COMMAND ----------

# DBTITLE 1,Python Program to Count the Number of Occurrences of an Element in the Linked List without using Recursion
#  def occurrences_iter(self,key):
#     curr = self.head
#     count = 0
#     while curr:
#       if curr.data == key:
#         count += 1
#       curr = curr.next  
#     return count  

# COMMAND ----------

# DBTITLE 1,Python Program to Print the Alternate Nodes in a Linked List using Recursion
# def alternate(self):
#     return self.alternate_helper(self.head)
  
#   def alternate_helper(self,curr):
#     if curr is None:
#       return None
#     print(curr.data,end = " ")
#     if curr.next :
#       self.alternate_helper(curr.next.next)

# COMMAND ----------

# DBTITLE 1,Python Program to Print the Alternate Nodes in a Linked List without using Recursion
# def alternate_iter(self):
#     curr = self.head
#     while curr:
#       print(curr.data,end=" ")
#       curr = curr.next.next

# COMMAND ----------

# DBTITLE 1,Python Program to Implement a Stack using Linked List
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
class Stack:
  def __init__(self):
    self.head = None
    
  def push(self,data):
    new_node = Node(data)
    curr = self.head
    if curr is None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head = new_node
      
  def pop(self):
    if self.head is None:
      return None
    else:
      curr  = self.head
      self.head = curr.next
      curr.next = None
      return curr
    
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop().data

  

# COMMAND ----------

# DBTITLE 1,Python Program to Implement Queue Data Structure using Linked List
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
class Queue:
  def __init__(self):
    self.head = None
    self.last = None
    
  def enqueue(self,data):
    new_node = Node(data)
    curr = self.head
    if curr is None:
      self.head = new_node
      self.last = self.head
    else:
      self.last.next = new_node
      self.last = self.last.next
      
  def dequeue(self):
    if self.head is None:
      return None
    else:
      curr  = self.head
      self.head = curr.next
      curr.next = None
      return curr
    
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue().data

  

# COMMAND ----------

# DBTITLE 1,Python Program to Implement Binary Tree using Linked List
class BinaryTree:
  def __init__(self,key=None):
    self.key = key
    self.left= None
    self.right = None
    
  def set_root(self,key):
    self.key = key
    
  def insert_left(self,new_node):
    self.left =new_node
    
  def insert_right(self,new_node):
    self.right =  new_node
  
  def inorder(self):
    if self.left is not None:
      self.left.inorder()
    print(self.key,end = ' ')
    if self.right is not None:
      self.right.inorder()
  
  def search(self,key):
    if self.key == key:
      return self
    if self.left is not None:
      temp = self.left.search(key)
      if temp is not None:
        return temp
      
    if self.right is not None:
      temp = self.right.search(key)
      if temp is not None:
        return temp  
    return None

btree = None
new_node = BinaryTree(10)
btree = new_node
btree.insert_left(BinaryTree(5))
btree.insert_right(BinaryTree(11))
btree.search(11).key

# COMMAND ----------

# DBTITLE 1,Python Program to Check whether 2 Linked Lists are Same
class Node:
  def __init__(self,data):
    self.data =data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    self.last_node = None
  
  def append(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.last_node = self.head
    else:
      self.last_node.next = new_node
      self.last_node = self.last_node.next
      
def is_equal(alist1,alist2):
  curr1 = alist1.head
  curr2 =  alist2.head

  while curr1 and curr2:
    if curr1.data != curr2.data:
      return False
    curr1 = curr1.next
    curr2 = curr2.next
  if curr1 is None and curr2 is None:
    return True
  else:
    return False
        
l1 = LinkedList()  
l2 = LinkedList() 
l1.append(1)
l1.append(3)
l1.append(5)
l1.append(7)

l2.append(1)
l2.append(3)
l2.append(5)
l2.append(7)
is_equal(l1,l2)

# COMMAND ----------

# DBTITLE 1,Python Program to Detect the Cycle in a Linked List
def has_cyclic(alist):
  slow = alist.head
  fast = alist.head
  while (fast != None and fast.next != None):
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False

l2 = LinkedList() 
l2.append(1)
l2.append(2)
l2.append(3)

if has_cyclic(l2):
  print('The linked list has a cycle.')
else:
  print('The linked list does not have a cycle.')

# COMMAND ----------


