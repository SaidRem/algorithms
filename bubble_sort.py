
def bubble_sort(arr):
    swaps = 0
    for _ in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr.insert(i + 1, arr.pop(i))
                swaps += 1
    return arr, swaps


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    arr, swaps = bubble_sort(a)
    print(f'Array is sorted in {swaps} swaps.\n'
          f'First Element: {arr[0]}\n'
          f'Last Element: {arr[-1]}')
