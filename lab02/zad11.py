# Python function to print common elements in three sorted arrays
def findCommon(L1, L2, L3, n1, n2, n3):
     
    # Initialize starting indexes for L1[], L2[] and L3[]
    i, j, k = 0, 0, 0
     
    # Iterate through three arrays while all arrays have elements   
    while (i < n1 and j < n2 and k< n3):
         
        # If x = y and y = z, print any of them and move ahead
        # in all arrays
        if (L1[i] == L2[j] and L2[j] == L3[k]):
            print(L1[i])
            i += 1
            j += 1
            k += 1
         
        # x < y   
        elif L1[i] < L2[j]:
            i += 1
             
        # y < z   
        elif L2[j] < L3[k]:
            j += 1
         
        # We reach here when x > y and z < y, i.e., z is smallest   
        else:
            k += 1
 
# Driver program to check above function
L1 = [1, 5, 10, 20, 40, 80]
L2 = [6, 7, 20, 80, 100]
L3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(L1)
n2 = len(L2)
n3 = len(L3)
print("Common elements are: ")
findCommon(L1, L2, L3, n1, n2, n3)
