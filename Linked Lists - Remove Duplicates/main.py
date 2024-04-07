'''A solution of "Linked Lists - Remove Duplicates"'''

class Node(object):
    '''A class representing a node in a linked list'''
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head: 'Node') -> 'Node':
    '''Removes duplicate nodes from a sorted linked list'''
    if head is None or head.next is None:
        return head
    to_change = head
    while to_change:
        while to_change.next and to_change.data == to_change.next.data:
            to_change.next = to_change.next.next
        to_change = to_change.next
    return head
