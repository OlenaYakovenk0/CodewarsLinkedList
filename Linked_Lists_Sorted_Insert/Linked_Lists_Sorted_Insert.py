class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def sorted_insert(head, data):
    current = head

    if not head:
        return Node(data)

    if data < head.data:
        return Node(data, head)

    while current.next and current.next.data < data:
        current = current.next

    current.next = Node(data, current.next)
    return head

def stringify(node):
    res = ''
    current = node
    while current:
        res += str(current.data) + ' -> '
        current = current.next
    return res + "None"

linked_list = Node(1, Node(2, Node(3, None)))
print(stringify(linked_list))
print(stringify(sorted_insert(linked_list, 0)))
