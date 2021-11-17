class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def split(list):
    '''
    Take O(k log n) Time
    k is the time used for slice 
    '''
    mid = len(list)//2
    left = list[:mid] # slice 1, O(k)
    right = list[mid:] # slice 2, O(k)
     
    return left, right

def merge(left,right):
    """
    merges two list, sorting them in the process, returns a new merged list
    Overall Take O(n) Time
    """
    l = []
    i = 0 
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    # right list is shorter
    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def merge_sort(list):
    '''
    O(kn log n) Time
    '''
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54,62,93,17,77,31,44,55,20]
l = merge_sort(alist)
print(l)

verify_sorted(alist)
verify_sorted(l)

