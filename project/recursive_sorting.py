### helper function
import random
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
#uncomment this for tests
    # for i in range( 0, elements ):
    #     if a >= len(arrA):    # all elements in arrA have been merged
    #         merged_arr[i] = arrB[b]
    #         b += 1
    #     elif b >= len(arrB):  # all elements in arrB have been merged
    #         merged_arr[i] = arrA[a]
    #         a += 1
    #     elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
    #         merged_arr[i] = arrA[a]
    #         a += 1
    #     else:  # else, next element in arrB must be smaller, so add it to final array
    #         merged_arr[i] = arrB[b]
    #         b += 1
    # return merged_arr


### recursive sorting function
def merge_sort( arr ):
    pass
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : len( arr ) / 2 ] )
        right = merge_sort( arr[ len( arr ) / 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    pass
    # TO-DO

# uncomment return
    # return arr

def merge_sort_in_place(arr, l, r): 
    pass
    # TO-DO

# uncomment return
    # return arr


# a = [random.randint(0, 10) for i in range(0, 10)]kk
# high - count: 18, i: 5
#  high - count: 17, i: 7
#   high - count: 16, i: 8
#    high - count: 15, i: 9
#     high - count: 14, i: 11
#      high - count: 13, i: 12
#       high - count: 12, i: 14
#        high - count: 11, i: 15
#         high - count: 10, i: 16
#          high - count: 9, i: 17
#           high - count: 8, i: 18
###[12, 3, 1, 9, 7, 6, 8, 15, 13, 16, 16, 14, 12, 17, 10, 18, 5, 3, 3, 20]
a = [12, 3, 1, 9, 7, 20, 8, 16, 16, 14, 3, 13, 17, 10, 18, 5, 3, 12, 15, 6]
# print(len(a))
# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort( arr, low, high ):
    # low and high point at the start and end of the array
    # low = 0
    # high = len(arr)
    pivot = 0
    count = 0

    if low < high:
        for i in range(low, high):
            if arr[i] > arr[pivot]:
                a = arr[i]
                # high len(arr) - 1
                b = arr[high - count]
                arr[i], arr[high - count] = b, a
                count += 1
                print(f" high - count: {high - count}, i: {i}")
        pivot = arr[high - count]
        x = arr[pivot]
        y = arr[high - count]
        arr[pivot], arr[high - count] = y, x
        # else:
        #     a = arr[i]
        #     b = arr[low]
        #     arr[i], arr[low] = b, a
    # Quick_sort recursion goes here. Deincrementing the high and low

        # quick_sort(arr, low, high - count - 1 )
        # quick_sort(arr, high - count + 1, high)
    return arr

    # While high and low are greater than one
    # quick_sort(arr, , high)
    # quick_sort(arr, low, high)


    # How to quick sort
    # select a pivot. Like the middle.
    # move all elements smallther than the pivot tot he left
    # move all elements larger than the pivot to the right.
    # While left side and right sight are greater than one Repeat steps one to three on each side.







    # print(low)
    # print(high)

print(quick_sort(a, 0, len(a) -1))
# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):
    pass
# uncomment return
    # return arr
