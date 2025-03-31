class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    while index > 0 and node.next:
        node = node.next
        index -= 1
    if index != 0 or not node:
        raise Exception
    return node

linked_list = Node(1, Node(2, Node(3, None)))
print(get_nth(linked_list, 0).data)
linked_list = Node(1, Node(2, Node(3, None)))
print(get_nth(linked_list, 1).data)
linked_list = Node(1, Node(2, Node(3, None)))
print(get_nth(linked_list, 3).data)
