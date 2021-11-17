def removeElements(head, val):
    if head is None:
        return head

    prev = None
    curr = head # pointer
    while curr:
        if curr.val == val and prev is None: # the head
            head = curr.next
            curr = head
            # curr = curr.next # will not change head
        elif curr.val == val: # not the head
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = prev.next
    
    return head