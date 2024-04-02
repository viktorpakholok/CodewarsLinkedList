'''Solution to problem "Convert a linked list to a string"'''

class Node():
    '''Basic class Node from Preloaded'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node: 'Node') -> str:
    '''Accepts an argument node and returns a string representation of the node'''
    res = ''
    while node:
        res += str(node.data) + " -> "
        node = node.next
    return res + "None"
