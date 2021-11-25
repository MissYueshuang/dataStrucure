import random

def partition(arr, low, high):
    i = low        # pivot index
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            
            arr[i], arr[j] = arr[j], arr[i] # swap
            i = i+1
            
    arr[i], arr[high] = arr[high], arr[i]

    return i

def randomPartition(arr, low, high):

    pivot_idx = random.randint(low, high)
    arr[pivot_idx] , arr[high] = arr[high], arr[pivot_idx] # swap
    i = partition(arr,low,high)
    return i
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
 
def quickSort(arr,low,high):
    """
    Time Complexity:
    Best case: O(n log n) for balanced data
    Worst case: O(n^2)
    With randomness, we can also achieve best case

    Space Complexity:
    Best case: O(log n)
    worst case: O(n)
    """
    if len(arr) == 1:
        return arr

    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = randomPartition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    
    return arr
 
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]    
low = 0
high = len(arr) - 1
quickSort(arr, low, high)
