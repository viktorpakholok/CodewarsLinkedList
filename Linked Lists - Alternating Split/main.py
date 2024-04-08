''''''

class Node(object):
    ''''''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    ''''''
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    ''''''
    counter, first, second, res_1, res_2 = 0, None, None, None, None
    while head:
        if not counter % 2:
            if first is None:
                first = Node(head.data)
                res_1 = first
            else:
                first.next = Node(head.data)
                first = first.next
        else:
            if second is None:
                second = Node(head.data)
                res_2 = second
            else:
                second.next = Node(head.data)
                second = second.next
        head = head.next

        counter += 1

    if res_2 is None:
        res_2 = Node(head.data)

    return Context(res_1, res_2)
