def merge(arrA, arrB):
    # we get the length of the new array
    new_length = len(arrA) + len(arrB)
    # we create a new array with zeros in it
    merged_arr = [0] * new_length
    # we set up some pointers.
    a = 0
    b = 0
    # then we loop through 0 to the length of the new array
    for i in range(0, new_length):
        # if a is greater than or equal to the length of arrA. then we merge in the 0 index element from the B array. 
        #     the value of a  is zero on the first pass
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            # we then increment b by one. So it will go to the next element in the b array
            b += 1
            # here we check to see if b is greater than or equal to  the length of the b array. 
            # if it's greather than b. Then we know that ?????

        elif b >= len(arrB):
            # if b is greater or equal. We merge arrB at index B into the merged_arr
            merged_arr[i] = arrA[a]
            # then we increment a by one 
            a += 1
            # here's where we compare the values if the array's are full of elements
            # the first element of the a array or the b array are bigger. We merge in the lesser one first
        elif arrA[a] < arrB[b]:
            # we merge in arrA[a]
            merged_arr[i] = arrA[a]
            # we increment a
            a += 1
        else:
            # otherwise we merge in arrA[a]
            merged_arr[i] = arrB[b]
            # then increment b
            # not sure what's going on here
            b += 1

    # 1. if all the elements from array A have been merged.
    #     put the next element from array B in to new array
        # put the item from b into the new array.
            # arrB[0] goes into the new array
            # arrA[0] goes into the new array.
        # put the item from a into the new array
    # 2. If all elements in array B have been merged put the next element from Array A into the new array.
    #  If you have to compare. 
    #  3. Array A first item is smaller. Then put it in new array
    # 4.  Or array B item is smaller. So put it into the new_array

    # create a new array of size of the len of array left plus array right.
    # we return the merged array. After everthing above is done. When the for loop completes.
    return merged_arr 


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
print(merge_sort([4, 8, 6, 7, 3, 99, 1, 4, 68, 45, 20, 0]))
