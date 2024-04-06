'''Solution of a "Linked Lists - Push & BuildOneTwoThree"'''

class Node:
    '''Represents a node in a linked list'''
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data) -> 'Node':
    '''Inserts a new node with the given data at the beginning of the linked list'''
    node = Node(data)
    node.next = head
    return node

def build_one_two_three() -> 'Node':
    '''Constructs a linked list with three nodes containing data 1, 2, and 3 respectively'''
    return push(push(push(None, 3), 2), 1)
