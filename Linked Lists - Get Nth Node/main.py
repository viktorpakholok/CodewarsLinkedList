'''A solution of "Linked Lists - Get Nth Node"'''

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next: 'Node'=None):
        self.data = data
        self.next = next

def get_nth(node, index: int) -> 'Node':
    '''Returns the node at the specified index in a linked list'''
    if index < 0 or not node:
        raise ValueError
    count = 0
    while count < index:
        if not node.next:
            raise ValueError
        node = node.next
        count += 1
    return node
