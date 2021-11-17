from single_linked_list import SinglyLinkedList

def merge_sort(linked_list):
    """
    Sort a linked list in ascending order
    - Recursively divide the linked list into sublists comtaining a single node
    - Repeatedly merge the sublists to produce sorted sublists until on remains

    returns a sorted linked list

    O(kn log n)
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(linked_list):
    """
    Divided the unsorted list at midpoint into sublists
    O(k * log n)
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half,right_half

    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = SinglyLinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half,right_half

def merge(left,right):
    """
    Merge two linked lists, sorting by data in nodes
    return a new, merged list
    O(n)
    """
    merged = SinglyLinkedList()

    # add a fake head that is discarded later
    merged.add(0)

    # set the current to the head of the linked list
    current = merged.head

    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        # If the head node of the left is None, we are pst the tail.
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # call the next on right to set loop condition to False
            right_head = right_head.next_node
            # iF THE HEAD NODE OF RIGHT IS None, we are past the tail
            # add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # call the next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # not at either tail node
            # obtain node data to perform comparison
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        current = current.next_node

    # Discard fake head
    head = merged.head.next_node
    merged.head = head

    return merged

# l = SinglyLinkedList()
# l.add(10)
# l.add(2)
# l.add(44)
# l.add(15)
# l.add(200)

# print(l)

# sorted_linked_list = merge_sort(l)
# print(sorted_linked_list)