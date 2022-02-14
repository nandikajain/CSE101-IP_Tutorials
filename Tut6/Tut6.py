# Tut Questions:
'''
File IO: 
'r' -> represents read only mode
'w' -> represents write only mode
FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'

seek -> pointer
'''
# file_notPresent = open("somefile.txt", 'r')

# file_present = open("intro_toProg.txt", "r")
# print(file_present.read()) #Read the whole file.
# print(file_present.readline()) #Read one line in the file.

# file_present.seek(0)
# print(file_present.readline()) #Read one line in the file.

'''Print using for loops.'''
# file = open('intro_toProg.txt', 'r')
# for line in file:
#     print(line)

'''Reading file after closing.'''

# file = open("intro_toProg.txt", "r")
# print(file.read()) 
# file.close()
# print(file.read()) #Can't read the file 

'''Reading n characters'''
# file = open("intro_toProg.txt", "r")
# print(file.read(5))
# print(file.read())

'''Using close:
closing the file is necessary so 
subsequent accesses will NOT miss the updates (adds, changes, deletes) you've made to it.

The file close writes to the file on disk.
Basically, your write operations will change a hidden buffer. 
At some cadence, the buffer is written to the file on disk. 
If your program does not close the file, some of the data that 
you thought was written to the file on disk was not actually written.
'''

'''
You are being provided a text file which contains the famous sonnet, OZYMANDIAS,
written by the great P.B. Shelley.
You are required to:
-Find the number of lines in the text file.
-Find the longest word(s) in the poem.
-Find the frequency of each of the words in the poem and return it as a dictionary
'''
from collections import Counter as ctr
# Finding no of lines
# Approach 1: finding '\n':
file = open('ozymandias.txt','r') #Opening the file in read mode.
info = file.read()
# l_lines = info.split("\n")
# print("Number of lines: ", len(l_lines))
# file.close()

# Approach 2: Using for loop:

# file = open('ozymandias.txt','r') #Opening the file in read mode.
# no_of_lines=0
# for line in file:
#       print(line)
#       no_of_lines+=1
# print("Number of lines: ", no_of_lines)
# file.close()

#Approach 3: readlines() -> returns an array
# file = open('ozymandias.txt','r') #Opening the file in read mode.
# list_of_lines = file.readlines()
# print(list_of_lines)
# print(len(list_of_lines))

wordList = info.split()
# length_max = len(max(wordList, key=len))
max_ = INT_MIN
for i in wordList:
      if(len(i)>max_):
            max_ = len(i)

ans= [i for i in wordList if len(i) ==max_]
'''
Max length word:
max()
max(iterable[, key=func]) -> value

So, the key=func basically allows us to pass an optional 
argument key to the function on whose basis is the given iterator/arguments 
are sorted & the maximum is returned.

Stack overflow link to follow:
https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression
'''
# Printing the frequency of words:
'''
class collections.Counter
It is a collection where elements are stored as dictionary 
keys and their counts are stored as dictionary values.
'''
# Approach 1: Using inbuilt counter from Collections.
# wordFreq = ctr(info.split())
# print("Frequency of each of the words: ")
# print(wordFreq)

# Approach 2: Maintain your own counter:
# counter_ = dict()
# for word in info.split():
#       if(word in counter_):
#             counter_[word] +=1
#       else:
#             counter_[word] = 1            
# print(counter_)
