def deleteDuplicates(head):
    if head == None or head.next == None: # length is 0 or 1
        return head

    li = [head.val]
    prev = head
    curr = head.next

    while curr:        
        if curr.val in li:
            prev.next = curr.next
        else:
            prev = prev.next
        li.append(curr.val)
        curr = curr.next                    
    
    return head