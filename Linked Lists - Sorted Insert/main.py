'''A solution of "Linked Lists - Sorted Insert"'''

class Node(object):
    '''A class representing a node in a linked list'''
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head: 'Node', data: int) -> 'Node':
    '''Inserts a new node with the given data into a sorted linked list'''
    if not head:
        return Node(data)
    if data < head.data:
        head, head.next = Node(data), head
        return head

    to_change = head
    while head:
        if to_change.next is None or data < to_change.next.data:
            inser = Node(data)
            inser.next = to_change.next
            to_change.next = inser
            return head

        to_change = to_change.next
    return head
