def swap(arr,i,j):
    """
    swap the location of two element in an array
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def BubbleSort(Arr):
    """
    Worst case: O(n^2)
    Best case: O(n)
    """
    for k in range(len(Arr)): # run the whole loop k times
        flag = 0
        for i in range(len(Arr)-k-1):
            if Arr[i]>Arr[i+1]:
                Arr = swap(Arr,i,i+1)
                flag = 1
        if flag == 0:
            break
    return Arr
