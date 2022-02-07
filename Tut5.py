# Tut Questions:
'''
Keywords, Arguments, Functions:
Upon completion of the function, the control returns to the calling line
Return value, if any, is used where the function was called

Return statement serves two purposes:
Terminates the execution of the function and returns the control 
back to where the function was called, Returns a value to the caller 

def example(list_):
      for i in range(0, len(list_)):
            if(i>3):
                  return list_[i]
      return 0


def cost (a, b, c):
      totcost = a*c
      print("Item, and total cost are: ", b, totcost)
      
cost (1,2 ,3)
      
item = 5
qty = 3
unit = 200
totcost = cost(b=qty, a=item, c=unit)
# order of args not important
=> Item, and total cost are:  3 1000
(2, c = qty, b= unit)

All positional args must come first, then the keyword args
I.e. there cannot be any positional args after a keyword arg 
1 2 3 
[1, 2, 3]
=> [int(1), int(2), int(3)]
phy=[]
for i in info:
      phy.append(i["phy"])
'''
# Default parameter
def value(x, slope, intercept):
      return x*slope+intercept

x, m, c = [int(x) for x in input().split()]
print(value(x,  m ,c))

'''
Now, we pass do print(value(x, m))
=> Throw TypeError: missing 1 reqired positional arguement.
'''

def value(x, slope, intercept = 1): #Setting the default value of intercept to be 1.
      return x*slope+intercept

'''
With default parameters, now in case u want to pass intercept of your own choice.
Default value is taken when nothing is specified.
'''

# Ways to pass variable no of parameters to a function
#Approach 1: As discussed in the last tutorial
def sumList(list_):
      return sum(list_)

list_ = [int(x) for x in input().split()]
print(sumList(list_))

#Approach 2: Using *args:
'''
The special syntax *args in function definitions in python is used to 
pass a variable number of arguments to a function. It is used to pass 
variable-length argument list.  The syntax is to use the symbol * to take 
in a variable number of arguments; by convention, it is often used with the word args.
Using the *, the variable that we associate with the * becomes an iterable 
meaning you can do things like iterate over it,.
'''
def sumList(*args):
      print(args)
      return sum(args)
      
print(sumList(1, 2, 3, 4, 4, 32, 2, 32))

#Calculate SI using *args:
def simpleInterest(*args):
      return ((args[0]* args[1]* args[2])/100)

print(simpleInterest(1, 2, 3))

#List Comprehension: [<expression for each item> in <iterable> if condition == True]
'''
1 2 3 4 
[1, 2, 3, 4]
list_ = [int(x) for x in input().split()]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits if "a" in x]
x = "apple"


x.upper()

He says "something"
print("He says "something"")
" '' "
' "" '
" \  "
'''


# String and Tuples are Immutable in Python:
'''
a= (1,)
s="hello"
s[0] = 'b'

b = list(s)
b = ['h', 'e', 'l', 'l', 'o']
'#'.join(b) =>"h#e#l#l#o"
s[i] = 'a' => Error (String does not support item assignment)

Similarly, t = (1, 2, 3) => Is immutable, but elements may be mutable
t[0] = 6 => Error
t = ([1, 2, 3], 1, 3)
t[0] = [1,2, 3]

Workaround:
Convert it into a list
new_list = list(t) => then u can use any operation u can use on a normal list.
Similarly for lists, use that and then use list slicing

'''

#Dictionaries:
'''
Dr. Pankaj Jalote has a list of students information. These are the 
shortlisted students who are going to be an intern under him for 2 months,
to work on a project. The information is in the form of a list. But, this 
list is a special list. It is a list of dictionaries. This list contains information
about students in Physics, Chemistry and, Maths. Dr. Jalote wants to fetch the marks 
in each subject as a list. (Maybe he wants to find out how tough or easy the paper was, 
that years high school exams). Help find Dr. Jalote to fetch the marks and complete his 
objective. For this task we can use our old friend function for this purpose.

{"Phy": 70, "Chem": 90, "Maths": 100}
phy = []
for i in info:
      a.append(<subjectCode>)
for i in info:
      phy.append(i["Phy"])
      print(i["Phy"])
    
    info[key] = value  
'''

info = [{"Phy": 70, "Chem": 90, "Maths": 100},{"Phy": 72, "Chem": 10, "Maths": 90},{"Phy": 10, "Chem": 97, "Maths": 87}]

for i in info:
      print(i) # Get each dictionary 

def fetchMarks(listOfDict, subject):
      return [X[subject] for X in listOfDict if subject in X]

print(f"Marks for py in list form are{fetchMarks(info, 'Phy')}")
print(f"Marks for py in list form are{fetchMarks(info, 'Chem')}")
print(f"Marks for py in list form are{fetchMarks(info, 'Maths')}")
