class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head

    res = Node('*', head)
    prev = res
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        prev.next = second
        first.next = second.next
        second.next = first

        prev = prev.next.next
    return res.next

def stringify(node):
    res = ''
    current = node
    while current:
        res += str(current.data) + ' -> '
        current = current.next
    return res + "None"

linked_list = Node('A', Node('B', Node('C', Node('D', Node('E', Node('F', Node('G', Node('K', Node('j')))))))))
print(stringify(linked_list))
print(stringify(swap_pairs(linked_list)))
