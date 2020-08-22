# Quicksort is an efficient sorting algorithm. It is an divide and conquer algorithm.
# Average performance: O(n log n). Worst case: O(n^2).
import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        r = random.randint(0, len(arr) - 1)     # Random int for select pivot element in random way.
        pivot = arr.pop(r)                      # Random selection of pivot element makes average 
        less = [x for x in arr if x <= pivot]   # time of the algorithm close to n*log(n).
        greater = [x for x in arr if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    arr = list(map(int, input('enter integers separated by spaces ').split()))
    print(f'{arr} \nsorted array: => {quick_sort(arr)}')
