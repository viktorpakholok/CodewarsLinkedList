'''A solution of "Linked Lists - Move Node"'''

class Node(object):
    '''Represents a node in a linked list'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    '''Represents the context for moving a node from one linked list to another'''
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source: 'Node', dest: 'Node') -> 'Node':
    '''Moves a node from the source linked list to the destination linked list'''
    if not source:
        raise ValueError
    res = Node(source.data)
    res.next = dest
    return Context(source.next, res)
