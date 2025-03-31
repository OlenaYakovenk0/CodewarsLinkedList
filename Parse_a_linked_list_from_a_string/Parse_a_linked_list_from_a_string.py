class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def stringify(node):
    res = ''
    current = node
    while current:
        res += str(current.data) + ' -> '
        current = current.next
    return res + "None"

def linked_list_from_string(s):
    components = s.split(' -> ')[:-1][::-1]
    if len(components) < 1:
        return None
    head = Node(int(components[0]))
    for el in components[1:]:
        head = Node(int(el), head)
    return head

res = (linked_list_from_string("1 -> 2 -> 3 -> None"))
print(stringify(res))
