import numpy as np
 
def printDiagonalSums(mat, n):
 
    principal = 0
    secondary = 0
    for i in range(0, n):
        principal += mat[i][i]
        secondary += mat[i][n - i - 1]
         
    print("Principal Diagonal:", principal)
 

n = 4
A = np.random.randint(10, size=(n,n))
print(A)
printDiagonalSums(A, 4)
 