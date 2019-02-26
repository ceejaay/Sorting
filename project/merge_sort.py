def merge(arrA, arrB):
    print(arrA)
    # create a new array of size of the len of array left plus array right.
    # new_array = []
    # print(arrA + arrB)
    # for i in range(0, len(arrA) - 1):
    #     print(arrA[i])
        # new_array.append(arrA[i])
        # print(f"l: {arrA}, r: {arrB}")
        # not sure what to do here.
    # print('new array', new_array)
    return new_array
    # for all the elements
    #     if all elements in array A have been merged. Put next element into array B. into merged array
    #     elif all the elements in array B hbvE been merged. Put next elementd in array A into merged array
        # elif nex element in array A smaller. Then add it to the merged array.

    # elif  next element in array B is smaLlbr, add it to the merged array
def merge_sort(arr):
    # left = []
    # right = []
    if len(arr) > 1:
        # we divide the array until it is down to 1
        # We use slices to cut the array in half.
        left = merge_sort(arr[0 : len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2 :])
        arr = merge(left, right)
        # print(f"right {right}, left: {left}")

    
    return arr 
print(merge_sort([4, 3, 6, 7, 8, 99]))
