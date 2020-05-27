

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr.insert(j + 1, arr.pop(j))
            j = j - 1
    return arr


if __name__ == '__main__':
    arr = map(int, input('enter integers separated by spaces').split())
    print(f'{arr} => {insertion_sort(arr)}')
