def selectionsort(A):
    n = len(A)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if (A[j] < A[min]):
                min = j
        temp = A[i]
        A[i] = A[min]
        A[min] = temp
    return A
