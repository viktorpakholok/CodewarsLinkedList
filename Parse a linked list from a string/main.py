'''A solution of "Parse a linked list from a string"'''

def linked_list_from_string(s: str) -> 'Node':
    '''Constructs a linked list from a string representation'''
    list_s = s.split(' -> ')[::-1][1:]
    res = None
    for el in list_s:
        res = Node(int(el), res)
    return res
