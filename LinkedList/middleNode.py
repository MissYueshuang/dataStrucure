def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    curr = head
    lens = 0
    
    while curr: # size A
        lens += 1
        curr = curr.next

    midpoint = (lens)//2
    index = 0
    curr = head

    while index <= midpoint-1:
        curr = curr.next
        index += 1

    return curr