# Constructor
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


# Linked List
class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


new_linked_list = LinkedList(10)

print(new_linked_list.head.value)
