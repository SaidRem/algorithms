# Bubble sort is a simple sorting algorithm that iterates
# over a list, comparing elements in pairs and swapping them
# up until the larger elements "bubble up" to the end of the
# list, and the smaller elements stay at the "bottom".
# Worst-case performance O(n^2) comparisons, O(n^2) swaps
# Best-case performance O(n) comparisons, O(1) swaps
# Average performance	O(n^2) comparisons, O(n^2) swaps


def bubble_sort(arr):
    swaps = 0
    for bypass in range(len(arr)-1):
        for i in range(len(arr)-1-bypass):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps += 1
    return arr, swaps



if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    arr, swaps = bubble_sort(a)
    print(f'Array is sorted in {swaps} swaps.\n'
          f'First Element: {arr[0]}\n'
          f'Last Element: {arr[-1]}')
