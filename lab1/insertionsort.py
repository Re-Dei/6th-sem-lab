def insertionsort(A):
    n = len(A)
    for i in range(0, n):
        key = A[i]
        j = i - 1
        while (j >= 0 and A[j] > key):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
    return A
    