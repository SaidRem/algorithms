def binary_search(arr, target):
    high = len(arr) - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2
        res = arr[mid]
        if target > res:
            low = mid + 1
            continue
        elif target < res:
            high = mid - 1
            continue
        return 'Target found'
    return 'target not found'


if __name__ == '__main__':
    arr = list(map(int, input('enter integers in order (separated by spaces): '
                              ).strip().split()))
    target = int(input('enter number: '))
    print(binary_search(arr, target))
