class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    current = head
    while current:
        if current.next and current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

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
