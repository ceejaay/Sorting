### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


### recursive sorting function
def merge_sort( arr ):
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : len( arr ) / 2 ] )
        right = merge_sort( arr[ len( arr ) / 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort( arr, low, high ):
    # set a pivot
    # pivot on the recursion, is the high on either side of the partition
    # len(arr) - 1 is what we pass in to the arguments on the first call of the method
    pivot = high

    # go through each item. If it's less than. Move it to the left.
    # if it's greater than. Move it to the right
    flag = low
    # this is the base case
    if low < high:
        for i in range(low, high - 1):
            if arr[i] < arr[pivot]:
                arr[i], arr[flag] = arr[flag], arr[i]
                flag += 1
        # swap flag with pivot
        arr[pivot], arr[flag] = arr[flag], arr[pivot]
                # swap with ??? to put it on the low side
        # here we do the recursion
        # low is the bottom of the left partition or the bottom of the right partiion.
        # high is the end of the partition on either the left or right
        # the pivot is sorted the high and low are __outside__ the pivot
        quick_sort(arr, flag + 1, high)
        quick_sort(arr, low, flag - 1)


    # Then move the the pivot to the right place. 
    # Between the two halves

#     Then we pass the array and the high and the low to the array recursively.
    # what is high?
    # low is the beginning of the left or right side of the array.
    # what is low?
    # high is the end of the left or right side of the array

    return arr

a = [5, 3, 7, 2, 1, 0, 10, 33, 22, 68, 4]
print(quick_sort(a, 0, len(a) -1))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):
    pass 
    return arr
