''''''

class Node(object):
    ''''''
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    ''''''
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
