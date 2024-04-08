'''A solution of "Parse a linked list from a string"'''

class Node:
    '''Represents a node in a linked list'''
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.data}, {self.next})"

def linked_list_from_string(s: str) -> 'Node':
    '''Constructs a linked list from a string representation'''
    list_s = s.split(' -> ')[::-1]
    res = None
    for el in list_s:
        if el != "None":
            res = Node(int(el), res if res else None)
    return res
