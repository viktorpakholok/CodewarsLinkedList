''''''

class Node:
    ''''''
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    ''''''
    if head is None or head.next is None:
        return head

    res = None
    while head and head.next:
        next_ = head.next.next
        first = head
        second = head.next
        if not res:
            res = second
        second.next = first
        first.next = next_
        head = head.next
        if head and head.next:
            first.next = head.next
    return res
