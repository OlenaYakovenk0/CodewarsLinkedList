<<<<<<< HEAD
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
    head = Node(components[0])
    for el in components[1:]:
        print(el)
        head = Node(el, head)

    return head

res = (linked_list_from_string("1 -> 2 -> 3 -> None"))
=======
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
    head = Node(components[0])
    for el in components[1:]:
        print(el)
        head = Node(el, head)

    return head

res = (linked_list_from_string("1 -> 2 -> 3 -> None"))
>>>>>>> 3490f9948536260b3176b5889b9749e25465dbe7
print(stringify(res))