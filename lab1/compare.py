import numpy as np
import matplotlib.pyplot as plt
from mergesort import mergesort
from insertionsort import insertionsort
import time

def generateArray(n: int):
    return [np.random.randint(0, 1000000) for _ in range(n)]

def compare(n: int):
    A = generateArray(n)
    B = A
    
    begin = time.time()
    mergesort(A)
    end = time.time()
    merge_time = end - begin
    
    begin = time.time()
    insertionsort(B)
    end = time.time()
    insertion_time = end - begin

    return insertion_time, merge_time

def main():
    sizes = [0, 150, 300, 450, 600, 750, 900, 1050, 1200, 1350, 1500]
    insertion_times = []
    merge_times = []

    for size in sizes:
        insertion_time, merge_time = compare(size)
        insertion_times.append(insertion_time)
        merge_times.append(merge_time)

    plt.plot(sizes, insertion_times, label='Insertion Sort')
    plt.plot(sizes, merge_times, label='Merge Sort')
    plt.xlabel('Array Size')
    plt.ylabel('Time (s)')
    plt.title('Comparison of Insertion Sort and Merge Sort')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
