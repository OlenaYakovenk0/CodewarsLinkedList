class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def loop_size(node):
    rabbit = node.next.next
    turtle = node.next
    while rabbit!=turtle:
        rabbit = rabbit.next.next
        turtle = turtle.next
    current = turtle.next
    cnt = 0
    while current!=turtle:
        cnt += 1
        current = current.next
    return cnt + 1

meet = Node('*')
linked_list_1 = Node(1, Node(2, Node(3, Node(4, meet))))
linked_list_2 = Node(5, Node(6, Node(7, Node(8, meet))))
meet.next = linked_list_2
print(loop_size(linked_list_1))
