# Tut Questions
'''
Q1: Given a list of n integers and an integer x, we want to 
make every number in the list equal to x. In one step we can
either increase or decrease an element in the list by 2.
Find the minimum number of steps required to make every
element in the list equal to x or tell if it is impossible to do so.

Odd +  2 = Odd
Even + 2 = Even

a[0] = 2 
x = 6
  
'''

array = [1,1,2, 2131]
x = int(input("Enter the value of x: "))
no_of_steps = 0
flag_impossible = 0
pos_diff  = 0
for i in array: 
      pos_diff = abs(i-x)
      if ((pos_diff % 2) == 0):
            no_of_steps+=(pos_diff)//2
      else:
            flag_impossible = 1
            print("Impossible to achieve")
            break

if(flag_impossible == 0):
      print(no_of_steps)
            

'''
Q2: Given a number N, print the whole Fibonacci sequence for N.
Sample Input:  
5
Sample Output:
0 
1
1
2
3
for i in list_:
      print(i, end=" ")

0 1 1 2 3
a = 0
b = 1
a = b
b = 0+1 (a+b)
0 1 

a, b, a+b, 
0, 1, 1, 2 , 


'''
# Fibonacci: Fib(N) = Fib(N-1) + Fib (N-2), given N>2, and Fib(1) = 0, Fib(2) = 1

print()
N = int(input("Enter value of N: "))
a = 0
b = 1
print(a)
while(N-1):
      print(b)
      c = a + b
      a = b
      b = c
      N-=1  # N = N-1 
      
'''
Q3: Given a list of n integers, find the sum of the elements 
of the list excluding the segments that starts with 10 and 
ends with 20.

1, 2, 10, 32, 12, 20, 12
1, 2, 10, 20, 20, 12
'''
print()
array = [10,2,1,1, 2,1,  10, 20, 20]
# [20, 1, 10]
first_10 = -1
last_20 = -1
sum_ = 0
for i in range(0, len(array)):
      if(array[i] == 10):
            first_10 = i
            break
#range(start, end, step)
for i in range(len(array) -1, -1, -1):
      if(array[i] == 20):
            last_20 = i
            break

print("First 10 is:", first_10, "Last 20 is:", last_20)
if(last_20 == -1 or first_10 == -1 or last_20 < first_10):
      for i in array:
            sum_+=i
else:
      for i in range(0, len(array)):
            if(i< first_10 or i>last_20):
                  sum_+= array[i]

print("Sum is:", sum_)