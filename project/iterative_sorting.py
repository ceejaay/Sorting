# I did a pull request to the original fork.
# Complete the selection_sort() function below in class with your instructor
# slection sort
# First look through all the cards and find the smallest.
# then move the card to the correct positions in the dataset. Swap it with whatever is at the far left.
#repeat this sequence till things are done
# Look for the next smallest card.
# Don't have to look at the smallest.
# move it to the correct spot



import random
def selection_sort( arr ):
    return arr


# print(selection_sort(a))

# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    # for item in range(1, len(arr)):
    #     temp = arr[0]
    #     while item > 0 and arr[]
    # When we go through the while loop. How do we know to stop? 
    # We know that we stop when we are going forward in the for loop.
    # We know that we need to stop teh while loop when teh item on the left is smaller than the temp item.
    # While the temp item is greater than zero. We keep moving do this.

    # Then the temp item is changed to the the next item in the for loop.
    # temp = arr[1]
    # for item in range(1, len(arr)):
    #     while temp < arr[item]:
    #         arr[item] = arr[item + 1]
    






    # We set the first item in the array as sorted.

            # We check the temp agains the neighbor to it's left.
            # if temp is larger. Leave it there.
            # # While the temp variable is larger than it's neighbor we leave it there. then we go to the next item in the array.
            # We set that to temp.
            # Then we check on the way down.
            # Checking each one against the left neighbor. When we find the spot where there the value is less than. We insert the temp item there.
            # We keep doing this. as the for loop increments. And when it does get all the way to the end. jk

    # for item in range(1, len(arr)):
    # start the for loop.
    # first sorted.
    # the second is the temp
    # Start the while loop.
    #     while the temp is larger than the items down  to 0
    #         we compare the temp item to it's neighbor to the left
    #         if the temp variable is larger. Then we stop. If it is less than, 
    #             We keep moving down until there is one that is less than. Or rather the temp variable is larger. than the one on the left.
    #             If the variable on the left is smaller, then we break the loop. Set a new temp and start over.






    return arr

# import random

# a = [random.randint(0, 100) for i in range(0, 100)]
# print(insertion_sort(a))

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    pass

    # return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    pass

    # return arr
