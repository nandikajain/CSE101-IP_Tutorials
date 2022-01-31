# Tut Questions
'''
range(): range(start, end, step_size)
range= [start, end)

Loops revision:
a = [1, 2, 3, 60]
a = ["a", "b"]
for i in range(0, 10):
      print(i)

for i in a:
      print(a)
a
b
      
for i in range(len(a)):
      print(i, a[i])
0 , a
1, b

5
1
2
3
4
5

n
1 2 
listSum 

'''

# Normal sequential input:
a = []
n = int(input())
for i in range(n):
      ab = int(input())
      a.append(ab)
print(a)

'''
Shallow Copy, Deep Copy:


Lists are passed by shallow copy.
Two different lists, make 
a = []
b = []
a = b = 0

a = b = [] [INCORRECT APPROACH]
a.append(1)
print(b) -> 1
a = [1, 2, 3, 4]
b = a

b = a.copy() 
OR
a = b[:]
a and b point to the same element
'''

# Space separated input:
# 5 
# 1 2 3 4 5 [1, 2, 3, 4, 5]
# str.split(separator, maxsplit) : By default separator is " "
# 1#2#3 -> [1, 2#3] -> str.split('#', 1)

n = int(input())
a = []
a = [int(x) for x in input().split()]
print(a)

'''
1 2 3
a, b, c = [int(x) for x in input().split()] 
instead of 
l = [int(x) for x in input().split()]
a = l[0]
b = l[1]
c = l[2] 
'''
#Advantages: Cleaner code, saving time by single input
# List Sum:

def listSum(list_):
      sum_ = 0
      for i in list_:
            sum_+=i
      return sum_
      '''
      for i in range(len(list_)):
            sum_+=list_[i]
      '''
      # return sum(list_)
      
n = int(intput())
a = [int(x) for x in input().split()]
sum_value(listSum(a))
# What if float data type, how would you modify?
'''
a = 1.2
float(a)? 1.2
int(a)? 1
'''

# Some inbuilt functions: sort, sum
'''
len(a): Returns len of list

sum(a):
replace listSum by
return sum(list_)
a = [1, 2.3] -> Will add 3.3
but not strings

sort(a):
Inplace sort
returns null
a = [1, -2,0]
a.sort()
a would become -2, 0 ,1
a = ["world", "hello"]
a.sort()
a = ["hello", "world"]

Sort in Descending Order:
a.sort(reverse=True)
By default, ascending order.


string<separator>.join(iterable)
a = ['h', 'e', 'l', 'l', 'o']
"hello"
'.'.join(a)

'hello', 'h.e.l.l.o'


Reversing a list:
a = [1, 2, -1, 0]
a = a[::-1]
a.reverse() => [0, -1, 2, 1]
a.reverse(), reverses in place
'''

# Find min max using sort function:
n = int(input())
a = [int(x) for x in input().split()]
a.sort()
print("Min element is:", a[0])
print("Max element",a[-1] )

#f-string:
'''
Cleaner way of printing statements.

ans1 = 31418
ans2 = 

"Hello world 31418"
"Hello world 12 12 12 1 532 42 2 33 "
print("Hello world", end="")
print(ans)
print("Hello world", ans)

'''

print(f"Hello world {ans1}")
print(f"Sum of elements in the list is {sum(a)}")

#How to debug problems:
a = [-5, 1 , 12, 6]
b = []
for i in a:
      print(i, a[i])
      b.append(a[i])

'''    
APPROACH TO DEBUG:
1. Take sample input and dry run whatever
you wrote and see whats the problem
2. Add print statements to see if the functionality
you intended is being followed by your code.
'''

a = [-5, 1 , 12, 6]
for i in a:
      print(i)
      print(a[i])
      
'''
For students facing difficulties in list slicing can
refer to the first ans of: https://stackoverflow.com/questions/509211/understanding-slice-notation
and 
https://www.learnbyexample.org/python-list-slicing/
'''