# Databricks notebook source
# DBTITLE 1,Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
a  =  10
b = 5
a = a + b
b = a - b
a = a - b
print("a=",a,"b=",b)


# COMMAND ----------

# DBTITLE 1,Python Program to Read a Mumber n and Compute n+nn+nnn eg: 5+55+555
n = "5"
t1 = n+n
t2 = n+n+n
result = int(n) + int(t1)+int(t2)
print(result)

# COMMAND ----------

# DBTITLE 1,Python Program to Reverse a Given Number
n= 123
rev = 0
while n>0:
  dig = n%10
  print(dig)
  rev = rev*10 + dig
  print("rev",rev)
  n = n//10
  print("n",n)


# COMMAND ----------

# DBTITLE 1,Python Program to Print all Numbers in a Range Divisible by a Given Number
upper = 50
lower = 1
d = 5
for x in range(lower,upper+1):
  if x%5 == 0:
    print(x)

# COMMAND ----------

# DBTITLE 1,Python Program to Read Two Numbers and Print Their Quotient and Remainder
a = 10
b = 7

quotient = a//b
remiander = a%b
print(quotient)
print(remiander)

# COMMAND ----------

# DBTITLE 1,Python Program to Accept Three Digits and Print all Possible Combinations from the Digits
d = [1,2,3]

for i in range(0,3):
  for j in range(0,3):
    for k in range(0,3):
      if (i!=j and j!=k and k!=i):
        #print("i=",i,"j=",j,"k=",k)
        print(d[i],d[j],d[k])
      else:
        pass
        #print("i=",i,"j=",j,"k=",k)

# COMMAND ----------

# DBTITLE 1,Python Program to Print Odd Numbers Within a Given Range
n = 10

for x in range(1,n+1):
  if x % 2 != 0:
    print(x)

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Sum of Digits in a Number
num = 123
sum = 0
while num > 0:
  dig = num % 10
  sum = sum + dig
  num = num //10
  
print(sum)  
  
  



# COMMAND ----------

# DBTITLE 1,Python Program to Find the Smallest Divisor of an Integer
num = 77
lst = []
for i in range(2,num+1):
  if num % i == 0:
    lst.append(i)
    
lst.sort()
print("smallest divisor : ",lst[0])
    
    
    

# COMMAND ----------

# DBTITLE 1,Python Program to Count the Number of Digits in a Number
n = 123455666423523526346
count = 0
while n > 0:
  count = count +1
  n = n//10
  
print(count)  

# COMMAND ----------

# DBTITLE 1,Python Program to Check if a Number is a Palindrome
n = 567
temp = n
rev = 0
while n > 0:
  dig = n % 10
  rev = rev*10 + dig
  n = n//10

if temp == rev:
  print("The number is a palindrome!")
else:
  print("The number is not a palindrome!")

# COMMAND ----------

# DBTITLE 1,Python Program to Print all Integers that Aren’t Divisible by Either 2 or 3 and Lie between 1 and 50.
for x in range(1,51):
  if (x % 2 !=0) and (x % 3 != 0):
    print(x)

# COMMAND ----------

# DBTITLE 1,Python Program to Read a Number n And Print the Series “1+2+…..+n= “
n = 10
series = ""
sum = 0
for x in range(1,n+1):
  sum = sum + x
  if x != n:
    series += str(x)+ "+"
  else:
    series += str(x)+ "="

print(series+ str(sum))    
  

# COMMAND ----------

# DBTITLE 1,Python Program to Read a Number n and Print the Natural Numbers Summation Pattern
n = 10
series = ""
sum = 0
for j in range(1,n+1):
      
  for i in range(1,j+1):
    sum = sum +i 
    if i < j :
      series += str(i) + "+"
    else:
      series += str(i) + "="
      
  print(series + str(sum))
  series = ""
  sum = 0
  
  
    

# COMMAND ----------

# DBTITLE 1,Python Program to Print an Identity Matrix
n = 5
series = ""
for i in range(n):
  for j in range(n):
    if i == j:
      series += "1 "
    else:
      series += "0 "
  print(series)
  series = ""
      

# COMMAND ----------

# DBTITLE 1,Python Program to Print an Inverted Star Pattern
n = 10
for x in range(n,0,-1):
  print((n-x)* ' ' +x * "*")

