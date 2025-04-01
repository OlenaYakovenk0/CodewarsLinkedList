class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    if not head:
        return head

    res = Node(head.data)
    current_node = res
    current = head

    while current:
        if current.data != current_node.data:
            current_node.next = Node(current.data)
            current_node = current_node.next
        current = current.next
    return res

def stringify(node):
    res = ''
    current = node
    while current:
        res += str(current.data) + ' -> '
        current = current.next
    return res + "None"

linked_list = Node(1, Node(1, Node(2, Node(2, Node(3, Node(3, Node(3)))))))
print(stringify(linked_list))
print(stringify(remove_duplicates(linked_list)))

linked_list = Node(1, Node(2, Node(3, None)))
print(stringify(linked_list))
print(stringify(remove_duplicates(linked_list)))

# linked_list = None
# print(stringify(linked_list))
# print(stringify(remove_duplicates(linked_list)))
