# Selection sort is an in-place comparison sorting algorithm.
# The average speed: O(n^2)
def find_smallest(arr):
    """Helper function to find smallest index."""
    smallest = arr[0]
    s_index = 0
    for i, item in enumerate(arr):
        if item < smallest:
            smallest = item
            s_index = i
    return s_index


def selection_sort(arr):
    """Main sort algorithm"""
    result = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        result.append(arr.pop(smallest))
    return result


if __name__ == '__main__':
    arr = list(map(int, input('enter integers separated by'
                              'spaces: ').strip().split()))
    print(f'Sorted list: {selection_sort(arr)}')
