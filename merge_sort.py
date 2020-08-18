# Merge sort algorithm:
# 1. Divide the unsorted list into sublists, each containing one element (a list of one element is considered sorted).
# 2. Repeatedly merge sorted sublist to produce new sorted sublists until there is only one sublist remaining - this will be the sorted list.

# Pseudocode of merge sort algorithm:
# 
# Merge(A, p, q, r)
# 
# 1. n1 = q - p + 1
# 2. n2 = r - q
# 3. Let L[1...n1 + 1] and R[1...n2 + 1] - new arrays
# 4. for i = 1 to n1
# 5.      L[i] = A[p + i - 1]
# 6. for j = 1 to n2
# 7.      R[j] = A[q +j]
# 8. L[n1 + 1] = infinity
# 9. R[n2 + 1] = infinity
# 10. i = 1
# 11. j = 1
# 12. for k = p to r
# 13.     if L[i] <= R[j]
# 14.             A[k] = L[i]
# 15.             i = i + 1
# 16.     else A[k] = R[j]
# 17.             j = j + 1
# 
##############
# 
# Merge-Sort(A, p, r)
# 1. if p < r
# 2.      q = (p + r) / 2
# 3.      Merge-Sort(A, p, q)
# 4.      Merge-Sort(A, q + 1, r)
# 5.      Merge(A, p, q, r)
####################################
# PYTHON CODE:
import random

def merge(arr_left, arr_right):
    sorted_arr = []
    arr_left_index = arr_right_index = 0
    
    # Lenght often need to use, so lenght variable will be handy.
    arr_left_len, arr_right_len = len(arr_left), len(arr_right)
    for _ in range(arr_left_len + arr_right_len):
        if arr_left_index < arr_left_len and arr_right_index < arr_right_len:
            
            # Check which value from the start is smaller.
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list.
            if arr_left[arr_left_index] <= arr_right[arr_right_index]:
                sorted_arr.append(arr_left[arr_left_index])
                arr_left_index += 1
                
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list.
            else:
                sorted_arr.append(arr_right[arr_right_index])
                arr_right_index += 1
                
        # If reached the end of the left list, then add elements from 
        # right list to the sorted list.
        elif arr_left_index == arr_left_len:
            sorted_arr.append(arr_right[arr_right_index])
            arr_right_index += 1
        
        # if reached the end of the right list, then add elements from 
        # left list to the sorted list.
        elif arr_right_index == arr_right_len:
            sorted_arr.append(arr_left[arr_left_index])
            arr_left_index += 1
    return sorted_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    
    # Sort and merge each half.
    arr_left = merge_sort(arr[:mid])
    arr_right = merge_sort(arr[mid:])
    
    # Merge the sorted lists into new one.
    return merge(arr_left, arr_right)


def test(test_arr):
    temp = test_arr[:]
    random.shuffle(temp)
    random_sorted = merge_sort(temp)
    if random_sorted == test_arr:
        return 'All right'
    else:
        return 'Wrong'


if __name__ == '__main__':
    test_arr = list(range(100))
    for i in range(10):
        print(f'test №{i} is {test(test_arr)}')
