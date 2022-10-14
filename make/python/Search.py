'''
Encoding: UTF-8
Title: binary_search.py
Created: 2022-10-13 20:17:06
@author: samantix
'''


class Search(object):
    '''
    search iterables
    '''

# ----------------------------------------------------------
    def __init__(self, arr, target):
        self.arr = arr
        self.x = target
# ----------------------------------------------------------

    def via_binary_recur(self):

        result = self.binary_recur()

        if result != -1:
            print(f"Element '{self.x}' is present at index {result}")
        else:
            print("Element is not present in array")

# ----------------------------------------------------------

    def via_binary_iter(self):

        result = self.binary_iter()

        if result != -1:
            print(f"Element '{self.x}' is present at index {result}")
        else:
            print("Element is not present in array")

# * ----------------------------------------------------------

    def binary_iter(self):
        '''
        Returns index of x in arr if present, else -1
        '''

        arr, x = self.arr, self.x
        low, high = 0, len(arr) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2

            # i.e, if index of value x = mid, we found it
            if arr[mid] == x:
                return mid

            # If x is greater, ignore left half
            elif arr[mid] < x:
                low = mid + 1

            # If x is smaller, ignore right half
            else:
                high = mid - 1

        # If we reach here, then the element was not present
        return -1


# * ----------------------------------------------------------


    def binary_recur(self, low=0, high=None):
        '''
        Returns index of x in arr if present, else -1
        '''

        arr, x = self.arr, self.x
        high = high or len(arr) - 1

        # Check base case
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return self.binary_recur(low, mid - 1)

            # Else the element can only be present in right subarray
            else:
                return self.binary_recur(mid + 1, high)

        else:
            # Element is not present in the array
            return -1


# ! ----------------------------------------------------------

# @ --------------------------------------------- @
# @                   TESTING                     @
# @ --------------------------------------------- @

arr = [2, 3, 4, 10, 40]
target = 10

# arr = ['a', 'b', 'c', 'd', 'e', 'f']
# target = 'e'

Search(arr, target).via_binary_iter()
Search(arr, target).via_binary_recur()


# ----------------------------------------------------------
