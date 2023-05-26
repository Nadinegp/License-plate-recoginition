import numpy as np
import time
import matplotlib.pyplot as plt

# Define the two bubble sort implementations
def bubble_sort1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubble_sort_improved(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True

# Generate some input sizes and corresponding CPU times
input_sizes = np.arange(1000, 5001, 500)
cpu_times1 = []
cpu_times2 = []

for size in input_sizes:
    arr = np.random.randint(0, 1000, size=size)
    
    start_time = time.process_time()
    bubble_sort1(arr)
    end_time = time.process_time()
    cpu_times1.append(end_time - start_time)
    
    start_time = time.process_time()
    bubble_sort_improved(arr)
    end_time = time.process_time()
    cpu_times2.append(end_time - start_time)

# Plot the CPU time data for both implementations
plt.plot(input_sizes, cpu_times1, label='Bubble Sort Normal')
plt.plot(input_sizes, cpu_times2, label='Bubble Sort Improved')

# Add axis labels and a title
plt.xlabel('Input Size')
plt.ylabel('CPU Time (s)')
plt.title('CPU Time Comparison of Bubble Sort Implementations')

# Add a legend
plt.legend()

# Show the plot
plt.show()
