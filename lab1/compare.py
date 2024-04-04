import numpy as np
import matplotlib.pyplot as plt
from selectionsort import selectionsort
from insertionsort import insertionsort
import time

def generateArray(n: int):
    return [np.random.randint(0, 1000000) for _ in range(n)]

def compare(n: int):
    A = generateArray(n)
    
    begin = time.time()
    insertionsort(A)
    end = time.time()
    insertion_time = end - begin

    begin = time.time()
    selectionsort(A)
    end = time.time()
    selection_time = end - begin

    return insertion_time, selection_time

def main():
    sizes = [10, 50, 100, 500, 1000, 5000, 10000]
    insertion_times = []
    selection_times = []

    for size in sizes:
        insertion_time, selection_time = compare(size)
        insertion_times.append(insertion_time)
        selection_times.append(selection_time)

    plt.plot(sizes, insertion_times, label='Insertion Sort')
    plt.plot(sizes, selection_times, label='Selection Sort')
    plt.xlabel('Array Size')
    plt.ylabel('Time (s)')
    plt.title('Comparison of Insertion Sort and Selection Sort')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
