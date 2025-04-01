class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def reverse(head):
    if not head:
        return head
    res = Node(head.data)
    current = head.next
    while current:
        res = Node(current.data, res)
        current = current.next
    return res

def stringify(node):
    res = ''
    current = node
    while current:
        res += str(current.data) + ' -> '
        current = current.next
    return res + "None"

linked_list = Node(1, Node(2, Node(3, None)))
print(stringify(linked_list))
print(stringify(reverse(linked_list)))

linked_list = None
print(stringify(linked_list))
print(stringify(reverse(linked_list)))
