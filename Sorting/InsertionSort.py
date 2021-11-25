def InsertionSort(arr):
    """
    Worst Case: O(n^2)
    """
    for i in range(1,len(arr)):
        key = arr[i] # key is the value to insert
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j] # shift
            j -= 1
        arr[j+1] = key
    
    return arr