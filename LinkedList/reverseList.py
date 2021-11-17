def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    O(N) time
    """
    if head == None or head.next == None: # length is 0 or 1
        return head

    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev