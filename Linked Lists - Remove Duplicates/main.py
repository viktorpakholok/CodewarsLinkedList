''''''

class Node(object):
    ''''''
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    ''''''
    if head is None or head.next is None:
        return head
    to_change = head
    while to_change:
        while to_change.next and to_change.data == to_change.next.data:
            to_change.next = to_change.next.next
        to_change = to_change.next
    return head
