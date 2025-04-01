class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def stringify(node):
    res = ''
    current = node
    while current:
        res += str(current.data) + ' -> '
        current = current.next
    return res + "None"

def alternating_split(head):
    if not head or not head.next:
        raise Exception

    first = head
    second = head.next

    first_current = first
    second_current = second

    while second_current and second_current.next:
        first_current.next = second_current.next
        second_current.next = second_current.next.next

        first_current = first_current.next
        second_current = second_current.next

    first_current.next = None
    # print('first', stringify(first))
    # print('second', stringify(second))
    return Context(first, second)

linked_list = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(stringify(linked_list))
alternating_split(linked_list)
