def deleteDuplicatesInSorted(head):
    if head == None or head.next == None: # length is 0 or 1
        return head

    prev = head

    while prev.next:        
        if prev.val == prev.next.val:
            prev.next = prev.next.next
        else:
            prev = prev.next

    return head