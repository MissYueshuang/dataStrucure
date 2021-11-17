from LinkedList.ListNode import ListNode

def mergeTwoLists(l1, l2):
    """
    Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode

    """
    current = ListNode(0)

    merged = current

    while l1 or l2:
        if l1 is None:             
            merged.next = l2
            l2 = l2.next
        elif l2 is None: 
            merged.next = l1
            l1 = l1.next
        else:
            if l1.val < l2.val:
                merged.next = l1      
                l1 = l1.next
            else:
                merged.next = l2 
                l2 = l2.next
        
        merged = merged.next

    current = current.next

    return current