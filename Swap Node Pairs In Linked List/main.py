''''''

class Node:
    ''''''
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    ''''''
    if head is None or head.next is None:
        return head

    res = None
    while head and head.next:
        next_ = head.next.next
        print(f'next: {next_}')
        first = head
        print(f'first: {first}')
        second = head.next
        if not res:
            res = second
        print(f'second: {second}')
        second.next = first
        first.next = next_
        print(f'first.next: {first.next}')
        print(f'jead: {head}')
        head = head.next
        print(f'head: {head}')
        if head and head.next:
            print('if')
            first.next = head.next
    return res
