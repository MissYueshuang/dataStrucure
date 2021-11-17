def node_at_index(head, index):
    '''
    Return the node the given index
    '''
    if index == 0:
        return head

    current = head
    position = 0

    while position < index:
        current = current.next
        position += 1

    return current