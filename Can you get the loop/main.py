'''A solution of "Can you get the loop ?"'''

class Node(object):
    '''Represents a node in a linked list'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

def loop_size(node: 'Node') -> int:
    '''Determines the size of the loop in a linked list, if it exists'''
    slow, fast = node, node

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

        if slow == fast:
            slow = node
            while slow != fast:
                slow, fast = slow.next, fast.next

            count = 1
            slow = slow.next
            while slow != fast:
                slow, count = slow.next, count + 1

            return count

    return None
