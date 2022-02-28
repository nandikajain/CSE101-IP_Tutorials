# Tutorial Questions:
'''
In mathematics, a matrix (plural matrices) is a rectangular array or 
table of numbers, symbols, or expressions, arranged in rows and columns, 
which is used to represent a mathematical object or a property of such an object.

Square Matrix → Rows and Columns have the same dimension (i.e, their number is the same)

Matrix_A = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
Matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
1
2
3
4
5
6
7
8
9
for i in range(0, len(Matrix_A)): #2
      for j in range(0, len(Matrix_A[0])):
            res[i][j] = Matrix_A[i][j]+ B[i][j]

B = [[1,2],
     [3,4],
     [5, 6]]
     no_of_rows = len(B)
     no_of_cols = len(B[0])
     
for i in l:
      for j in i:
            print(j, end=" ")
      print()
'''
# Q: generic function that accepts such list of lists and prints in the matrix form

def printMatrix(M):
      n_row = len(M)
      for r in range(n_row):
            print(*M[r]) # Will print space separated matrix.
            
'''


Given 2 matrix, perform the following operations:
A. Matrix Addition
B. Matrix Subtraction
C. Matrix Transpose
D. Matrix Multiplication -> HW
axb bxc => axc
1 2 3
[i for i in input().split()] -> [1, 2,3]

[fun(X1), fun(X2), ... fun(Xn)]-> len-> n_row
M1[i][j]+ M2[i][j]
[[a, b, c, ...n], [], [], []]
'''

def addMatrix(M1, M2):
      n_row = len(M1)
      n_col = len(M1[0])
      addition_matrix = [[ M1[i][j]+ M2[i][j] for j in range(n_col)] for i in range(n_row)]
      # for i in range(n_row):
      #       l1=[]
      #       for j in range(n_col):
      #             l1.append(M1[i][j] + M2[i][j])
      #       addition_matrix.append(l1)
      
def subMatrix(M1, M2):
      n_row = len(M1)
      n_col = len(M1[0])
      addition_matrix = [[ M1[i][j]- M2[i][j] for j in range(n_col)] for i in range(n_row)]

'''
Transpose:
[[1, 2],
[3, 4]]
after Transpose:
[[1, 3],
[2, 4]]
'''

def transposeMatrix(M1):
      n_row = len(M1)
      n_col = len(M1[0])
      transpose = [[M[j][i] for j in range(n_row)]for i in range(n_col)]
      
def MatrixTranspose(MatrixQ,m,n):
      # m -> n_row, n -> n_col
      MatrixTranspose=[] 
      Matrix=[]
      for j in range(0,n):
            for i in range(0,m):
                  Matrix.append(MatrixQ[i][j])
            MatrixTranspose.append(Matrix)
            Matrix = []

def MatrixMult(A, B):
      # aXb, bxc = > axc
      # iterating by row of A
      for i in range(len(A)):
      # iterating by column by B
            for j in range(len(B[0])):
            # iterating by rows of B
                  for k in range(len(B)):
                        result[i][j] += A[i][k] * B[k][j]

def MatrixM(MatrixT,MatrixA):
      MatrixR=[] #Contruction of Matrix R of order nxn
      Matrix=[]
      n=len(MatrixT) #no of rows of required matrix
      m=len(MatrixA[0]) #no of columns of matrix A
      for i in range(0,n):
            for j in range(0,m):
                  l=0
                  for k in range(0,len(MatrixA)):
                        l+=MatrixT[i][k]*MatrixA[k][j]
                  Matrix.append(l)
            MatrixR.append(Matrix)
            Matrix=[]

	