import numpy as np
import matplotlib.pyplot as plt
from mergesort import mergesort
from quicksort import quicksort
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
    quicksort(B, 0, len(B) - 1)
    end = time.time()
    quick_time = end - begin

    return quick_time, merge_time

def main():
    sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    quick_times = []
    merge_times = []

    for size in sizes:
        quick_time, merge_time = compare(size)
        quick_times.append(quick_time)
        merge_times.append(merge_time)

    plt.plot(sizes, quick_times, label='Quick Sort')
    plt.plot(sizes, merge_times, label='Merge Sort')
    plt.xlabel('Array Size')
    plt.ylabel('Time (s)')
    plt.title('Comparison of Quick Sort and Merge Sort')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()