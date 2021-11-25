def distance_fn(arr1,arr2) -> int:
    """
    This function return the distance of two vectors.
    input:
    arr1: vector
    arr2: vector

    output:
    res: float
    """
    if len(arr1) != len(arr2):
        ValueError('two vectors are of different length!')

    res = 0
    for i in range(len(arr1)):
        res += pow(arr1[i]+arr2[i],2)

    return pow(res,0.5)

def swap(arr,i,j):
    """
    swap the location of two element in an array
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def find_KNN(arr,point,k):
    '''
    O(n): n^2
    return the k nearest points to the given point in the arr 

    input:
    arr: array of points
    point: target point
    k: int

    output:
    res: array of points
    '''
    res = []
    distance = []
    for i in range(len(arr)):
        dis = distance_fn(arr[i],point)
        distance.append(dis)
        res.append(arr[i])
        if dis < distance[i-1]:
            j = i
            while distance[j] < distance[j-1]:
                distance = swap(distance,j-1,j)
                res = swap(res,j-1,j)
                j += -1             

    return res[:k]
