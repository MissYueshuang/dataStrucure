def getDecimalValue(head):
    """
    :type head: ListNode
    :rtype: int
    """
    res = 0

    curr = head
    lens = 0
    
    while curr: 
        lens += 1
        curr = curr.next

    curr = head
    while lens > 0:
        res += curr.val * pow(2,(lens-1))
        lens += -1
        curr = curr.next

    return res