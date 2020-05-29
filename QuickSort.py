import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        r = random.randint(0, len(arr) - 1)
        pivot = arr.pop(r)
        less = [x for x in arr if x <= pivot]
        greater = [x for x in arr if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    arr = list(map(int, input('enter integers separated by spaces ').split()))
    print(f'{arr} \nsorted array: => {quick_sort(arr)}')
