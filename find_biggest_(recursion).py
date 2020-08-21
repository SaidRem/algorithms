# Finds the biggest element using recursion


def the_biggest(arr):
    # Base case if length of array equals 2 .
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    # Recursion case.
    sub_max = the_biggest(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    print(the_biggest(arr))
