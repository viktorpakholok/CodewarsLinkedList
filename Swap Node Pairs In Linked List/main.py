'''A soultion of "Swap Node Pairs In Linked List"'''

class Node:
    '''Represents a node in a linked list'''
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head: 'Node') -> 'Node':
    '''Swaps pairs of neighbouring nodes in a linked list'''
    if head is None or head.next is None:
        return head

    res = None
    while head and head.next:
        next_, first, second = head.next.next, head, head.next
        if not res:
            res = second
        second.next, first.next = first, next_
        head = head.next
        if head and head.next:
            first.next = head.next
    return res
