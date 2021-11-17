from LinkedList.ListNode import ListNode
from LinkedList.add_node import add_node
from LinkedList.sliceList import slice_linked_list
from LinkedList.reverseList import reverseList

def ReverseList(head, left, right):
    """
    Reverse the linked list in between
    :param head: Head node of linked list
    :param left: Start position to reverse
    :param right: End position to reverse
    :return: New head with reversed linked list
    """
    if right - left < 0:
        print('Wrong input')
    elif right - left == 0:
        return head
    else:
        index = 1
        current = head
        if left == 1:
            node1 = None
            node2 = current
        else:
            while current and index < left - 1:
                current = current.next
                index += 1
            node1 = current
            index += 1
            node2 = current.next

        current = node2
        prev = None
        while current and index <= right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            index += 1
        if current:
            node2.next = current
        if node1:
            node1.next = prev
        else:
            head = prev
    return head

def reverseBetweenOld(head, left, right):
    """
    Given the head of a singly linked list and two integers left and right where left <= right, 
    reverse the nodes of the list from position left to position right, and return the reversed list.

    :type head: ListNode
    :type left: int
    :type right: int
    :rtype: ListNode
    """
    if head == None or head.next == None: # length is 0 or 1
        return head

    left_slice,to_reverse,right_slice = slice_linked_list(head,left,right)
    reversed = reverseList(to_reverse)

    res = ListNode()
    res = add_node(res,left_slice)
    res = add_node(res,reversed)
    left_slice = add_node(res,right_slice)

    return res.next