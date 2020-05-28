import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    arr = list(map(int, input('enter integers separated by spaces ').split()))
    print(f'{arr} \nsorted array: => {quick_sort(arr)}')
