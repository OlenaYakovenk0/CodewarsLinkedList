class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    res = ''
    current = node
    while current:
        res += str(current.data) + ' -> '
        current = current.next
    return res + "None"

print(stringify(Node(1, Node(2, Node(3)))))
