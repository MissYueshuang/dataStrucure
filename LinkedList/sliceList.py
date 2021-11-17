from LinkedList.ListNode import ListNode
from LinkedList.add_node import add_node

def slice_linked_list(head,left,right):

    index=1

    next_node = head.next
    next_node = add_node(next_node,ListNode())
    curr = head    
    curr.next = None

    left_slice = ListNode()
    to_reverse = ListNode()
    right_slice = ListNode()

    while next_node:
        # print(index)
        if index < left:
            left_slice = add_node(left_slice,curr)

        elif index >= left and index <= right:
            to_reverse = add_node(to_reverse,curr)

        else: # index > right:
            right_slice = add_node(right_slice,curr)

        temp = next_node.next

        curr = next_node    
        curr.next = None

        next_node = temp
        index += 1

    return left_slice.next, to_reverse.next, right_slice.next