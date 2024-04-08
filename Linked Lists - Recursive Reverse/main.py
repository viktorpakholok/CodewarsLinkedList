'''A solution of "Linked Lists - Recursive Reverse"'''

class Node(object):
    '''Represents a node in a linked list'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head: 'Node') -> 'Node':
    '''Reverses a linked list iteratively'''
    if not head or not head.next:
        return head
    res = Node(head.data)
    to_change = res

    def reverse_def(head: 'Node', count: int = 0) -> 'Node':
        '''Helper function to reverse the linked list recursively'''
        nonlocal to_change
        nonlocal res
        if not head and count == 0:
            return None

        if head and head.next is not None:
            reverse_def(head.next, count = count + 1)

        to_change.data = head.data
        if not count:
            to_change.next = None
        else:
            to_change.next = Node(None)
            to_change = to_change.next
    reverse_def(head)

    return res
