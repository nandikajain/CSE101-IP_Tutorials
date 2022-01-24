# Tut 3 Questions
'''
Usually, when you buy something, you're asked whether
your credit card number, phone number, or answer to your
most secret question is still correct. However, since someone could
look over your shoulder, you don't want that shown on your screen.
Instead, we mask it. Your task is to write a function maskify(),
which changes all but the last four characters into '#'.
Example
maskify("4556364607935616") => "############5616"
maskify("64607935616") => "#######5616"
maskify("1") =>"1"
maskify("") => ""
'''

# Approach 1: Using if-else
def maskify(string_to_mask):
      masked_string = ''
      if len(string_to_mask)>4:
            for i in string_to_mask[:len(string_to_mask)-4]:
                  masked_string = masked_string+'#'
            for i in string_to_mask[len(string_to_mask)-4:len(string_to_mask)]:
                  masked_string = masked_string+i
      else:
            masked_string = string_to_mask
      return masked_string

# Approach 2: Use of Join
# string<separator>.join(iterable)
# a = ['h', 'e', 'l', 'l', 'o']
# "hello"
# ''.join(a)

# 'hello', 'h.e.l.l.o'

def maskify(string_to_mask):
      word = list(string_to_mask)
      for i in range(len(word) - 4):
            word[i] = '#'
      return ''.join(word)


#Approach 3:
def maskify(cc):
      l = len(cc)
      if l <= 4: 
            return cc
      else:
            return (l - 4) * '#' + cc[-4:]


'''
Deoxyribonucleic acid (DNA) is a chemical found in the 
nucleus of cells and carries the "instructions" for the 
development and functioning of living organisms. In DNA strings, 
symbols "A" and "T" are complements of each other, as "C" and "G". You take
input a string, as one side of the DNA; you need to return the other 
complementary side. DNA strand is never empty or there is no DNA at 
all.(i.e, if the input is an empty string, “”, then simply print out the empty string)
Also, if the input DNA string contains some wrongly encoded character, it prints out
“Wrong Encoding”.
Example (input -> output)
"ATTGC" → "TAACG"
"GTAT" → "CATA"
“ATGC” →”TACG”
“GTAT” → “CATA”
“AAAA” → “TTTT”
“” → “” ## empty string

0, 1, 2, 3, 4
a = "hello" =>5
a[1] = 'e'

ATTT => 4
for i in range(4):
      0,1, 2, 3
comp_dna = 'AT'
comp_dna = 'AT' +'A'
comp_dna = 'ATA'   

ATYT
TAA
'''
dna = input("Enter the DNA Sequence: ")
comp_dna = ""
flag_encoded = 1  
if dna == "":
      print("")  
else:
      for i in range(len(dna)):
            if(dna[i]=='A'):
                  comp_dna += 'T'
            elif(dna[i]=='T'):
                  comp_dna += 'A' # comp_dna = comp_dna + 'A'
            elif(dna[i]=='C'):
                  comp_dna += 'G'
            elif(dna[i]=='G'):
                  comp_dna += 'C'
            else:
                  flag_encoded = 0
                  print("Wrong Encoding")
                  break
            
      if(flag_encoded):
            print(comp_dna)
            
            
'''
Convert Q2 into a function, assuming that if its wrongly encoded, 
we return an empty string.
'''
def return_comp(dna):
      dna = input("Enter the DNA Sequence: ")
      comp_dna = ""
      if dna == "":
            return dna # return "" 
      else:
            for i in range(len(dna)):
                  if(dna[i]=='A'):
                        comp_dna += 'T'
                  elif(dna[i]=='T'):
                        comp_dna += 'A' # comp_dna = comp_dna + 'A'
                  elif(dna[i]=='C'):
                        comp_dna += 'G'
                  elif(dna[i]=='G'):
                        comp_dna += 'C'
                  else:
                        return "" # For Wrong Encoding, returning empty string. Similar to applying break statement.
                  
            return comp_dna