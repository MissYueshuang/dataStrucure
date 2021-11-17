class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        # return 'node value is %d'% self.val
        nodes = ["[%d]" % self.val]
        current = self.next
        while current:
            nodes.append("[%s]" % current.val)
            current = current.next
        return  '-> '.join(nodes)
