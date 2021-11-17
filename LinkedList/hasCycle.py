def hasCycle(head):
    while head != None:
        if head.val == None:
            return True
            
        head.val = None
        head = head.next

    return False      