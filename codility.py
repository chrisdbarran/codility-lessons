# Codility tests module
def permCheck( A ):
    
    A.sort()

    # Read the instructions, the sequence must begin with 1!

    if A[0] != 1:
        return 0

    length = len(A)
    if length == 1:
        return 1

    
    for i in range(length):
        if i + 1 == length:
            return 1

        if A[i] + 1 != A[i+1]:
            return 0