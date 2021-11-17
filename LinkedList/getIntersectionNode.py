def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    currA = headA
    currB = headB    
    lenA = 0
    lenB = 0
    
    while currA: # size A
        lenA += 1
        currA = currA.next

    while currB: # size B
        lenB += 1
        currB = currB.next

    currA = headA
    currB = headB       
    while lenA != lenB:
        if lenA > lenB:
            currA = currA.next
            lenA += -1
        else: # lenB > lenA
            currB = currB.next
            lenB += -1
    
    while currA != currB: # same length now
        currA = currA.next
        currB = currB.next
    
    return currA