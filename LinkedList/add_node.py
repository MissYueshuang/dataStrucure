def add_node(Node,next_node):
    '''
    add a node to the tail of the linked list
    Node: current node
    next_node: The node you want to add
    '''
    current = Node
    while current.next is not None:
        current = current.next
    current.next = next_node
    return Node