# COMMAND ----------

# DBTITLE 1,Python Program to Read Print Prime Numbers in a Range using Sieve of Eratosthenes
n =10
sieve = set(range(2,n+1))
while sieve:
  prime = min(sieve)
  print(prime,end="\t")
  #print("before",sieve)
  sieve -= set(range(prime,n+1,prime))
  #print("after",sieve)

# COMMAND ----------

# DBTITLE 1,Python Program to Check if a Date is Valid and Print the Incremented Date if it is
#dd,mm,yy =  map(int,input().split("/"))
dd,mm,yy = 31,5,1993

if(mm ==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max1 = 31
elif (mm == 4 or mm == 6 or mm == 9 or mm == 11):
    max1 = 30
elif ((yy % 4 ==0 and yy%100 != 0) or yy%400 ==0):
    max1 = 29
else:
    max1 = 28

if (mm <1 or mm > 12):
   print("date is invalid")
elif(dd < 1 or dd > max1):
   print("date is in valid")
elif(dd == max1 and mm < 12):
   dd = 1
   mm = mm + 1
   print("Incremental date is :",dd,mm,yy)
elif(dd == max1 and mm == 12):
   dd = 1
   mm = 1
   yy = yy + 1
   print("Incremental date is :",dd,mm,yy)
else:
   dd = dd + 1
   print("Incremental date is :",dd,mm,yy)

# COMMAND ----------

# DBTITLE 1,Python Program to Compute Simple Interest Given all the Required Values
principal = 70000
rate =4
time = 1
simple_interest = (principal * time * rate) / 100
print(simple_interest)

# COMMAND ----------

# DBTITLE 1,Python Program to Check Whether a Given Year is a Leap Year
yy = 2016
if (yy % 4 == 0 and yy % 100 != 0) or (yy %400 == 0):
  print("leap year")
else:
  print("not a leap year")

# COMMAND ----------

# DBTITLE 1,Python Program to Read Height in Centimeters and then Convert the Height to Feet and Inches
h = 153 # in centimeters
inches = 0.394 * h
feet = 0.0328 * h
print("inches",round(inches,2),"feet=",round(feet,2))

# COMMAND ----------

# DBTITLE 1,Python Program to Take the Temperature in Celcius and Covert it to Farenheit
celcius= 32 # celcius
f = (celcius * 1.8) + 32
print("temperature in farenheit is :",f)

# COMMAND ----------

# DBTITLE 1,Python Program to Compute Prime Factors of an Integer
n = 315
i = 1

while i <= n:
  k = 0
#   print("k=",k)
#   print("i=",i)
  if n % i == 0:
    j = 1
#     print("j=",j)
    while j <= i:
      if i % j == 0:
#         print("inside if")
        k = k + 1
#         print("k in while ",k)
      j = j + 1
#       print("j in while ",j)
    if k == 2:
      print(i)
  i = i + 1
  
  

# COMMAND ----------

# DBTITLE 1,Python Program to Generate all the Divisors of an Integer
n= 25
for x in range(1,n+1):
  if n % x == 0:
    print(x)

# COMMAND ----------

# DBTITLE 1,Python Program to Print Table of a Given Number
n = 17

for x in range(1,11):
  print(n,"x",x,"=",n*x)

# COMMAND ----------

# DBTITLE 1,Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List
b = [-12,34,35,89]
s1 = 0
s2 = 0
s3 = 0
for x in b:
  if x < 0:
    s1 +=x
  elif x > 0 and x % 2 == 0:
    s2 += x
  elif x > 0 and x % 2 != 0:
    s3 += x
  else:
    print("Number is invalid")
print("sum of negative =",s1)
print("sum of even positive =",s2)
print("sum of odd positive =",s3)
    

# COMMAND ----------

# DBTITLE 1,Python Program to Print Largest Even and Largest Odd Number in a List
n = [45,20,80,93,3]
largest_even_so_far = 0
largest_odd_so_far = 0

for x in n:
  if x % 2 == 0:
    if largest_even_so_far < x:
      largest_even_so_far = x
  elif x % 2 != 0:
    if largest_odd_so_far < x:
      largest_odd_so_far = x
      
print("largest_even_so_far =",largest_even_so_far)   
print("largest_odd_so_far =",largest_odd_so_far)  

# COMMAND ----------

# DBTITLE 1,Python Program to Form an Integer that has the Number of Digits at Ten’s Place and the Least Significant Digit of the Entered Integer at One’s Place
#Python Program to Form an Integer that has the Number of Digits at Ten’s Place and the Least Significant Digit of the Entered Integer at One’s Place

n = 123
temp = n
k = 0
while n > 0:
  k +=1
  n = n // 10
b = str(temp)
c = str(k)
result = c+b[k-1]
print("The new number formed:",int(result))

# COMMAND ----------

# DBTITLE 1,Python Program to Find Those Numbers which are Divisible by 7 and Multiple of 5 in a Given Range of Numbers
n = 100

for x in range(1, n +1):
  if x % 7 == 0 and x % 5 ==0:
    print(x)

# COMMAND ----------

# DBTITLE 1,Python Program to Check if a Number is an Armstrong Number
n = 371
a =  list(map(int,str(n)))
b = list(map(lambda x : x**3,a))
print("b",b)
print("sum b",sum(b))
if sum(b) == n:
  print("The number is an armstrong number. ")
else:
  print("The number isn't an arsmtrong number. ")


# COMMAND ----------

# DBTITLE 1,Python Program to Print the Pascal’s triangle for n number of rows given by the user


n = 4
a =[]
for i in range(n):
  a.append([])
  print(a)
  a[i].append(1)
  for j in range(1,i):
    print("a[i-1] = ",a[i-1])
    print("[j-1] = ",[j-1])
    print("[j] = ",[j])
    a[i].append(a[i-1][j-1]+ a[i-1][j])
  if n!=0:
    a[i].append(1)

print("a",a)

for i in range(n):
  print("   "*(n-i), end =" ",sep = " ")
  for j in range(0,i+1):
    print('{0:5}'.format(a[i][j]),end=" ",sep=" ")
  print()    

# COMMAND ----------


#                  1 
#               1     1 
#            1     2     1 
#         1     3     3     1 

n = 4
l = []
for i in range(4):
  temp = []
  for j in range(0,i+1):
    if j == 0 or j == i:
      temp.append(1)
    else:
      temp.append(l[i -1][j-1] + l[i-1][j])
  l.append(temp)
print(l)
for x in range(n):
  print("   "* (n-x),end=" ",sep =" ")
  for y in range(0,x+1):
    print("{0:5}".format(l[x][y]),end= " ",sep = " ")
  print()
  
  

# COMMAND ----------

# DBTITLE 1,Python Program to Check if a Number is a Perfect Number
n = 25
sum = 0
for x in range(1,n):
  if n % x == 0:
    sum = sum + x
if sum == n:
  print("The number is a Perfect Number")
else:
  print("The number is not a Perfect Number")

# COMMAND ----------

# DBTITLE 1,Python Program to Check if a Number is a Strong Number
n = 234
sum1 = 0
temp = n
while n > 0:
  i = 1
  f = 1
  r = n % 10
  while i <= r:
    f = f * i
    i = i + 1
  sum1 = sum1 + f  
  n = n // 10  

print(sum1)
if temp == sum1:
  print("The number is a Strong Number")
else:
  print("The Number is not a Strong Number")

# COMMAND ----------

# DBTITLE 1,Python Program to Find the LCM of Two Numbers
a = 12
b = 18
if a > b:
  min1 = b
else:
  min1 = a
  
while (1):
  if min1 % a == 0 and min1 % b == 0:
    print("lcm :",min1)
    break
  min1 = min1 + 1
  

# COMMAND ----------

# DBTITLE 1,Python Program to Find the GCD of Two Numbers
a = 30
b = 35


def gcd(a,b):
  if b == 0:
    return a
  return gcd(b,a%b)

print(gcd(a,b))


# COMMAND ----------

# DBTITLE 1,Python Program to Compute a Polynomial Equation given that the Coefficients of the Polynomial are stored in a List
print("Enter the coefficients of the form ax^3 + bx^2 + cx + d")
c= [2,5,6,3]
j = 3
x = 1
sum1 = 0
for i in range(0,3):
  sum1 = sum1 + (c[i]* (x**j))
  j = j - 1
  
sum1 = sum1 + c[3]
print("The value of the polynomial is:",sum1)


# COMMAND ----------

# DBTITLE 1,Python Program to Check If Two Numbers are Amicable Numbers
x  = 284
y = 220
sum1 = 0
sum2 = 0
for i in range(1,x):
  if x % i == 0:
    sum1 +=i

for j in range(1,y):
  if y % j == 0:
    sum2 +=j    
    
print(sum1)
print(sum2)
if sum1 == y and sum2 == x:
  print("Amicable")
else:
  print("not Amicable")

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Area of a Triangle Given All Three Sides using Heron's formula

a,b,c = 15,7,9
#half of the triangles perimeter
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**(1/2)
print("Area of a traingle",round(area,2))

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Gravitational Force Acting Between Two Objects
m1,m2,r = 1000000,500000,20
G = 6.673*(10**11)
f = (G*m1*m2)/(r**2)
print(f)
print("Hence, the gravitational force is: ",f,"N")

# COMMAND ----------

# DBTITLE 1,Python Program to Check if a Number is a Prime Number
n = 25
k = 0
for x in range(2,n//2 + 1):
  if n % x == 0:
    k = k + 1
    
if k <=0:
  print("prime")
else:
  print("not prime")
    
    
    

# COMMAND ----------

# DBTITLE 1,Python Program to Print all the Prime Numbers within a Given Range
n = 23
for a in range(2,n+1):
  k = 0
  for x in range(2,a//2 +1):
    if a % x ==0:
      k = k + 1
  if k <=0:
    print(a,end=" ")
  


# COMMAND ----------

# DBTITLE 1,Python Program to Print Numbers in a Range (1,upper) Without Using any Loops
def printno(upper):
  if upper > 0:
    printno(upper - 1)
    print(upper)
upper = 5
printno(upper)

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Sum of Sine Series
#sin(x) = (((-1)**k)/(2k +1)!)* x**2k+1
import math

def sin(x,n):
  sine = 0
  for i in range(n):
    sign  = (-i)**i
    # convert degree to radians
    pi = 22/7
    y = x*(pi/180)
    sine = sine + ((y**(2*i + 1))/ math.factorial(2*i + 1)) * sign
  return sine

x = 30 # in g=degree
n = 10 # no of term
print(round(sin(x,n),2))

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Sum of Cosine Series
#cos(x) = (((-1)**k)/(2k)!)* x**2k

def cosine(x,n):
  cosx = 0
  for i in range(n):
    sign  = (-1)**i
    pi = 22/7
    y = x*(pi/180)
    cosx = cosx + ((y**(2*i))/math.factorial(2*i)) * sign
  return cosx

x = 0
n = 10
print(round(cosine(x,n),2))

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Sum of First N Natural Numbers
n = 167

s = (n * (n+1))/2
print(s)


# COMMAND ----------

# DBTITLE 1,Python Program to Find the Sum of the Series: 1 + 1/2 + 1/3 + ….. + 1/N
n= 15
sum = 0

for i in range(1,n+1):
  sum = sum + 1/i
print(round(sum,2))

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Sum of the Series: 1 + x^2/2 + x^3/3 + … x^n/n
n= 5
x = 2
sum1 = 1

for i in range(2,n+1):
  sum1 = sum1 + ((x**i)/i)
print(round(sum1,2))

# COMMAND ----------

# DBTITLE 1,Python Program to Compute the Value of Euler’s Number e. Use the Formula: e = 1 + 1/1! + 1/2! + …… 1/n!
n= 5
sum1 = 1

for i in range(1,n+1):
  sum1 = sum1 + 1/math.factorial(i)
print(round(sum1,2))

# COMMAND ----------

# DBTITLE 1,Python Program to Determine all Pythagorean Triplets in the Range
limit  =  20
c= 0
m = 2

while c < limit:
  
  for n in range(1,m):
    print("m",m,"--n",n)
    a  = m*m - n*n
    b = 2 * m* n
    c = m*m + n*n
    print("a",a)
    print("b",b)
    print("c",c)
    if c > limit:
      break
#     if (a ==0 or b ==0 or c== 0):
#       break
    print(a,b,c)
  m = m + 1   
      

# COMMAND ----------

# DBTITLE 1,Python Program to Search the Number of Times a Particular Number Occurs in a List
s = 12
lst = [1,2,3,6,23,24, 3, 12, 22, 12]
count = 0
for x in lst:
  if x == s:
    count +=1
    
print(count)    

# COMMAND ----------

# DBTITLE 1,Python Program to test Collatz Conjecture for a Given Number
# The Collatz conjecture is a conjecture that a particular sequence always reaches 1. The sequence is defined as: start with a number n. The next number in the sequence is n/2 #if n is even and 3n + 1 if n is odd.
n = 5

def collatz(n):
  while n > 1:
    print(n,end=" ")
    if n % 2 :
      # n is odd
      n = 3*n + 1
    else:
      #n is even
      n = n/2
  print(1,end= "")    
      
      
collatz(n)      

# COMMAND ----------

# DBTITLE 1,Python Program to Count Set Bits in a Number
#remove the set bits
#Brian Kernighan’s Algorithm:
n = 11
def count_bits(n):
  count = 0
  while n > 0:
    n &= n -1
    count+=1
  print(count)  
count_bits(n)

# COMMAND ----------

# DBTITLE 1,Python Program to Find Whether a Number is a Power of Two
def is_power_of_two(n):
  if n <= 0:
    return False
  else:
    print(n&n-1)
    return n & (n - 1) == 0

n = 16
if is_power_of_two(n):
  print('{} is a power of two.'.format(n))
else:
  print('{} is not a power of two.'.format(n))
  
  

# COMMAND ----------

# DBTITLE 1,Python Program to Clear the Rightmost Set Bit of a Number 
def clear_rightmost_set_bits(n):
  return n & (n-1)
n = 14
ans = clear_rightmost_set_bits(n)
print('n with its rightmost set bit cleared equals:', ans)

# COMMAND ----------

# DBTITLE 1,Python Program to Generate Gray Codes using Recursion
def get_gray_codes(n):
  if n == 0:
    return ['']
  first_half = get_gray_codes(n-1)

  print("first",first_half)
  second_half = first_half.copy()
  print("second_half",first_half)
  first_half = ['0' + code for code in first_half]
  second_half = ['1'+ code for code in reversed(second_half)]
  
  return first_half + second_half
n = 4
print(get_gray_codes(n))

# COMMAND ----------

# DBTITLE 1,Python Program to Generate Gray Codes with out Recursion
#Generate Gray code with out recursion
def generate_gray_code(n):
  a = ['']
  for x in range(1,n+1):
    f = ['0' + c for c in a]
    s = ['1' + c for c in reversed(a) ]
    a = f + s
  return a
print(generate_gray_code(4))

# COMMAND ----------

# DBTITLE 1,Python Program to Convert Gray Code to Binary
def gray_to_binary(n):
  n  =  int(n,2) # convert to int
  print(n)
  mask =  n
  while mask != 0:
    print("mask-b",mask)
    mask >>= 1
    print("mask-a",mask)
    n ^=mask
    print("n",n)
  print(n)
  print(bin(n)[2:])
  return bin(n)[2:]

g = '101'
b = gray_to_binary(g)
print('In binary:', b)
  
  
  

# COMMAND ----------

# DBTITLE 1,Python Program to Convert Binary to Gray Code
def binary_to_gray(n):
    """Convert Binary to Gray codeword and return it."""
    n = int(n, 2) # convert to int
    print("n",n)
    print("(n >> 1)",(n^ n>> 1))
    n ^= (n >> 1)
 
    # bin(n) returns n's binary representation with a '0b' prefixed
    # the slice operation is to remove the prefix
    return bin(n)[2:]
 
 
g = '110'
b = binary_to_gray(g)
print('Gray codeword:', b)

# COMMAND ----------

# DBTITLE 1,ith bit is set or not

def is_bit_set(n,k):
  mask = 1
  mask <<= k
  print(mask)
  print(n&mask)
  if n & mask:
    print('yes')
  else:
    print('No')
    
is_bit_set(8,3)    

# COMMAND ----------

# DBTITLE 1,Find rightmost different bit between 2 numbers
is_match = True
while True:
  if (a & mask) == (b & mask):
    mask <<=1
  else:
    is_match = False
    break
    
if is_match:
  print("yes")
else:
  print("No")

# COMMAND ----------

#conversion of binary to gray code
n = '100101'
gray = n[0]
for x in range(len(n)-1):
  gray += str(int(n[x]) ^ int(n[x+1])) 
print(gray)  

# COMMAND ----------

#conversion of gray to bibary code
n = '110111'
gray = n[0]
for x in range(len(n)-1):
  print(gray)
  gray += str(int(gray[x]) ^ int(n[x+1])) 
print(gray) 

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Largest Number in a List
a = [1,34,5,6,8,5,746,4,6,866,353,24,233]
a.sort()
print(a[-1])

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Second Largest Number in a List
a = [1,34,5,6,8,5,746,4,6,866,353,24,233]
a.sort()
print(a[-2])

# COMMAND ----------

# DBTITLE 1,Python Program to Put Even and Odd elements in a List into Two Different Lists
even = []
odd = []
lst = [1,34,5,6,8,5,746,4,6,866,353,24,233]
for x in lst:
  if x % 2 == 0:
    even.append(x)
  else:
    odd.append(x)
    
print(even)
print(odd)

# COMMAND ----------

# DBTITLE 1,Python Program to Merge Two Lists and Sort it
a= [1,3,5,7,9]
b = [2,4,6,8]
new = a+b
new.sort()
print(new)

# COMMAND ----------

# DBTITLE 1,Python Program to Sort the List According to the Second Element in Sublist
a=[['A',34],['B',21],['C',26]]

for i in range(0,len(a)):
  for j in range(0,len(a)-i-1):
    if (a[j][1] > a[j+1][1]):
      temp = a[j]
      a[j] = a[j+1]
      a[j+1] = temp
      
print(a)      

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Second Largest Number in a List Using Bubble Sort
a = [3,4,3,6,7,2,1,9]
for i in range(0,len(a)):
  for j in range(0,len(a)-i-1):
    if (a[j]> a[j+1]):
      temp = a[j]
      a[j] = a[j+1]
      a[j+1] = temp

print(a[-2])      

# COMMAND ----------

# DBTITLE 1,Python Program to Sort a List According to the Length of the Elements
a = ["Apple","Ball","Cat","Dog"]
a.sort(key = len)
print(a)

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Union of two Lists
a = [1,3,5,7,9]
b = [2,4,6,8]

new = list(set().union(a,b))
print(new)

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Intersection of Two Lists
a = [1,3,5,7,9,2]
b = [2,4,6,8,3]

new = list(set(a) & set(b))
print(new)

# COMMAND ----------

# DBTITLE 1,Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number
#Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number
n = 10
tup = []
for x in range(1,n+1):
  tup.append((x,x*x))
  
print(tup)  


# COMMAND ----------

# DBTITLE 1,Python Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10
#Python Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10
a = []
l= 50
u= 700
for x in range(l,u+1):
   if (int(x**(1/2))**2 == x) and sum(list(map(int,str(x))))<10:
      print(x**(1/2))
      a.append(x)
    
print(a)    

# COMMAND ----------

# DBTITLE 1,Python Program to Find the Cumulative Sum of a List where the ith Element is the Sum of the First i+1 Elements From The Original List
a = [1,2,3,4,5]
new_list = [sum(a[:x+1]) for x in range(0,len(a))]
print("original",a)
print("new_list",new_list)

# COMMAND ----------

# DBTITLE 1,Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List
import random
a = [random.randint(1,20) for _ in range(10)]
print(a)

# COMMAND ----------

# DBTITLE 1,Python program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple
# def last(n):
#   print(n)
#   print(n[-1])
#   return n[-1]  
 
   
# def sort(tuples):
#   return sorted(tuples,key=last)

def sort(tuples):
  return sorted(tuples,key=lambda x : x[-1])

a =[(2,5),(1,2),(4,4),(2,3)]
print(sort(a))

# COMMAND ----------

# DBTITLE 1,Python Program to Swap the First and Last Value of a List
a = [1,2,3,4,5]
temp = a[0]
a[0] = a[-1]
a[-1] = temp
print(a)

# COMMAND ----------

# DBTITLE 1,Python Program to Remove the Duplicate Items from a List
a = [1,2,3,3,4,4,5,5,6,7,7,7,8,8,9,5,10]

b = set()
unique = []
for x in a:
  if x not in b:
    unique.append(x)
    b.add(x)

print(unique)
               
               
               
               
  

# COMMAND ----------

# DBTITLE 1,Python Program to Read a List of Words and Return the Length of the Longest One
a = ["Apple","ball","cat","donkey","banana","dog","elephant"]
longest_so_far = 0
for x in a:
  if len(x) > longest_so_far:
    longest_so_far = len(x)
    
print("longest lenght",longest_so_far)    

# COMMAND ----------

# DBTITLE 1,Python Program to Remove the ith Occurrence of the Given Word in a List where Words can Repeat
a = ["apple","apple","ball","ball","cat","banana"]
r = 2
elem = 'ball'
count = 0
new = []
for x in a:
  if x == elem:
    count +=1
    if count != r:
      new.append(x)
  else:
    new.append(x)
    
print("rmove the occurrance",r)    
print("rmove the elem",elem)    
print("original",a)    
print("new",new)    
    

# COMMAND ----------

# DBTITLE 1,Python Program to Remove All Tuples in a List of Tuples with the USN Outside the Given Range
y=[('a','12CS039'),('b','12CS320'),('c','12CS055'),('d','12CS100')]
low = 50
up=150
l = '12CS0' + str(low)
u = '12CS' + str(up)

p = [x for x in y if x[1] > l and x[1] < u ]
print(p)

# COMMAND ----------

# DBTITLE 1,Python Program to solve Maximum Subarray Problem using Divide and Conquer


def max_subarray(arr,start,end):
  if start == end -1:
    return start,end,arr[start]
  else:
    mid = (start + end) // 2
    left_start,left_end, left_max = max_subarray(arr,start,mid)
    right_start,right_end, right_max = max_subarray(arr,mid,end)
    cross_start,cross_end, cross_max = max_cross_subarry(arr,start,mid,end)
    if left_max > right_max and left_max > cross_max:
      return left_start,left_end,left_max
    elif right_max > left_max and right_max > cross_max:
      return right_start,right_end, right_max
    else:
      return cross_start,cross_end, cross_max
    
def max_cross_subarry(arr,start,mid,end):
  sum_left = float('-inf')
  sum_temp = 0
  cross_start = mid
  
  for x in range(mid-1,start -1,-1):
    sum_temp = sum_temp + arr[x]
    if sum_temp > sum_left:
      sum_left = sum_temp
      cross_start = x
      
  sum_right = float('-inf')
  sum_temp = 0
  cross_end = mid + 1
  
  for x in range(mid,end):
    sum_temp = sum_temp + arr[x]
    if sum_temp > sum_right:
      sum_right = sum_temp
      cross_end = x    
      
  return cross_start,cross_end,(sum_left + sum_right)
y = [3, 4, -2, 3, -10, 32, 4 ,-11 ,7 ,-3 ,2]
max_subarray(y,0,len(y))

# COMMAND ----------

# DBTITLE 1,Python Program to solve Maximum Subarray Problem using Greedy Alogrithms
y = [3, 4, -2, 3, -10, 32, 4 ,-11 ,7 ,-3 ,2]

def max_subarry_greedy(arr,start,end):
  if start == end -1:
    return arr[start]
  
  curr_sum = arr[0]
  max_sum = arr[0]
  for x  in range(1,end-1):
    
    curr_sum = max(curr_sum+ arr[x], arr[x])
    if curr_sum > max_sum:
      max_sum = curr_sum
      
  return max_sum    

max_subarry_greedy(y,0,len(y))

# COMMAND ----------

# DBTITLE 1,Python Program to solve Maximum Subarray Problem using Kadane Alogrithms
y = [3, 4, -2, 3, -10, 32, 4 ,-11 ,7 ,-3 ,2]
def max_subarry_kadane(arr,start,end):
  if start == end -1:
    return arr[start]
  
  curr = max_sum = arr[0]
  for x  in range(1,end-1):
    if curr>0:
      curr = curr + arr[x]
    else:
      curr = arr[x]
    if curr > max_sum:
      max_sum = curr
      
  return max_sum    

max_subarry_kadane(y,0,len(y))

# COMMAND ----------

# DBTITLE 1,Python Program to Find Element Occurring Odd Number of Times in a List

def find_odd_occurring(alist):
  ans = 0
  for elem in alist:
    ans^=elem
    
  return ans

alist = [15, 22, 10 ,33 ,22, 33, 15, 1, 1, 15, 15]
find_odd_occurring(alist)

# COMMAND ----------

# DBTITLE 1,Python Program to Replace all Occurrences of ‘a’ with $ in a String
s1 = "Apple"
s2 = "Asia"
print(s1.replace("A","$"))
print(s2.replace("a","$"))

# COMMAND ----------

# DBTITLE 1,Python Program to Remove the nth Index Character from a Non-Empty String
s = "sumit"
def remove(s,n):
  first = s[:n]
  second = s[n+1:]
  return first + second
print(remove(s,3))

# COMMAND ----------

# DBTITLE 1,Python Program to Detect if Two Strings are Anagrams
s1 = 'dod'
s2 = 'odd'
if sorted(s1)==sorted(s2):
  print("The string is anagrams")
else:
  print("The string is not anagrams")

# COMMAND ----------

# DBTITLE 1,Python Program to Form a New String where the First Character and the Last Character have been Exchanged
t = "sumit"
def exchange(s):
  f = s[0]
  sec = s[-1]
  return (sec +  s[1:-1] + f)

exchange(t)

# COMMAND ----------

# DBTITLE 1,Python Program to Count the Number of Vowels in a String
t = "sumit"
def count_vowel(t):
  count = 0
  for x in t:
    if x in ['a','e','i','o','u']:
      count +=1
  return count  

count_vowel(t)

# COMMAND ----------

# DBTITLE 1,Python Program to Take in a String and Replace Every Blank Space with Hyphen with out using replace
s = "s u m i     t"
def replace_space(s):
  string  = ""
  for x in s:
    if x == " ":
      string +="-"
    else:
      string += x
      
  return string
replace_space(s)

# COMMAND ----------

# DBTITLE 1,Python Program to Calculate the Length of a String Without Using a Library Function
def len_of_string(s):
  count = 0
  for x in s:
    count +=1
  return count  

s = "sumit"
len_of_string(s)

# COMMAND ----------

# DBTITLE 1,Python Program to Remove the Characters of Odd Index Values in a String
def remove_odd(s):
  count = 0
  string = ""
  for x in s:
    if count % 2 == 0:
      string += x
    count +=1  
      
  return string
s = "maurya"
remove_odd(s)    

# COMMAND ----------

# DBTITLE 1,Python Program to Calculate the Number of Words and the Number of Characters Present in a String
s = "I love python"
char = 0
word = 1

for x in s:
  char +=1
  if x == " ":
    word +=1
    
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)    

# COMMAND ----------

# DBTITLE 1,Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
s1 = "Bangalore"
s2 = "Delhi"
def largest(s1,s2):
  t1 = 0
  t2 = 0
  for x in s1:
    t1 +=1
  for  x in s2:
    t2 +=1
  if t1 > t2:
    return s1
  else:
    return s2
    
largest(s1,s2)    

# COMMAND ----------

# DBTITLE 1,Python Program to Count Number of Lowercase Characters in a String
s = "SumiT"
count = 0
for x in s:
  if x.islower():
    count +=1
    
    
print(count)    
    

# COMMAND ----------

# DBTITLE 1,Python Program to Check if a String is a Palindrome or Not
import math
s = "madam"
# if s == s[::-1]:
#   print("Palindrome")
# else:
#   print("Not Palindrome")
alist = list(s)
lenght = len(alist)
flag = True
for x in range(lenght):
  if x < math.ceil(lenght/2):
    if alist[(lenght-1)-x] != alist[x]:
      flag = False
      break
if flag :
  print("Palindrome")
else:
  print("Not Palindrome")

# COMMAND ----------

# DBTITLE 1,Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String
s = "SumiT"
l = 0
u =0
for x in s:
  if x.islower():
    l +=1
  elif x.isupper():
    u +=1
    
    
    
print(l)   
print(u)   

# COMMAND ----------

# DBTITLE 1,Python Program to Check if a String is a Pangram or Not
from string import ascii_lowercase as asc_lower
s = "The quick brown fox jumps over the lazy dog"
def check(s):
  return set(asc_lower) - set(s.lower()) == set([])

if check(s):
  print("Pangram")
else:
  print("Not Pangram")


# COMMAND ----------


